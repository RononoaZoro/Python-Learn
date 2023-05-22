import operator
# 列表创建
list1 = ['Google', 'Runoob', 1997, 2000]
list2 = [1, 2, 3, 4, 5]
list3 = ["a", "b", "c", "d"]
list4 = ['red', 'green', 'blue', 'yellow', 'white', 'black']

# 访问
list = ['red', 'green', 'blue', 'yellow', 'white', 'black']
print(list[0])
print(list[1])
print(list[2])
print(list[-1])
print(list[-2])
print(list[-3])

# 更新
list = ['Google', 'Runoob', 1997, 2000]

print("第三个元素为 : ", list[2])
list[2] = 2001
print("更新后的第三个元素为 : ", list[2])

list1 = ['Google', 'Runoob', 'Taobao']
list1.append('Baidu')
print("更新后的列表 : ", list1)

# 删除
list = ['Google', 'Runoob', 1997, 2000]

print("原始列表 : ", list)
del list[2]
print("删除第三个元素 : ", list)

# 脚本操作符
# 长度
len([1, 2, 3])
# 组合
l1 = [1, 2, 3] + [4, 5, 6]
# 重复 等价于 ['Hi!', 'Hi!', 'Hi!', 'Hi!']
l2 = ['Hi!'] * 4
# 元素是否存在于列表中
isExist = 3 in [1, 2, 3]
# 迭代
for x in [1, 2, 3]:
    print(x, end=" ")

# 切片
L = ['Google', 'Runoob', 'Taobao']
"""
L[2]	'Taobao'	读取第三个元素
L[-2]	'Runoob'	从右侧开始读取倒数第二个元素: count from the right
L[1:]	['Runoob', 'Taobao']	输出从第二个元素开始后的所有元素
"""

# 列表比较
# 导入 operator 模块

a = [1, 2]
b = [2, 3]
c = [2, 3]
print("operator.eq(a,b): ", operator.eq(a, b))
print("operator.eq(c,b): ", operator.eq(c, b))


# 列表函数&方法
"""
# 函数
len(list)
列表元素个数
max(list)
返回列表元素最大值
min(list)
返回列表元素最小值
list(seq)
将元组转换为列表

# 方法
list.append(obj)
在列表末尾添加新的对象
list.count(obj)
统计某个元素在列表中出现的次数
list.extend(seq)
在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
list.index(obj)
从列表中找出某个值第一个匹配项的索引位置
list.insert(index, obj)
将对象插入列表
list.pop([index=-1])
移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
list.remove(obj)
移除列表中某个值的第一个匹配项
list.reverse()
反向列表中元素
list.sort( key=None, reverse=False)
对原列表进行排序
list.clear()
清空列表
list.copy()
复制列表
"""