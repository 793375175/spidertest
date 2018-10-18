from selenium import webdriver
import time
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get('http://www.baidu.com')

# elements = driver.find_elements_by_xpath('//*[@id="u1"]/a')
# for element in elements:
#     print(element.text)

element = driver.find_element_by_class_name('mnav')
# 根据链接文本查找元素
# element = driver.find_element_by_link_text('地图')
# element = driver.find_element_by_partial_link_text('吧')
# element = driver.find_element_by_tag_name('div')
print(element)
# print(element.tag_name)
# print(element.text)
# print(element.get_attribute('name'))
# driver.find_element(By.NAME, 'wd').send_keys("Python")

time.sleep(3)
driver.quit()