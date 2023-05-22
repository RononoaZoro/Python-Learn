
# 定义
var1 = 'Hello World!'
var2 = "Runoob"

# 访问
print ("var1[0]: ", var1[0])
print ("var2[1:5]: ", var2[1:5])

# 更新
var1 = 'Hello World!'

print("已更新字符串 : ", var1[:6] + 'Runoob!')

# 转义
"""
参考：https://www.runoob.com/python3/python3-string.html
"""

# 字符串运算符
"""
+	字符串连接	a + b                                                               输出结果： HelloPython
*	重复输出字符串	a*2                                                                 输出结果：HelloHello
[]	通过索引获取字符串中字符	a[1]                                                    输出结果 e
[ : ]	截取字符串中的一部分，遵循左闭右开原则，str[0:2] 是不包含第 3 个字符的。	a[1:4]      输出结果 ell
in	成员运算符 - 如果字符串中包含给定的字符返回 True	'H' in a                            输出结果 True
not in	成员运算符 - 如果字符串中不包含给定的字符返回 True	'M' not in a                    输出结果 True
r/R	原始字符串 - 原始字符串：所有的字符串都是直接按照字面的意思来使用，没有转义特殊或不能打印的字符。 原始字符串除在字符串的第一个引号前加上字母 r（可以大小写）以外，与普通字符串有着几乎完全相同的语法。	
    print( r'\n' )
    print( R'\n' )
%	格式字符串	请看下一节内容。
"""

# 字符串格式化
print ("我叫 %s 今年 %d 岁!" % ('小明', 10))

"""
%c	 格式化字符及其ASCII码
%s	 格式化字符串
%d	 格式化整数
%u	 格式化无符号整型
%o	 格式化无符号八进制数
%x	 格式化无符号十六进制数
%X	 格式化无符号十六进制数（大写）
%f	 格式化浮点数字，可指定小数点后的精度
%e	 用科学计数法格式化浮点数
%E	 作用同%e，用科学计数法格式化浮点数
%g	 %f和%e的简写
%G	 %f 和 %E 的简写
%p	 用十六进制数格式化变量的地址

# 格式化操作符辅助指令:
*	定义宽度或者小数点精度
-	用做左对齐
+	在正数前面显示加号( + )
<sp>	在正数前面显示空格
#	在八进制数前面显示零('0')，在十六进制前面显示'0x'或者'0X'(取决于用的是'x'还是'X')
0	显示的数字前面填充'0'而不是默认的空格
%	'%%'输出一个单一的'%'
(var)	映射变量(字典参数)
m.n.	m 是显示的最小总宽度,n 是小数点后的位数(如果可用的话)
"""

# 三引号
para_str = """这是一个多行字符串的实例
多行字符串可以使用制表符
TAB ( \t )。
也可以使用换行符 [ \n ]。
"""
print (para_str)

# f-string
"""
>>> name = 'Runoob'
>>> f'Hello {name}'  # 替换变量
'Hello Runoob'
>>> f'{1+2}'         # 使用表达式
'3'

>>> w = {'name': 'Runoob', 'url': 'www.runoob.com'}
>>> f'{w["name"]}: {w["url"]}'
'Runoob: www.runoob.com'
"""

# Unicode 字符串
"""
在Python2中，普通字符串是以8位ASCII码进行存储的，而Unicode字符串则存储为16位unicode字符串，这样能够表示更多的字符集。使用的语法是在字符串前面加上前缀 u。
在Python3中，所有的字符串都是Unicode字符串。
"""

# 字符串内建函数
"""
参考：https://www.runoob.com/python3/python3-string.html
"""