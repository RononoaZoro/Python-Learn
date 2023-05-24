print()

"""
# 用Python实现ADT Stack
在清楚地定义了抽象数据类型Stack之后，我们看看如何用Python来实现它
Python的面向对象机制，可以用来实现用户自定义类型
将ADT Stack实现为Python的一个Class
将ADT Stack的操作实现为Class的方法
由于Stack是一个数据集，所以可以采用Python的原生数据集来实现，我们选用最常用的数据集List来实现

不同的实现方案保持了ADT接口的稳定性
但性能有所不同，栈顶首端的版本，其push/pop的复杂度为O(n),而栈顶尾端的实现，其push/pop的复杂度为0(1)
"""

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.size() == 0:
            return None
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


s=Stack()
print(s.isEmpty())
print(s.pop())
print(None == None)