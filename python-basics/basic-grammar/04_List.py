# 列表创建
list1 = ['Google', 'Runoob', 1997, 2000]
list2 = [1, 2, 3, 4, 5 ]
list3 = ["a", "b", "c", "d"]
list4 = ['red', 'green', 'blue', 'yellow', 'white', 'black']

# 访问
list = ['red', 'green', 'blue', 'yellow', 'white', 'black']
print( list[0] )
print( list[1] )
print( list[2] )
print( list[-1] )
print( list[-2] )
print( list[-3] )

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