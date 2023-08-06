import asyncio
import logging

import aiohttp
import pymongo
import requests
from motor.motor_asyncio import AsyncIOMotorClient
from pyppeteer import launch

logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(levelname)s : %(message)s')

headers = {
    # 'User-Agent':'User-Agent:Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    'content-type': 'application/json'

}
json = {"qimei36": "0_8386bd366dea9", "forward": "1", "base_req": {"from": "pc"}, "flush_num": 1,
        "channel_id": "news_news_finance", "device_id": "0_8386bd366dea9", "is_local_chlid": ""}
INDEX_URL = 'https://r.inews.qq.com/web_feed/getPCList'
DETAIL_URL = 'https://view.inews.qq.com/a/{id}'

# mongod --dbpath d:\mongodb\data\db
MONGO_CONNECTION_STRING = 'mongodb://localhost:27017'
MONGO_DB_NAME = 'news1'
MONGO_COLLECTION_NAME = 'qqfinance2'

client = AsyncIOMotorClient(MONGO_CONNECTION_STRING)
db = client[MONGO_DB_NAME]
collection = db[MONGO_COLLECTION_NAME]

WINDOWS_WIDTH, WINDOW_HEIGHT = 1366, 768
HEADLESS = False  # 这里设置非无头模式

browser, tab = None,None
async def init():
    global browser, tab
    browser = await launch(headless=HEADLESS,
                           args=['--disable-infobars', f'--window-size={WINDOWS_WIDTH},{WINDOW_HEIGHT}'])
    tab = await browser.newPage()
    await tab.setViewport({'width': WINDOWS_WIDTH, 'height': WINDOW_HEIGHT})


async def scrape_api(data):
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.post(INDEX_URL, json=data) as response:
            return await response.json()


async def scrape_index(data):
    return await scrape_api(data)


TIME_OUT = 5
async def scrape_detail(id):
    url = DETAIL_URL.format(id=id)
    try:
        await tab.goto(url)
        await asyncio.sleep(1)
        # await tab.waitFor(options={'timeout':TIME_OUT*1000})
    except TimeoutError:
        logging.error('爬取地址%s 超时了',url,exc_info=True)


async def parse_detail():
    detailData = await tab.evaluate('''()=> {
       return window.initData
    }''')
    return detailData


# 保存数据到mongodb
async def save_data(id,data):
    return await collection.update_one(
        {
            'id':id
        },
        {
            '$set': data
        }, upsert=True)


async def main():
    await init()
    try:
        for index in range(2):
            json['flush_num'] = index
            results = await scrape_index(json)
            for result in results.get('data'):
                id = result.get('id')
                await scrape_detail(id)
                detail_data = await parse_detail()
                logging.info('新闻id: %s 新闻标题: %s',detail_data['content'].get('id'),detail_data['content'].get('title'))
                await save_data(id,detail_data)
    finally:
        await browser.close()


if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop=loop)
    loop.run_until_complete(main())

# if response.status_code == 200:
#     result = response.json()
#     for item in result.get('data'):
#         id = item.get('id')
#         title = item.get('title')
#         publish_time = item.get('2023-04-28 07:00:00')
#         pic_info = item.get('pic_info')
#         print(pic_info.get('big_img'))
#         print(pic_info.get('small_img'))
#         print(pic_info.get('three_img'))
#         print("=================")
