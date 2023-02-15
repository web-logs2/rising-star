import re

word = 'Hello 123 4567 World_This is a Regex Demo'
# 基础用法
# result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}', word)
# print(result)
# print(result.group())  # 取匹配到内容
# print(result.span())  # 匹配结果在原字符串中的范围
# 如果匹配要 . * 等字符，可以转义，如\. \* \( \)等

# 取指定部分
# result = re.match('^Hello\s\d+\s\d{4}\s\w{10}', word)
# print(result.group())  # 无法直接取到123
# result1 = re.match('^Hello\s(\d+)\s\d{4}\s\w{10}', word)
# print(result1.group(1))  # 无参是取所有，指定参数就对应第几个()中的内容，依次类推(这里传2会报错，因为没有第二个)

# 贪婪与非贪婪
# word1 = 'Hello 1234567 World_This is a Regex Demo'
# .匹配任意字符(除换行) *不限次
# 贪婪
# result1 = re.match('^H.*(\d+).*Demo$', word1)
# print(result1.group(1))  # .*会尽可能多的匹配，\d+是至少一个数字，也没有指定多少个，所以.*留了一个7给\d+导致结果为7
# 非贪婪
# result2 = re.match('^H.*?(\d+).*Demo$', word1)
# print(result2.group(1))  # .*?会尽可能少的匹配，\d+可以匹配1234567，所以交给\d+匹配，自己匹配H到1之间的
# 为了结果准确，养成使用非贪婪的习惯，但是注意，如果匹配的内容在字符串结尾，非贪婪可能匹配不到，因为?是0个或1个，它要尽量少的匹配
# print(re.match('http.*?comment/(.*?)', 'http://weibo.com/comment/kEraCN').group())  # 这里.*?和.*效果一样，但养成好习惯
# print(re.match('http.*?comment/(.*)', 'http://weibo.com/comment/kEraCN').group())

# 修饰符
# word1 = '''Hello 1234567 World_This
# is a Regex Demo'''
# print(re.match('^H.*(\d+).*Demo$', word1).group())  # 报错是因为match完是None，None.get会报错。而为None是因为.不匹配换行符所以没结果
# print(re.match('^H.*(\d+).*Demo$', word1, re.S).group())  # re.S是让.匹配所有字符包括换行
# 类似还有re.I(使匹配对大小写不敏感)、re.M(多行匹配，影响^和$)等等


# match会是从头开始匹配，如果一开始匹配不上那肯定就没结果 所以这里介绍search()
# print(re.match('llo.*?Demo$', word))  # 开头就匹配不上，一定是None
# print(re.search('llo.*?Demo$', word).group())  # 返回匹配到的第一个结果，可以匹配部分而不是全部

# 如下练习
html = '''<div id="songs-list">
<h2 class="title">经典老歌</h2>
<p class="introduction">
经典老歌列表
</p>
<ul id="list" class="list-group">
<li data-view="2">一路上有你</li>
<li data-view="7">
<a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
</li>
<li data-view="4" class="active">
<a href="/3.mp3" singer="齐秦">往事随风</a>
</li>
<li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
<li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
<li data-view="5">
<a href="/6.mp3" singer="邓丽君">但愿人长久</a>
</li>
</ul>
</div>'''
# result = re.search('<li.*?active.*?singer="(.*?)">(.*?)</a>', html, re.S)  # 筛选active类中的歌手和歌名
# if result:
#     print(result.group(1), result.group(2))  # 不为None则输出
#
# result = re.search('<li.*?singer="(.*?)">(.*?)</a>', html, re.S)  # 去掉active就返回第一个匹配到的结果
# if result:
#     print(result.group(1), result.group(2))
#
# result = re.search('<li.*?singer="(.*?)">(.*?)</a>', html)  # 不加re.S的话.就不匹配换行符  符合条件的只有 beyond光辉岁月
# if result:
#     print(result.group(1), result.group(2))  # 所以匹配html时，最好都加上re.S避免丢数据或出现异常

# 全部匹配
# results = re.findall('<li.*?href="(.*?)".*?singer="(.*?)">(.*?)</a>', html, re.S)  # 返回所有匹配项，返回值类型为list
# print(results)  # 三个()，所有list的每个元素是三元组
# print(type(results))
# for result in results:
#     print(result[0], result[1], result[2])

# results = re.findall('<li.*?>\s*?(<a.*?>)?(\w+)(</a>)?\s*?</li>', html, re.S)  # 针对每个<li></li>标签筛选歌名，注意非贪婪，否则从第一个<li匹配到最后一个>
# for result in results:
#     print(result[1])

# 正则替换 sub()
# content = '54aK54yr5oiR54ix5L2g'
# content_new1 = re.sub('\d+', '--', content)  # 匹配到的替换为第二个参数
# content_new2 = re.sub('[a-zA-Z]', '', content)  # 匹配到的替换为第二个参数
# content_new3 = re.sub('', ' ', content)  # 匹配到的替换为第二个参数
# print(content_new1)
# print(content_new2)
# print(content_new3)

# 更简单的方式取所有歌名
# html = re.sub('<a.*?>|</a>', '', html)
# print(html)
# results = re.findall('<li.*?>(.*?)</li>', html, re.S)
# for result in results:
#     print(result.strip())  # 首尾去空格或换行

# html = re.sub('[^\u4e00-\u9fa5\n]', '', html)  # 除中文和换行外，全部替换为空
# print([i for i in html.split('\n') if i != ''])  # 丢了beyond


# 将正则封装成对象复用
# pattern = re.compile('^H.*?(\d+).*Demo$', re.S)  # 就是把正则封装成对象，用法还是一样，在这里指定了re.S,之后方法调用就不必再设置了
# print(re.match(pattern, word).group(1))

