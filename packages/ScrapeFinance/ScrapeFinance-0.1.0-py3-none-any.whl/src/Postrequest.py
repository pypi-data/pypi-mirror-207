import asyncio

import aiohttp
import pymongo
import requests
from motor.motor_asyncio import AsyncIOMotorClient

headers = {
    # 'User-Agent':'User-Agent:Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    'content-type': 'application/json'

}
json = {"qimei36": "0_8386bd366dea9", "forward": "1", "base_req": {"from": "pc"}, "flush_num": 1,
        "channel_id": "news_news_finance", "device_id": "0_8386bd366dea9", "is_local_chlid": ""}
url = 'https://r.inews.qq.com/web_feed/getPCList'

# mongod --dbpath d:\mongodb\data\db
MONGO_CONNECTION_STRING = 'mongodb://localhost:27017'
MONGO_DB_NAME = 'news1'
MONGO_COLLECTION_NAME = 'qqfinance1'

client = AsyncIOMotorClient(MONGO_CONNECTION_STRING)
db = client[MONGO_DB_NAME]
collection = db[MONGO_COLLECTION_NAME]


async def scrape_api(data):
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.post(url, json=data) as response:
            return await response.json()


async def scrape_index(data):
    return await scrape_api(data)


#保存数据到mongodb
async def save_data(data):
    print(data)
    return await collection.update_one(
        {
            'id': data.get('id')
        },
        {
            '$set': data
        }, upsert=True)


async def main():
    for index in range(2):
        json['flush_num'] = index
        results = await scrape_index(json)
        for result in results.get('data'):
            print(result.get('id'))
            await save_data(result)

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
