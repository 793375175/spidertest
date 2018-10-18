from selenium import webdriver
import requests
import yudama
import time

driver = webdriver.Chrome()
driver.get('http://renren.com/')

# 输入用户
driver.find_element_by_id('email').send_keys('15565280933')
# 输入密码
driver.find_element_by_id('password').send_keys('a123456')

# 获取验证图片的URL

# 人人网只有输入账号, 等一会才会出现验证码
time.sleep(1)
# 如果验证码区是显示的
# 人人网登录时是通过id为codeimg的div来控制验证区域示范显示的
# 只有验证码区域显示出来了, 我们才需要处理验证码
if driver.find_element_by_id('codeimg').is_displayed():
    # 获取验证码图片的URL
    img_url = driver.find_element_by_id('verifyPic_login').get_attribute('src')
    # 获取浏览器的cookies信息, 转换为一个字典
    cookies = {cookie['name']:cookie['value'] for cookie in driver.get_cookies()}
    # 发送请求, 获取验证码图片数据codeimg
    response = requests.get(img_url, cookies=cookies)
    # 识别验证码
    code = yudama.indetify(response.content)
    print(code)
    # 找到验证码输入框, 输入验证码
    driver.find_element_by_id('icode').send_keys(code)

# 点击登录按钮
driver.find_element_by_id('login').click()

time.sleep(2)
driver.quit()

# 设置超时
driver.implicitly_wait(30)