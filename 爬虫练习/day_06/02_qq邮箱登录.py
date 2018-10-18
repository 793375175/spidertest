from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://mail.qq.com/')

driver.switch_to.frame('login_frame')

driver.find_element_by_id('u').send_keys('793375175@qq.com')
driver.find_element_by_id('p').send_keys('xxx')

driver.find_element_by_id('login_button').click()

time.sleep(13)
driver.quit()