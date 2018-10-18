import yudama
from selenium import webdriver
import time, requests


# 创建驱动
driver = webdriver.Chrome()
driver.get('https://www.douban.com/')

driver.find_element_by_id('form_email').send_keys('583349285@qq.com')
driver.find_element_by_id('form_password').send_keys('ivan1986')

# 识别豆瓣登录的验证码
# URL对应图片内容是不发生改变, 我们之间获取图片的URL, 发送请求图片数据, 进行识别就可以了
images = driver.find_elements_by_id('captcha_image')
if len(images) != 0:
    # 如果有验证码就识别验证码
    img_url = images[0].get_attribute('src')
    # 发送请求, 获取图片数据
    response = requests.get(img_url)
    # 识别图片
    code = yudama.indetify(response.content)
    print(code)
    driver.find_element_by_id('captcha_field').send_keys(code)

# 点击登录
driver.find_element_by_class_name('bn-submit').click()

time.sleep(10)
driver.quit()