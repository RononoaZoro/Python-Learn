# 标识符
"""
第一个字符必须是字母表中字母或下划线 _ ,标识符的其他的部分由字母、数字和下划线组成,标识符对大小写敏感。
在 Python 3 中，可以用中文作为变量名，非 ASCII 标识符也是允许的了。
"""

# 函数
# def 函数名（参数列表）:
#     函数体

def hello() :
    print("Hello World!")

hello()


# # 计算面积函数
# def area(width, height):
#     return width * height
#
#
# def print_welcome(name):
#     print("Welcome", name)
#
#
# print_welcome("Runoob")
# w = 4
# h = 5
# print("width =", w, " height =", h, " area =", area(w, h))

# 在Python中，函数可以返回多个值。实际上，返回多个值的机制是通过将这些值封装在一个数据结构中进行的，通常使用元组（tuple）来实现。
# def get_name_and_age():
#     name = "John"
#     age = 30
#     return name, age
#
# person = get_name_and_age()
# print(person)  # 输出：("John", 30)
# print(person[0])  # 输出："John"
# print(person[1])  # 输出：30
