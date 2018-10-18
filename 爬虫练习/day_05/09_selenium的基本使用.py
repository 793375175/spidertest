from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options


options = Options()
options.set_headless()

driver = webdriver.Chrome(options=options)
driver.get('http://www.baidu.com')


driver.find_element_by_id('kw').send_keys("python")
driver.find_element_by_id('su').click()

# print(driver.page_source)

cookies = {cookie['name']: cookie['value'] for cookie in driver.get_cookies()}
print(cookies)

driver.save_screenshot('baidu.png')


time.sleep(3)
driver.quit()