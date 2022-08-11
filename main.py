import random

from rich import print
from rich.panel import Panel

import asyncio
import aiofiles
import validators
import argparse

from checker import checker


parser = argparse.ArgumentParser(description='linkchecker')
parser.add_argument('--filein', type=str, help='.txt file with links')
parser.add_argument('--fileout', type=str, help='.txt file where output should be saved')
parser.add_argument('--proxies', type=str, help='.txt file with proxies')
args = parser.parse_args()
filein = args.filein
fileout = args.fileout
proxies = open(args.proxies, 'r').readlines()


async def main():
	async with aiofiles.open(filein, mode='r') as links:
		async for link in links:
			if validators.url(link):
				proxy = random.choice(proxies)
				print(Panel.fit(f"Использую прокси: {proxy}"))
				await checker(link, fileout, proxy)
			else:
				print(Panel.fit(f"[red]Ссылка введена неверно: {link}[/]"))


if __name__ == "__main__":
	asyncio.run(main())
