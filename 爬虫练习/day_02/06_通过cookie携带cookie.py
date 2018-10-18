import requests
url = 'http://www.renren.com/967475625/profile'
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Mobile Safari/537.36'
}
# cookie的字符串
cookies_str = 'anonymid=jkv3vp2d-5hpl25; depovince=GW; _r01_=1; JSESSIONID=abcYL4iEcHsRkfIIKI9uw; ick_login=712a2f26-e22a-4cf9-b6af-373ce3088a38; ick=ec6fc9fd-2bd1-440f-a3df-34619b765835; t=27fa21626fe6ac095775c36d6daddac55; societyguester=27fa21626fe6ac095775c36d6daddac55; id=967475625; xnsid=c273ee06; XNESSESSIONID=c517adb73e0f; WebOnLineNotice_967475625=1; jebe_key=80ceb5c5-4df0-43ed-aed2-6956fd265505%7C437e12ae670f84cf0e8fe68be727c599%7C1534336026607%7C1%7C1534336033552; wp_fold=0; jebecookies=9c437038-a4dc-42d5-a69e-b0c7512cc39a|||||'
# str-->dict
cookies = {cookie_str.split('=')[0]:cookie_str.split('=')[1] for cookie_str in cookies_str.split('; ')}
response = requests.get(url, headers=headers, cookies=cookies)
print(response.content.decode())