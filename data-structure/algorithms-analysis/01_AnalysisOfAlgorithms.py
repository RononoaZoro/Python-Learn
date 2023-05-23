from big_o import big_o, datagen


# 算法分析：算法复杂度
# 使用赋值语句的数量来衡量（从代码分析确定执行时间数量级函数）
def algorithmsAnaly(n):
    a = 5
    b = 6
    c = 10
    for i in range(n):
        for j in range(n):
            x = j * i
            y = j * j
            z = i * j

    for k in range(n):
        w = a * k + 45
        v = b * b

    d = 33


# T(n) = 3+3n²+2n+1=3n²+2n+4
# 数量级为 O(n²)
# 大O表示法：表示了所有上限中最小的那个上限
# 大Ω表示法：表示了所有下限中最大的那个下限【f(n)=Ω(g(n)),当且仅当g(n)=O(f(n))】
# 大Θ表示法：如果上下限相同，那么就可以用大Θ表示【f(n)=Θ(g(n)),当且仅当f(n)=O(g(n))且f(n)=Ω(g(n))】

"""
第三方模块big_O
pip install big-O
估算一个函数的大O数量级
big_o(
fuc,#需要估计大0数量级的算法函数，1个输入参数
data_generator,#能产生输入参数的函数，以N为参数
min_n,maX_n,n_measures,#最小N,最大N,取多少个N
n_repeats,#重复执行多少次func,来计算执行时间
n_timings)#重复测量多少次，保留最好测量结果
返回值：(best_class,fitted)最佳拟合的复杂度，以及其它拟合信息

一些通用的data_generator
big_o.datagen.n_(N)就是参数N
big_o.datagen.integers(N,min,max)返回N个随机整数list
big_o.datagen.range_n(N)返回参数N的range(N)列表list
参考官方文档：https://pypi.org/project/big-O
"""


# 定义一个函数，计算列表中所有元素的和
def sum_list(lst):
    total = 0
    for num in lst:
        total += num
    return total


# 评估 sum_list 函数的时间复杂度
# complexity, other = big_o(
#     sum_list,
#     lambda n: datagen.integers(n, 10000, 50000),
#     min_n=1000,
#     max_n=100000,
#     n_measures=100,
# )
# print(complexity)
"""
Linear: time = -0.00043 + 1.5E-07*n (sec)
线性:O(n)
"""

# complexity, other = big_o(
#     sorted,
#     lambda n: datagen.integers(n, 10000, 50000),
#     min_n=10000,
#     max_n=100000,
#     n_measures=100,
# )
# print(complexity)
"""
Linearithmic: time = -0.0014 + 4.5E-08*n*log(n) (sec)
线性对数:O(nlogn)
"""


# 创建一个BigO对象
bigo = big_o()

# 定义一个函数来评估算法的复杂度
def my_algorithm(n):
    for i in range(n):
        print(i)

# 使用BigO对象评估函数的复杂度
complexity = bigo.calculate(my_algorithm, inputs=[10, 100, 1000])
print(complexity)

