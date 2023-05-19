import time


def sumOfN(n):
    start = time.time()
    theSum = 0
    for i in range(1, n + 1):
        theSum = theSum + i
    end = time.time()
    return theSum, end - start


print(sumOfN(10))


def sumOfN1(n):
    start = time.time()
    theSum = 0
    for i in range(n):
        theSum = theSum + (i + 1)
    end = time.time()
    return theSum, end - start


def sumOfN2(n):
    start = time.time()
    theSum = n * (n + 1) / 2
    end = time.time()
    return theSum, end - start


print(sumOfN1(10))

for i in range(5):
    print("Sum is %d required %10.7f seconds" % sumOfN1(1000000))
    print("Sum is %d required %10.7f seconds" % sumOfN2(1000000))

"""
print("Sum is %d required %10.7f seconds" % sumOfN1(10000))
"Sum is %d required %10.7f seconds"是一个格式化字符串，其中包含了两个占位符。

- %d表示一个整数的占位符。
- %10.7f表示一个浮点数的占位符，其中10表示总宽度为10个字符，包括小数点和小数部分，而.7表示小数部分保留7位有效数字。
- % sumOfN1(10000)表示使用sumOfN1(10000)函数的返回值来填充格式化字符串中的占位符。
"""
