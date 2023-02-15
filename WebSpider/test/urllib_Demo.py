from urllib import request, parse, error

"""
===================请求==================
"""
# 简单的基础请求，无法自定义请求头信息
# response = request.urlopen('http://httpbin.org/post', data=bytes(parse.urlencode({'姓名': '张三'}), encoding='utf-8'))
# print(response.read().decode('utf8'))
# url必填，其余选填，不填有默认值  data-表单数据  timeout-超时时间  cafile-CA证书  capath-证书路径  cadefault-被废弃  context-SSL相关设置
# data是bytes类型,parse的urlencode可以将字典转为str，然后手动再用bytes方法将str转bytes并指定编码    如果传了data参数，请求方式会变为post，否则get

# 使用Request对象请求，可以设置请求头
# myRequest = request.Request('http://httpbin.org/post',
#                             data=bytes(parse.urlencode({'姓名': '张三'}), encoding='utf-8'),
#                             # headers={
#                             #     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Chrome/105.0.0.0 Safari/537.36',
#                             #     'Host': 'httpbin.org'},
#                             method='POST')
# url(必填，其他选填)和data同上
# headers-请求头，字典类型   常用User-Agent，这是客户端的设备信息，我们一般选择伪装成浏览器
# origin_req_host-请求方的host或ip地址,不设置默认None
# unverifiable-请求是否不可验证，true为不可，代表用户没有权限接收此请求的结果或资源 默认为false代表可以接收
# method 请求方式,必须大写
# response1 = request.urlopen(myRequest)
# print(response1.read().decode('utf8'))

# 高阶用法
# urllib对于cookies处理、代理设置、异常处理等不如requests简洁，不详细介绍，简单指引如下，更推荐直接用requests
# urllib.request中的BaseHandler是所有Handler的父类，它的子类例举如下部分
#   HTTPDefaultErrorHandler:用于处理http错误  HTTPRedirectHandler:处理重定向  HTTPCookieProcessor:处理Cookies
#   ProxyHandler:处理代理 HTTPPasswordMgr:管理密码 HTTPBasicAuthHandler:管理认证
# 另一个重要的类OpenerDirector,简称Opener，之前的简单urlopen方法和自定义的Request对象都是类库已经封装好的常用Opener请求方式，而现在需要更底层的方式自定义功能
# 简而言之，要利用Handler来构建Opener来自定义更多功能，具体代码太多 省略
# urllib.error中有各种异常类型，如URLError、HTTPError(处理状态玛)等，可以捕获并取得额外信息

"""
==================解析==================
"""
# 网址的组成：scheme://netloc/path;params?query#fragment

# urlparse = parse.urlparse('http://www.baidu.com/index.html;user?id=5#comment', scheme='https')  # 解析指定网址的结构
# url必填  scheme-协议类型(如果url中已经写明协议，则这个参数的设置不生效)   allow_fragments-是否允许fragment,为false则忽略，默认是true
# print(urlparse)  # url中没有写scheme时，参数scheme才生效

# urlunparse = parse.urlunparse(
#     ['https', 'www.baidu.com', 'index.html', 'user', 'a=6', 'comment'])  # 结构转网址  参数必须是sequence（序列），如列表、元祖  长度必须是6个
# print(urlunparse)

# urlsplit()和urlparse() 一摸一样，只不过没有单独params这一结构，会拼在path里面  urlunsplit()也一样，只能传长度为5的序列，没有params这一结构
# 还有urljoin、urlencode、parse_qs、parse_qsl、quote、unquote等等方法 不一一演示

