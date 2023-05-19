# 赋值
counter = 100  # 整型变量
miles = 1000.0  # 浮点型变量
name = "runoob"  # 字符串

print(counter)
print(miles)
print(name)

# 多个变量赋值
a1 = b1 = c1 = 1
a2, b2, c2 = 1, 2, "runoob"

# 标准数据类型
# Number（数字）
a3, b3, c3, d3 = 20, 5.5, True, 4 + 3j
print(type(a3), type(b3), type(c3), type(d3))
print(isinstance(a3, int))
# isinstance()会认为子类是一种父类类型。type()不会
# Python3 中，bool 是 int 的子类，True 和 False 可以和数字相加， True==1、False==0 会返回 True，但可以通过 is 来判断类型
print(issubclass(bool, int))

# 数值运算
# 5 + 4  # 加法
# 4.3 - 2  # 减法
# 3 * 7  # 乘法
# 2 / 4  # 除法，得到一个浮点数
# 2 // 4  # 除法，得到一个整数
# 17 % 3  # 取余
# 2 ** 5  # 乘方

# 字符串
# str = 'Runoob'
#
# print (str)          # 输出字符串
# print (str[0:-1])    # 输出第一个到倒数第二个的所有字符
# print (str[0])       # 输出字符串第一个字符
# print (str[2:5])     # 输出从第三个开始到第五个的字符
# print (str[2:])      # 输出从第三个开始的后的所有字符
# print (str * 2)      # 输出字符串两次，也可以写成 print (2 * str)
# print (str + "TEST") # 连接字符串

print('Ru\noob')
'''
Ru
oob
'''
print(r'Ru\noob')
'''
Ru\noob
'''

# 布尔类型
# a = True
# b = False
#
# # 比较运算符
# print(2 < 3)   # True
# print(2 == 3)  # False
#
# # 逻辑运算符
# print(a and b)  # False
# print(a or b)   # True
# print(not a)    # False
#
# # 类型转换
# print(int(a))   # 1
# print(float(b)) # 0.0
# print(str(a))   # "True"

# List（列表）
# list = [ 'abcd', 786 , 2.23, 'runoob', 70.2 ]
# tinylist = [123, 'runoob']
#
# print (list)            # 输出完整列表
# print (list[0])         # 输出列表第一个元素
# print (list[1:3])       # 从第二个开始输出到第三个元素
# print (list[2:])        # 输出从第三个元素开始的所有元素
# print (tinylist * 2)    # 输出两次列表
# print (list + tinylist) # 连接列表

# Tuple（元组）
# tuple = ( 'abcd', 786 , 2.23, 'runoob', 70.2  )
# tinytuple = (123, 'runoob')
#
# print (tuple)             # 输出完整元组
# print (tuple[0])          # 输出元组的第一个元素
# print (tuple[1:3])        # 输出从第二个元素开始到第三个元素
# print (tuple[2:])         # 输出从第三个元素开始的所有元素
# print (tinytuple * 2)     # 输出两次元组
# print (tuple + tinytuple) # 连接元组

# Set（集合）
# sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu'}
#
# print(sites)   # 输出集合，重复的元素被自动去掉
#
# # 成员测试
# if 'Runoob' in sites :
#     print('Runoob 在集合中')
# else :
#     print('Runoob 不在集合中')
#
#
# # set可以进行集合运算
# a = set('abracadabra')
# b = set('alacazam')
#
# print(a)
# print(a - b)     # a 和 b 的差集
# print(a | b)     # a 和 b 的并集
# print(a & b)     # a 和 b 的交集
# print(a ^ b)     # a 和 b 中不同时存在的元素
# 注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。


# Dictionary（字典）
# dict = {}
# dict['one'] = "1 - 菜鸟教程"
# dict[2]     = "2 - 菜鸟工具"
#
# tinydict = {'name': 'runoob','code':1, 'site': 'www.runoob.com'}
#
#
# print (dict['one'])       # 输出键为 'one' 的值
# print (dict[2])           # 输出键为 2 的值
# print (tinydict)          # 输出完整的字典
# print (tinydict.keys())   # 输出所有键
# print (tinydict.values()) # 输出所有值

# bytes 类型
x0 = bytes("hello", encoding="utf-8")
x = b"hello"
y = x[1:3]  # 切片操作，得到 b"el"
z = x + b"world"  # 拼接操作，得到 b"helloworld"

# 需要注意的是，bytes 类型中的元素是整数值，因此在进行比较操作时需要使用相应的整数值。例如：
x = b"hello"
if x[0] == ord("h"):
    print("The first element is 'h'")