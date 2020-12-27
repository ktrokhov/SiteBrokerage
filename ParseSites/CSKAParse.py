import time
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from webdriver_manager.chrome import ChromeDriverManager


i = 0
while i < 5000:
    CSKASite = "https://pfc-cska.com/fans/oprosy/5280/"
    browser = webdriver.Chrome('/Users/kirilltrokhov/PycharmProjects/SiteBrokerage/ParseSites/chromedriver')
    browser.get(CSKASite)
    element = browser.find_element_by_id('173058')
    browser.execute_script("arguments[0].click();", element)
    browser.find_element_by_css_selector('button.vote__btn').click()
    browser.close()
    i = i + 1
    print(i)

# for i in range(500):
#     try:
#         webdriver = webdriver.Firefox(executable_path=r'C:\Utility\BrowserDrivers\geckodriver.exe')
#         print("WebDriver and WebBrowser initialized ...")
#         break
#     except WebDriverException:
#         #Cross platform
#         PROCNAME = "geckodriver"
#         for proc in psutil.process_iter():
#             # check whether the process name matches
#             if proc.name() == PROCNAME:
#                 proc.kill()
#         print("Retrying ...")