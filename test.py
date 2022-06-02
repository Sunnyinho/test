import time
import pyotp
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from 

chrome_options = Options()
# chrome_options.headless = True
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

webdriver_service = Service(ChromeDriverManager().install())

browser = webdriver.Chrome(service=webdriver_service, options=chrome_options)

#browser to automate

browser.get(
    "https://datastudio.google.com/u/0/reporting/d1ce7463-c6b3-4358-befe-8cdf8826c369/page/gto4B"
)


time.sleep(10)
browser.quit()
