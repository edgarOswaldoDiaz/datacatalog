# -*- coding: utf-8 -*-

import asyncio
from pyppeteer import launch

async def main():

    browser = await launch(executablePath='C:/Users/Ernesto/Downloads/chrome-win/chrome.exe')
    page = await browser.newPage()
    await page.goto('https://www.facebook.com')
    title = await page.title()
    print(title)
    await browser.close()

asyncio.run(main())

