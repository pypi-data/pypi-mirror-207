import asyncio

import requests
from lxml import etree
from pyppeteer import launch

headers = {
    'User-Agent':'User-Agent:Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
}

# url = 'https://new.qq.com/rain/a/20230427A00XLW00'
url = 'https://view.inews.qq.com/a/20230426A08LUH00'
async def main():
    browser = await launch(headless=False)
    page = await browser.newPage()
    await page.goto(url)

    # print(items)
    # await page.waitForSelector('.item .name')
    detailData = await page.evaluate('''()=> {
       return window.initData
    }''')

    print(detailData['content'].get('content').get('text'))
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())