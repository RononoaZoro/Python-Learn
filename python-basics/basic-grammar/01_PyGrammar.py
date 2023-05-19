import keyword

# hello world
# 多行注释
'''
hello world
'''

"""
hello world
"""
print("Hello world")

# 保留字
kwlist = keyword.kwlist
print(kwlist)

# 行与缩进
if True:
    print("True")
else:
    print("False")

# 多行语句
total = 1 + \
        2 + \
        3
print(total)

# 在 [], {}, 或 () 中的多行语句，不需要使用反斜杠 \
total = ['item_one', 'item_two', 'item_three',
         'item_four', 'item_five']
