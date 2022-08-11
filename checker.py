import aiofiles
from rich import print
from rich.panel import Panel

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.headless = True
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


async def checker(url: str, fileout: str):
	print(Panel.fit(f"[blue]Проверяю ссылку {url}[/]"))
	driver.get(url)
	try:
		driver.find_element(By.XPATH, '//*[@id="filelist"]/noindex/a')
		print(Panel.fit(f"[green]Валидная ссылка: {url}[/]"))
		async with aiofiles.open(fileout, 'a') as fileout:
			await fileout.write(f"Валидная ссылка: {url}")
	except NoSuchElementException:
		print(Panel.fit(f"[red]Невалидная ссылка: {url}[/]"))
		async with aiofiles.open(fileout, 'a') as fileout:
			await fileout.write(f"Невалидная ссылка: {url}")
