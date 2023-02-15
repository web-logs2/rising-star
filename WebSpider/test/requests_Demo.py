import requests

'''
=============请求===============
'''
# response = requests.get('http://httpbin.org/get')  # get\post\put\head等等方法
# print(type(response.status_code), response.status_code)
# print(type(response.headers), response.headers)
# print(type(response.cookies), response.cookies)
# print(type(response.history), response.history)
# print(type(response.text), response.text)

# response = requests.get('http://httpbin.org/get', params={'姓名': '张三', '年龄': 12})  # 自动将字典转为?k=v&k=v拼接 如果是post则转为表单
# print(response.text)
# print(response.json())  # 因为返回结果是json格式，所以可以直接解析json转为字典类型，注意如果返回结果不是json格式会报错

# response = requests.get('https://zhihu.com/explore',
#                         headers={
#                             'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Chrome/105.0.0.0 Safari/537.36',
#                         })  # 指定请求头
# 部分网站不传headers
# 如上，不止有headers、params，还有很多参数选填,比如file(上传文件)、verify(是否检查SSL证书)、proxies(设置代理)、cookies(传入自定义的RequestCookieJar对象)、timeout(等待响应的超时时间)等等

# 通过请求获取图片
# response = requests.get("https://github.com/favicon.ico")
# print(response.text)  # 图片转字符串肯定乱码
# print(response.content)  # 返回二进制形式(bytes类型)
# with open('github.ico', 'wb') as result:
#     result.write(response.content)

# 通过请求上传文件
# response = requests.post('http://httpbin.org/post',
#                          files={
#                              'file': open('github.ico', 'rb')
#                          })
# print(response.text)

# 携带cookie(在网页上登陆，然后复制cookie，请求时携带上)
# response = requests.get('https://www.zhihu.com', headers={
#     'Cookie': '_zap=eeb5fd9c-c8de-4b99-9081-ebd3329f609c; _xsrf=a8a536ed-6890-4f17-81c8-34adedd3a8df; d_c0=ADCW-FjkkhWPTpXUHsw59bM4qs6ZURt5ClM=|1663415006; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1663415007; _9755xjdesxxd_=32; YD00517437729195%3AWM_NI=LVQAWV7XZPJRWM%2BnWXkoFjNVcNx62xTP%2BXo6nc9NsxOyjdGdMrYFiYVQQIJFDj2aclqmNrd%2BtD0CfLU26MpLndhycPqPovfb6Y5cCiS6nzuTzjgqwDzFutj4V5Pe29uSc2Y%3D; YD00517437729195%3AWM_NIKE=9ca17ae2e6ffcda170e2e6eedad06083a884d7cb2197ac8aa3d54f939f8fb0d444af89ababc873a6a6fab4d52af0fea7c3b92a908a9fa2d65ef58896b1c95a9593e58fd654a9b18a8bcd5ea192b8d7b1749890e5b9ee3eaebdf7aff2748da7a685c6708fae97a7ec53968f9faac94e88b6fe82e268b3b38293e721b89c00a4e54897eefaaef348aebca89ae25cb390a197e56af687fb84c26391eaa29bf860bab6a992f650ba9abb95e94096eba086b133b78dadd3dc37e2a3; YD00517437729195%3AWM_TID=wDDVvxcDiH5FBEBRVFOETjDfYUiemuHU; __snaker__id=P0g27XgPBroegh6u; gdxidpyhxdE=KcWl6wWmqvaC9egpiu1ebt%2F014AR7Ki7CLc3pXk2bSJYmCRPs4fQs0KbgfkD76oinTWjxYgYuJS8S2a%2BoZr23yZHx5WMrLjq8eANIX%2F6zfPnCILBm86fl4Jll%2FisEsChPoJG49%5C804a9v9zVktOrxx5r6mw%5CBj3%5CGNoGvlWHQ%5Cm1ZrC7%3A1663416967980; q_c1=e1924c3a75c14e9691688771f4179f68|1663416275000|1663416275000; NOT_UNREGISTER_WAITING=1; captcha_session_v2=2|1:0|10:1663416664|18:captcha_session_v2|88:OXFlU0RmU2RUNzNUTExSR2trbndKZ0xlL1FiTG1raURmdVlyZldUbnROWUJKQ09vVHF0K3lQTWVTcEhGelppUQ==|256596888c3d9ea4958b1bc389f32a7547b2c4431db5669f486c3a834d70a32b; SESSIONID=1WQaTMzXAzz1fY6LhHMiBKF2G35tjt1haLulfAFayRU; JOID=W18dBU-WQ89OKfHsRJlAnap8Gn1QqRuQLXCymRLaN7pxTaXUB8_75iIq8O1IJkceYA7WUvwCPsADcAOwbeflfXI=; osd=V1wTC0yaQMFAKv3vSpdDkalyFH5cqhWeLnyxlxzZO7l_Q6bYBMH15S4p_uNLKkQQbg3aUfIMPcwAfg2zYeTrc3E=; z_c0=2|1:0|10:1663416697|4:z_c0|92:Mi4xcU83cUdnQUFBQUFBTUpiNFdPU1NGU1lBQUFCZ0FsVk5lUWNUWkFBYU0zWURJOXR6NGd5TllBX2VPRzRQOFlQVzNB|46aae761f28f1f9543bb93512bd0a64471892b0b3979df9e29d88f20bfbcbc6d; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1663416698; KLBRSID=e42bab774ac0012482937540873c03cf|1663416757|1663415006',
#     'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'})
# print(response.text)
# 可以看到，当网页上没有登陆时，这里第一次请求知乎时返回的是登陆页面的html，网页上登陆后，复制cookie并携带上再次请求时可以返回首页的html，当网页上点击退出登陆，cookie被清理，再请求又变为登陆
# 除了在headers中直接配置cookie外，也可以构造RequestCookieJar(requests.cookies下)对象自己配置，然后get方法中直接传入即可(和url、headers同级)

# session会话
# requests.get('http://httpbin.org/cookies/set/number/12323')  # 设置cookie
# response = requests.get('http://httpbin.org/cookies')  # 取当前cookie
# print(response.text)  # 取不到，因为每次请求都是新的会话，而不是接着上次，所以使用session
# 换session尝试
# session = requests.Session()
# session.get('http://httpbin.org/cookies/set/number/12323')
# response = session.get('http://httpbin.org/cookies')
# print(response.text)


# 身份验证
# response = requests.get('xxx', auth=('username', 'password'))  # 懒得找要验证的网站
# print(response.status_code)

# 灵活构造请求对象，类似于urllib中的构造Request方式
# Request = requests.Request('POST',
#                            url='http://httpbin.org/post',
#                            headers={
#                                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Chrome/105.0.0.0 Safari/537.36'},
#                            data={
#                                'name': 'Ben'}
#                            )
# session = requests.Session()
# prepped = session.prepare_request(Request)
# response = session.send(prepped)
# print(response.text)
