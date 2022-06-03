import time, datetime
import boto3
import pyotp
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from fake_useragent import UserAgent


#locators of fields
locators = {
    "email_field"          : "//input[@type='email']",
    "password_field"       : "//input[@type='password']",
    "try_another_way"      : "//div[@class='FliLIb kDmnNe']//button",
    "google_authenticator" : "//div[@class='vxx8jf']//strong[contains(text(),'Google')]",
    "token_field"          : "//input[@type='tel']"
}

#locators for table to download
table_locators = {
    "table2" : "(//lego-table[@class='table'])[2]"
}

#locators for hamburger/menu icon
more_icon = {
    "more2" : "(//chart-menu-button[@component='$ctrl.component'])[4]"
}

#locators for buttons
buttons = {
    "email_next_button"    : "//div[@id='identifierNext']//button",
    "password_next_button" : "//div[@id='passwordNext']//button",
    "token_next_button"    : "//div[@id='totpNext']//button",
    "more_export"          : "//button[.=' Export ']",
    "download"             : "//span[.=' Export ']"
}

#s3_bucket properties
date_time = datetime.datetime.now()
s3_bucket = {
    "local_path_and_file" : "./Ibotta Report_Page 1_Table.csv",
    "s3_bucket_name"      : "cfsnowflakestage-dev",
    "s3_bucket_path"      : f"prefect/data_studio/Ibotta/{date_time.year}/{date_time.month}/{date_time.day}/Ibotta Report_Page 1_Table-{date_time.replace(microsecond=0)}.csv"
}

url = "https://datastudio.google.com/u/0/reporting/d1ce7463-c6b3-4358-befe-8cdf8826c369/page/gto4B" #site to visit
webdriver_service = Service(ChromeDriverManager(version="latest").install()) #driver path

#define properties of browser
def get_Browser():
    chrome_options = Options()
    ua = UserAgent()
    userAgent = ua.chrome
    print(userAgent)
    chrome_options.add_argument(f'user-agent={userAgent}')
    chrome_options.headless = True
    browser = webdriver.Chrome(service=webdriver_service, options=chrome_options)
    browser.get(url)
    time.sleep(3)
    browser.set_window_size(800,700)
    print("browser-get")
    browser.quit()
    return browser

get_Browser()
