
# 创建
"""
# d = {key1 : value1, key2 : value2, key3 : value3 }
1）不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住
2）键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行
"""

tinydict = {'name': 'runoob', 'likes': 123, 'url': 'www.runoob.com'}
tinydict1 = { 'abc': 456 }
tinydict2 = { 'abc': 123, 98.6: 37 }

# 空字典
# 使用大括号 {} 来创建空字典
emptyDict = {}

# 打印字典
print(emptyDict)
# 查看字典的数量
print("Length:", len(emptyDict))
# 查看类型
print(type(emptyDict))

emptyDict = dict()

# 打印字典
print(emptyDict)
# 查看字典的数量
print("Length:", len(emptyDict))
# 查看类型
print(type(emptyDict))

# 访问
tinydict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

print("tinydict['Name']: ", tinydict['Name'])
print("tinydict['Age']: ", tinydict['Age'])

# 修改
tinydict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

tinydict['Age'] = 8  # 更新 Age
tinydict['School'] = "菜鸟教程"  # 添加信息

print("tinydict['Age']: ", tinydict['Age'])
print("tinydict['School']: ", tinydict['School'])

# 删除
tinydict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

del tinydict['Name']  # 删除键 'Name'
tinydict.clear()  # 清空字典
del tinydict  # 删除字典

# 已经删除再操作字典，会抛异常
# print("tinydict['Age']: ", tinydict['Age'])
# print("tinydict['School']: ", tinydict['School'])