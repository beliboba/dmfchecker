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
args = parser.parse_args()
filein = args.filein
fileout = args.fileout


async def main():
	async with aiofiles.open(filein, mode='r') as links:
		async for link in links:
			if validators.url(link):
				await checker(link, fileout)
			else:
				print(Panel.fit(f"[red]Ссылка введена неверно: {link}[/]"))


if __name__ == "__main__":
	asyncio.run(main())
