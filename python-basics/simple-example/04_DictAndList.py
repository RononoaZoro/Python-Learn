from timeit import Timer
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
t1 = Timer("test1()","from __main__ import test1")
print("concat %f seconds\n" % t1.timeit(number=1000))

t2 = Timer("test2()","from __main__ import test2")
print("append %f seconds\n" % t2.timeit(number=1000))

t3 = Timer("test3()","from __main__ import test3")
print("comprehension %f seconds\n" % t3.timeit(number=1000))

t4 = Timer("test4()","from __main__ import test4")
print("list range %f seconds\n" % t4.timeit(number=1000))

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