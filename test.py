import time
import pyotp
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

chrome_options = Options()
# chrome_options.headless = True
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

webdriver_service = Service("/usr/bin/chromedriver")

browser = webdriver.Chrome(service=webdriver_service, options=chrome_options)

#browser to automate

browser.get(
    "https://datastudio.google.com/u/0/reporting/d1ce7463-c6b3-4358-befe-8cdf8826c369/page/gto4B"
)

browser.maximize_window() # to maximize the window
time.sleep(4) # wait for 4sec after maximizing the browser
print('browser-get')

username = browser.find_element(By.XPATH, "//input[@type='email']") # to select input field
username.send_keys('sunny.shah@cloudfactory.com')
time.sleep(2)
user_next = browser.find_element(By.XPATH, "//span[.='अर्को']")
user_next.click()
print('entered-email')
time.sleep(2)

password = browser.find_element(By.XPATH, "//input[@type='password']")
password.send_keys('Htc1x@619619')
time.sleep(2)
password_next = browser.find_element(By.XPATH, "//span[.='अर्को']")
password_next.click()
print('entered-password')
time.sleep(5)
browser.find_element(By.XPATH, "//span[.='अर्को तरिकाले प्रयास गर्नुहोस्']").click()
time.sleep(4)
browser.find_element(By.XPATH, "//strong[.='Google प्रमाणक']").click()
time.sleep(2)
print('from-google-authenticator')
# to generate token
gcode = 'xartjv3upgvjgio4fm2zy45ojq5wdxeg'
totp1 = pyotp.TOTP(gcode)
token_account = totp1.now()
print(token_account)
browser.find_element(By.XPATH, "//input[@type='tel']").send_keys(token_account)
time.sleep(1)
browser.find_element(By.XPATH, "//span[@jsname='V67aGc' and .='अर्को']").click()
time.sleep(30)
print(browser.title)
print('token-generated')
action = ActionChains(browser)

move_cursor = browser.find_element(By.XPATH, "//div[@title='Email' and @class='colName']")
action.move_to_element(move_cursor).perform()
print('success')
# move_to_element_chrome(browser, move_cursor)
time.sleep(3)

move_to_icon = browser.find_element(By.XPATH, "(//div[@class='chart-menu-button header-menu-button' and @aria-label='More'])[3]")
move_to_icon.click()
time.sleep(2)

click_export = browser.find_element(By.XPATH, "//button[.=' Export ']")
click_export.click()
time.sleep(1)

click_export_to_csv = browser.find_element(By.XPATH, "//span[.=' Export ']")
click_export_to_csv.click()

time.sleep(10)
browser.quit()
