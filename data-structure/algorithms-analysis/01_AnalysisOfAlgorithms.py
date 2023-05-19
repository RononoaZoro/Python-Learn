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
