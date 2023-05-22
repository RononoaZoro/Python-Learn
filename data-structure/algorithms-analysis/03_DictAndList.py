import timeit
from timeit import Timer
import random

""""""
"""
# List 列表数据类型
list类型各种操作(interface)的实现方法有很多，如何选择具体哪种实现方法？
总的方案就是，让最常用的操作性能最好,牺牲不太常用的操作
80/20准则：88%的功能其使用率只有20%
"""

"""
- 最常用的是：按索引取值和赋值(V=a[i],a[i]=v)
由于列表的随机访问特性，这两个操作执行时间与列表大小无关，均为O(1)

- 另一个是列表增长，可以选择append()和_add_() "+"
list.append(v),执行时间是O(1)
list=list+[v],执行时间是O(n+k),其中k是被加的列表长度
选择哪个方法来操作列表，决定了程序的性能
"""

"""
首先是循环连接列表(+)方式生成
"""


def test1():
    l = []
    for i in range(1000):
        l = l + [i]


"""
然后是用append方法添加元素生成
"""


def test2():
    l = []
    for i in range(1000):
        l.append(i)


"""
接着用列表推导式来做
"""


def test3():
    l = [i for i in range(1000)]


"""
最后是range函数调用转成列表
"""


def test4():
    l = list(range(1000))


"""
- 创建一个Timer对象，指定需要反复运行的语句和只需要运行一次的“安装语句”
- 然后调用这个对象的timeit方法，其中可以指定反复运行多少次

__main__模块是Python中的一个特殊模块名称。当Python解释器执行一个脚本文件时，该文件被视为主程序（main program），其模块名称被设置为__main__。
__main__模块在Python中还有其他用途，例如在模块内部进行一些测试和调试操作时，可以使用if __name__ == "__main__":语句来判断当前模块是否被当作主程序执行，从而执行相应的代码。
"""
# t1 = Timer("test1()", "from __main__ import test1")
# print("concat %f seconds\n" % t1.timeit(number=1000))
#
# t2 = Timer("test2()", "from __main__ import test2")
# print("append %f seconds\n" % t2.timeit(number=1000))
#
# t3 = Timer("test3()", "from __main__ import test3")
# print("comprehension %f seconds\n" % t3.timeit(number=1000))
#
# t4 = Timer("test4()", "from __main__ import test4")
# print("list range %f seconds\n" % t4.timeit(number=1000))

"""
运行结果：
concat 4.204483 seconds

append 0.422084 seconds

comprehension 0.122807 seconds

list range 0.045583 seconds

我们看到，4种方法运行的时间差别很大
列表连接(concat)最慢，List range最快，速度相差近92倍。
append也要比concat快得多
另外，我们注意到列表推导式速度是append两倍的样子
"""

"""

- 我们注意到pop这个操作
    pop()从列表末尾移除元素，O(1)
    pop(i)从列表中部移除元素，O(n)
- 原因在于Python所选择的实现方法
    从中部移除元素的话，要把移除元素后面的元素全部向前挪位复制一遍，这个看起来有点笨拙
    但这种实现方法能够保证列表按索引取值和赋值的操作很快，达到O(1)这也算是一种对常用和不常用操作的折衷方案
"""

"""
# list.pop的计时试验
- 为了验证表中的大O数量级，我们把两种情况下的pop操作来实际计时对比
相对同一个大小的1ist,分别调用pop()和pop(0)
- 对不同大小的list做计时，期望的结果是
pop()的时间不随1ist大小变化，pop(0)的时间随着1ist变大而变长
"""
# x0 = list(range(2000000))
# popzero = timeit.Timer("x0.pop(0)", "from __main__ import x0")
# x1 = list(range(2000000))
# popend = timeit.Timer("x1.pop()", "from __main__ import x1")
# print("popzero run %f seconds, size %f\n" % (popzero.timeit(number=1000), len(x0)))
# print("popend run %f seconds, size %f\n" % (popend.timeit(number=1000), len(x1)))

"""
# 结果
popzero run 2.084515 seconds

popend run 0.000069 seconds

相差35000多倍
"""

"""
通过改变列表的大小来测试两个操作的增长趋势
"""
# popend = timeit.Timer("x.pop()", "from __main__ import x")
# popzero = timeit.Timer("x.pop(0)", "from __main__ import x")
# print("        pop()           pop(0)")
# for i in range(1000000, 100000001, 1000000):
#     x = list(range(i))
#     pt = popend.timeit(number=1000)
#     x = list(range(i))
#     pz = popzero.timeit(number=1000)
#     print("%15.5f, %15.5f" % (pt, pz))

"""
pop()            pop(0)
0.00007,         1.78759
0.00025,         3.46439
0.00007,         3.83188
0.00029,         6.01310
0.00045,         6.69388
0.00026,         9.64040

pop()：基本不变，为常数,O(1)
pop(0):线性增长,O(n)
"""

# list和dict的in操作对比
"""
设计一个性能试验来验证list中检索一个值，以及dict中检索一个值的计时对比
生成包含连续值的list和包含连续关键码key的dict,用随机数来检验操作将in的耗时。
"""
print("size     list        dict")
for i in range(10000, 1000001, 20000):
    t = timeit.Timer("random.randrange(%d) in x" % i, "from __main__ import random,x")
    x = list(range(i))
    list_time = t.timeit(number=1000)
    x = {j: None for j in range(i)}
    dict_time = t.timeit(number=1000)
    print("%d,%10.3f,%10.3f" % (i, list_time, dict_time))


"""
# 输出
size     list        dict
10000,     0.089,     0.001
30000,     0.282,     0.002
50000,     0.457,     0.001
70000,     0.556,     0.002
90000,     0.714,     0.001
110000,     0.824,     0.001
130000,     0.941,     0.001
150000,     1.254,     0.003
170000,     1.776,     0.001
190000,     1.765,     0.001
210000,     1.863,     0.002
230000,     2.048,     0.001
列表是线性增长，O(n)
字典是常数，O(1)

python 官方算法复杂度网址：https://wiki.python.org/moin/TimeComplexity
"""