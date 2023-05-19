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
        l = l.append([i])

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
