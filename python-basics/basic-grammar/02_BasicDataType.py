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
# Number（数字）：整型(int) ，浮点型(float)，复数( (complex))
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
# 2 ** 5  # 幂运算 2的5次方
# 删除 del var
# del var_a, var_b

# Python 数字类型转换
# int(x) 将x转换为一个整数。
# float(x) 将x转换到一个浮点数。
# complex(x) 将x转换到一个复数，实数部分为 x，虚数部分为 0。
# complex(x, y) 将 x 和 y 转换到一个复数，实数部分为 x，虚数部分为 y。x 和 y 是数字表达式。

# 数学函数
"""
abs(x)	返回数字的绝对值，如abs(-10) 返回 10
ceil(x)	返回数字的上入整数，如math.ceil(4.1) 返回 5
cmp(x, y)

如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1。 Python 3 已废弃，使用 (x>y)-(x<y) 替换。
exp(x)	返回e的x次幂(ex),如math.exp(1) 返回2.718281828459045
fabs(x)	以浮点数形式返回数字的绝对值，如math.fabs(-10) 返回10.0
floor(x)	返回数字的下舍整数，如math.floor(4.9)返回 4
log(x)	如math.log(math.e)返回1.0,math.log(100,10)返回2.0
log10(x)	返回以10为基数的x的对数，如math.log10(100)返回 2.0
max(x1, x2,...)	返回给定参数的最大值，参数可以为序列。
min(x1, x2,...)	返回给定参数的最小值，参数可以为序列。
modf(x)	返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示。
pow(x, y)	x**y 运算后的值。
round(x [,n])	返回浮点数 x 的四舍五入值，如给出 n 值，则代表舍入到小数点后的位数。其实准确的说是保留值将保留到离上一位更近的一端。
sqrt(x)	返回数字x的平方根。
"""

# 随机数函数
"""
choice(seq)	从序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑选一个整数。
randrange ([start,] stop [,step])	从指定范围内，按指定基数递增的集合中获取一个随机数，基数默认值为 1
random()	随机生成下一个实数，它在[0,1)范围内。
seed([x])	改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed。
shuffle(lst)	将序列的所有元素随机排序
uniform(x, y)	随机生成下一个实数，它在[x,y]范围内。
"""

# 三角函数
"""
acos(x)	返回x的反余弦弧度值。
asin(x)	返回x的反正弦弧度值。
atan(x)	返回x的反正切弧度值。
atan2(y, x)	返回给定的 X 及 Y 坐标值的反正切值。
cos(x)	返回x的弧度的余弦值。
hypot(x, y)	返回欧几里德范数 sqrt(x*x + y*y)。
sin(x)	返回的x弧度的正弦值。
tan(x)	返回x弧度的正切值。
degrees(x)	将弧度转换为角度,如degrees(math.pi/2) ， 返回90.0
radians(x)	将角度转换为弧度
"""

# 数学常量
"""
pi	数学常量 pi（圆周率，一般以π来表示）
e	数学常量 e，e即自然常数（自然常数）。
"""

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