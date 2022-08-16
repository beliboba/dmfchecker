import aiofiles
from rich import print
from rich.panel import Panel

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager

from urllib.parse import urlencode
import aiohttp

options = Options()
options.headless = True
prefs = {"download.default_directory": "."}
options.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


async def dmfchecker(url: str, fileout: str, proxy: str, download: bool):
	print(Panel.fit(f"[blue]Проверяю ссылку {url}[/]"))
	options.add_argument(f'--proxy-server={proxy}')
	driver.get(url)
	try:
		element = driver.find_element(By.XPATH, "//*[@id='filelist']/noindex/a")
		print(Panel.fit(f"[green]Валидная ссылка: {url}[/]"))
		async with aiofiles.open(fileout, 'a') as fileout:
			await fileout.write(f"Валидная ссылка: {url}")
		if download:
			element.click()
	except NoSuchElementException:
		print(Panel.fit(f"[red]Невалидная ссылка: {url}[/]"))
	driver.close()


async def ydchecker(url: str, fileout: str, proxy: str, download: bool):
	print(Panel.fit(f"[blue]Проверяю ссылку {url}[/]"))
	options.add_argument(f'--proxy-server={proxy}')
	driver.get(url)
	try:
		element = driver.find_element(By.XPATH, "'//*[@id='app']/div/div/div/div[1]/div[2]/div[2]/button[2]'")
		print(Panel.fit(f"[green]Валидная ссылка: {url}[/]"))
		async with aiofiles.open(fileout, 'a') as fileout:
			await fileout.write(f"Валидная ссылка: {url}")
		if download:
			element.click()
	except NoSuchElementException:
		print(Panel.fit(f"[red]Невалидная ссылка: {url}[/]"))
	driver.close()


