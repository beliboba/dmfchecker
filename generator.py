import itertools
import os
import string
import asyncio

import aiofiles
from rich import print
from rich.panel import Panel


async def generate():
	print(Panel.fit("[green]Генерирую ссылки. Вывод: links.txt[/]"))
	generatedlinks=0
	async with aiofiles.open('links.txt', 'a+') as f:
		for word in itertools.product(string.ascii_letters, repeat=5):
			if 'https://dropmefiles.com/' + ''.join(word) + '\n' not in await f.readlines():
				await f.write('https://dropmefiles.com/' + ''.join(word) + '\n')
				generatedlinks += 1
			else:
				pass
			print(f"Сгенерировано ссылок: {generatedlinks}")
			os.system('cls')


asyncio.run(generate())
