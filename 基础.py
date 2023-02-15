#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    交互式编程：命令行交互
    脚本式编程：新建文件后写代码   指定用python执行：python 文件
              如果在文件顶部声明：   #! /usr/bin/env python3    则可以像shell脚本一样直接 ./ 执行，会自己识别执行器为python
    另外：第二行时告诉Python解释器，按照UTF-8编码读取源代码(不写也默认用utf，所以可以换别的编码方式)，申明了UTF-8编码并不意味着你的.py文件就是UTF-8编码的，必须并且要确保文本编辑器正在使用UTF-8 without BOM编码
    如果.py文件本身使用UTF-8编码，并且也申明了# -*- coding: utf-8 -*-，打开命令提示符测试就可以正常显示中文
"""

""" （多行注释用三个双引号或者三个单引号都行）
数字类型：int （python3中没有Long）
        bool
        float
        complex (复数), 如 1 + 2j、 1.1 + 2.2j
字符串类型：String  没有单独的字符char类型，一个字符就是长度为 1 的字符串
元组类型：Tuple 元祖中元素的类型可以不同（相当于java的数组，不过不限制元素类型的一致性） tuple的元素不可改变，但它可以包含可变的对象，比如list列表
-----------上三个是不可变类型，下三个是可变类型----------
列表类型：List  列表中元素的类型可以不同
集合类型：Set   自动去重
字典类型：Dictionary   键必须是唯一的(重复不会报错但只有后面的被记住，所以严格上不许重复)，但值则不必。值可以取任何数据类型，但键必须是不可变的，如字符串，数字

string tuple list都属于sequence（序列），有索引概念，所以有下标
"""
a = 1  # 可以多变量赋值 a = b = c = 1   也可以  a, b, c = 1, 2, "hello"
b = True  # T必须大写 bool是int的子类，所以能和数字相加，True是1，False是0  True==1的返回值是true，想严格比较可以通过is来判断  1 is True返回false
#          is 用于判断两个变量引用对象是否为同一个， == 用于判断引用变量的值是否相等
c = 1.22
d = 1 + 2j
e = '苹果'  # 单引号 ' 和双引号 " 的使用完全相同
f = """香蕉 菠萝
桃子 芒果"""  # 使用三引号(''' 或 """)可以指定一个多行字符串  当然若不接收为变量就相当于多行注释
g = """这是一个多行字符串的实例
多行字符串可以使用制表符
TAB ( \t )。
也可以使用换行符 [ \n ]。 
"""  # 三引号让程序员从引号和特殊字符串的泥潭里面解脱出来，自始至终保持一小块字符串的格式是所谓的 所见即所得 格式
h = r"hello \n python"  # 使用 r 可以让反斜杠不发生转义
print(f[4:7])  # 换行（\n）被当作一个字符   [n:m]遵循前闭后开   print默认是换行输出，不想换行可以指定end print("aaa", end="")
# h = input("来来来，给个数:")  # 接收输入，得到一定是str类型，若是数字 需要再转类型
print(type(chr(97)))  # chr方法按阿斯克码将数字转成str类型  python3中没有char类型
print("我叫%s，今年%d岁" % ('小明', 10))  # 占位符
print(f"我的得分是{c * 100}")  # f-string 格式化字符串以 f 开头，后面跟着字符串，字符串中的表达式用大括号 {} 包起来，它会识别变量、也支持表达式计算后的值替换进去
print(f"{1+1=}")  # 在 Python 3.8 的版本中可以使用 = 符号来 拼接表达式与结果 一同输出

# .format()  # 超级好用的字符串格式化方法！！
print("{} {}".format("hello", "world"))  # 不设置指定位置，按默认顺序
print("{0} {1} {0}".format("hello", "world"))  # 设置指定位置
print("网站名：{name}, 地址 {url}".format(name="菜鸟教程", url="www.runoob.com"))  # 自定义名称
site = {"name": "菜鸟教程", "url": "www.runoob.com"};
print("网站名：{name}, 地址 {url}".format(**site))  # 通过字典设置参数
my_list = ['菜鸟教程', 'www.runoob.com'];
print("网站名：{0[0]}, 地址 {0[1]}".format(my_list))  # 通过列表索引设置参数  注意"0" 是必须的
print("{:.2f}".format(3.1415926))  # 建议参考 https://www.runoob.com/python/att-string-format.html 中的数字格式化
# 字符串有许多实用的内建函数  参考 https://www.runoob.com/python3/python3-string.html 中的string内建函数

"""
类型转换
    隐式类型转换：整形和浮点型混合计算时，较低数据类型（int）会自动转换为较高数据类型（float）以避免数据丢失
    强制类型转换：如，字符强转整形 int("3") 、 浮点强转整形（丢失精度）int(2.8) 、 字符强转浮点 float("4.2") 、 整形浮点型转字符 str(3.0)
"""

# 元组(相当于java数组，不可变，但不要求子元素的类型统一)
tuple = ('abcd', 786, 2.23, 'hello', 70.2)  # tuple只有一个元素时应写为 ('a',)  若不写,会被当作string类型  list类型只有一个元素时不用加,
tuple1 = 'a', 'b'  # 不写() 也行  tuple1也是元组类型
# 列表
list = ['abcd', 786, 2.23]  # 注意：list的append方法是浅拷贝 https://zhuanlan.zhihu.com/p/356195709   list之间可以拼接：list+=[1,2]
# 列表比较需要引入 operator 模块的 eq 方法，https://www.runoob.com/python3/python-operator.html
# 集合(自动去重)
set = {'Google', 'Taobao', 'Facebook', 'Zhihu', 'Baidu'}  # 创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典
# 集合添加元素有add和update两种方法  删除有remove和discard两种方法，pop是随机删一个元素并返回该元素的值  详细的对比见：https://www.runoob.com/python3/python3-set.html
# 字典
tinydict = {'name': 'baidu', 'code': 1, 'site': 'www.baidu.com'}  # 字典中的元素通过键来存取而不是下标 并且键(key)必须是不可变类型且key在字典中必须唯一(key重复不会报错但后者会覆盖前者,所以是唯一)
tinydict['Age'] = 8  # 有这个key就是修改这个key的值，没有就是新增这个kv

"""
推导式：一种独特的数据处理方式，可以用一个数据序列来构建另一个新的数据序列的结构体
列表推导式格式为 [输出的表达式 for 变量 in 任意collection if 条件]   if可有可无
集合推导式格式为 {输出的表达式 for 变量 in 任意collection if 条件}   if可有可无
字典推导式格式为 {输出的k:v for 变量 in 任意collection if 条件}    if可有可无
元组推导式格式为 (输出的表达式 for 变量 in 任意collection if 条件)  if可有可无    注意：元组推导式返回的结果是一个生成器对象
"""
# 过滤掉长度小于或等于3的字符串列表，并将满足条件的转换成大写字母 构建成新的列表
names = ['Bob', 'Tom', 'alice', 'Jerry', 'Wendy', 'Smith']
new_names = [word.upper() for word in names if len(word) > 3]
# 计算 30 以内(含30)可以被 3 整除的整数
result = [num for num in range(31) if num % 3 == 0]
# 99乘法表
result1 = [str(num1) + '*' + str(num2) + '=' + str(num1 * num2) for num1 in range(1, 10) for num2 in
           range(1, 10)]  # 双循环 输出表达式的执行在第二层循环中
# 使用字符串的字面量及其长度创建新字典 （还是用上面的names列表）
new_dict = {word: len(word) for word in names}
# 自己提供三个数字，以三个数字为键，三个数字的平方为值来创建字典
new_dict2 = {num: num ** 2 for num in (2, 4, 6)}
# 将给定字典转换成由一组二元组组成的列表，元组的格式为(key, value)
dic_tolist = [('new_' + k, v) for k, v in tinydict.items()]

"""
生成器
构建生成器(Generator)格式为 (输出的表达式 for 变量 in 任意collection if 条件)   if可有可无   注意返回的是生成器对象
生成器的作用：按照某种算法不断生成新的数据，直到满足某一个指定的条件结束
生成器的特性：只有在调用时才会生成相应的数据，只记录当前的位置，只能next，不能prev
构造生成器的方式：使用推导式生成 (2*n for n in range(3, 11)) 或使用包含yield的函数来生成
生成器的调用方式：调用内置的next()方法、使用循环对生成器对象进行遍历（推荐）等等

迭代器：Iterator对象表示的是一个数据流，Iterator可以被next()函数调用被不断返回下一个数据，直到没有数据可以返回时抛出StopIteration异常错误。
可以把这个数据流看做一个有序序列，但我们无法提前知道这个序列的长度。同时，Iterator的计算是惰性的，只有通过next()函数时才会计算并返回下一个数据，
生成器也是这样的，因为生成器也是迭代器

Iterable、Iterator与Generator之间的关系
生成器对象既是可迭代对象，也是迭代器： 我们已经知道，生成器不但可以作用与for循环，还可以被next()函数不断调用并返回下一个值，直到最后抛出StopIteration错误表示无法继续返回下一个值了。也就是说，生成器同时满足可迭代对象和迭代器的定义；
迭代器对象一定是可迭代对象，反之则不一定： 例如list、dict、str等集合数据类型是可迭代对象，但不是迭代器，但是它们可以通过iter()函数生成一个迭代器对象。
也就是说：迭代器、生成器和可迭代对象都可以用for循环去迭代，生成器和迭代器还可以被next()方函数调用并返回下一个值。
"""
# 一个数字的生成器
generator = (x for x in range(1, 3))
print(type(generator))
# 遍历生成器
print(next(generator))
# print(next(generator))
# print(next(generator))  # 使用next()方法遍历生成器时，最后是以抛出一个StopIeration异常终止 相当于越界 因为生成器中只有1和2
for x in generator:  # 循环遍历  是接着上次的next继续遍历的
    print('---', x)


