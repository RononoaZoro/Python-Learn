
# Timer（计时器）是用于测量时间间隔的工具或类。它可以用于衡量代码执行时间、定时任务、性能测试等场景。在 Python 中，有多种方式可以实现计时器功能。

# 1、使用 time 模块

import time

# 开始计时
start_time = time.time()

# 执行一些代码或任务
time.sleep(2)  # 模拟耗时操作

# 结束计时
end_time = time.time()

# 计算时间间隔
elapsed_time = end_time - start_time

print("执行耗时：", elapsed_time, "秒")

# 使用 timeit 模块

import timeit

# 定义要执行的代码片段
code = """
for i in range(100):
    print(i)
"""

# 测量执行时间
# number 参数指定执行代码的次数
elapsed_time = timeit.timeit(code, number=100)

print("执行耗时：", elapsed_time, "秒")
