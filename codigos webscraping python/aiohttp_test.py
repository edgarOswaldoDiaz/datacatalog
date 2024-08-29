# -*- coding: utf-8 -*-

import aiohttp
import asyncio
from bs4 import BeautifulSoup
import nest_asyncio

nest_asyncio.apply()

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, 'https://www.facebook.com')
        soup = BeautifulSoup(html, 'html.parser')
        print(soup.title.text)

asyncio.run(main())
