from selenium import webdriver
from selenium.webdriver import FirefoxOptions

browser = webdriver.Chrome()
#opts.add_argument("--headless")
#browser = webdriver.ChromeOptions()

print("BROWSER", browser)

browser.get('http://127.0.0.1:8000')

assert 'Django' in browser.title