import itertools
import os
import string
import asyncio

import aiofiles
from rich import print
from rich.panel import Panel


async def dmf_generate():
	print(Panel.fit("[green]Генерирую ссылки. Вывод: dmf_links.txt[/]"))
	generatedlinks=0
	async with aiofiles.open('dmf_links.txt', 'a+') as f:
		for word in itertools.product(string.ascii_letters + string.digits, repeat=5):
			if 'https://dropmefiles.com/' + ''.join(word) + '\n' not in await f.readlines():
				await f.write('https://dropmefiles.com/' + ''.join(word) + '\n')
				generatedlinks += 1
				print(f"Сгенерировано ссылок: {generatedlinks}")
			os.system('cls')


async def yd_generate():
	print(Panel.fit("[green]Генерирую ссылки. Вывод: yd_links.txt[/]"))
	generatedlinks = 0
	async with aiofiles.open('yd_links.txt', 'a+') as f:
		for word in itertools.product(string.ascii_letters + string.digits, repeat=14):
			if 'https://disk.yandex.ru/d/' + ''.join(word) + '\n' not in await f.readlines():
				await f.write('https://disk.yandex.ru/d/' + ''.join(word) + '\n')
				generatedlinks += 1
				print(f"Сгенерировано ссылок: {generatedlinks}")
			os.system('cls')
