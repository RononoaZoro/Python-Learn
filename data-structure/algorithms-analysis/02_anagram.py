# 问题描述
"""
所谓“变位词”是指两个词之间存在组成字母的重新排列关系
如：heart和earth,python和typhon
为了简单起见，假设参与判断的两个词仅由小写
字母构成，而且长度相等
"""
"""
# 思路一：逐个匹配法
将词1中的字符逐个到词2中检查是否存在
存在就“打勾”标记（防止重复检查）
如果每个字符都能找到，则两个词是变位词
只要有1个字符找不到，就不是变位词
"""

# def anagramSolution1(s1, s2):
#     # 复制s2到列表中
#     alist = list(s2)
#     pos1 = 0
#     stillOK = True
#     # 循环 s1 中的每个字符
#     while pos1 < len(s1) and stillOK:
#         pos2 = 0
#         found = False
#         # 在s2逐个对比
#         while pos2 < len(alist) and not found:
#             if s1[pos1] == alist[pos2]:
#                 found = True
#             else:
#                 pos2 += 1
#         # 找到就打勾，找不到就返回False
#         if found:
#             alist[pos2] = None
#         else:
#             stillOK = False
#         pos1 += 1
#     return stillOK
#
#
# print(anagramSolution1("abcd", 'cdba'))
# print(anagramSolution1("abcde", 'cdbaa'))

"""
# 问题规模：词中包含的字符个数
# 主要部分在于两重循环：外层循环遍历S1每个字符，将执行n次，内层循环在s2中查找字符，每个字符的对比次数分别是1/2/3...n中的一个，而且各不相同
# 所以总执行次数是1+2+3+4+5+6+......+n
# 克制其数量级为O(n²)
# ∑(i=1,n)=n(n+1)/2=n²/2+n/2 --> O(n²)
"""

"""
# 思路二:排序法
将两个字特串都按照字母顺序排好序
再逐个字符对比是否相同，如果相同则是变位词
有任何不同就不是变位词
"""

# def anagramSolution2(s1,s2):
#     alist1=list(s1)
#     alist2=list(s2)
#
#     # 先排序
#     alist1.sort()
#     alist2.sort()
#     pos=0
#     matches=True
#     # 再逐个对比
#     while pos<len(s1) and matches:
#         if(alist1[pos]==alist2[pos]):
#             pos+=1
#         else:
#             matches=False
#     return matches
#
# print(anagramSolution2("abcd", 'cdba'))
# print(anagramSolution2("abcde", 'cdbaa'))

"""
# 问题规模：词中包含的字符个数
粗看上去，本算法只有一个循环，最多执行n次，数量级是O(n)
但循环前面的两个sort并不是无代价的，排序算法采用不同的解决方策，其运行时间数量级差不多是O(n²)或者O(n 1og n),大过循环的O(n)
所以本算法时间主导的步骡骤是排序步骤，本算法的运行时间数量级就等于排序过程的数量级O(n log n)
"""

"""
# 思路三：暴力法
暴力法解题思路为：穷尽所有可能组合
将s1中出现的字符进行全排列，再查看s2是否出现在全排列列表中
这里最大困难是产生s1所有字符的全排列，
根据组合数学的结论，如果n个字符进行全排列,其所有可能的字符串个数为n!

我们已知n!的增长速度甚至超过2ⁿ，
例如，对于20个字符长的词来说，将产生20!=2,432,902,008,176,640,000个候选词
如果每微秒处理1个候选词的话，需要近8万年时间来做完所有的匹配。
结论：暴力法恐怕不能算是个好算法
"""

"""
# 思路四：计数比较
解题思路：对比两个词中每个子母出现的次数，如果26个字母出现的次数都相同的话，这两个字符串就一定是变位词
具体做法：为每个词设置一个26位的计数器，先检查每个词，在计数器中设定好每个字母出现的次数
计数完成后，进入比较阶段，看两个字符串的计数器是否相同，如果相同则输出是变位词的结论
"""


def anagramSolution4(s1, s2):
    # 计数器
    c1 = [0] * 26
    c2 = [0] * 26
    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('a')
        c1[pos] += 1
    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')
        c2[pos] += 1
    j = 0
    stillOK = True
    # 比较
    while j < 26 and stillOK:
        if c1[j] == c2[j]:
            j += 1
        else:
            stillOK = False
    return stillOK
print(anagramSolution4("abcd", 'cdba'))
print(anagramSolution4("abcde", 'cdbaa'))

"""
# 问题规模：词中包含的字符个数
计数比较算法中有3个循环迭代，但不像解法1那样存在嵌套循坏
前两个循环用于对字符串进行计数，操作次数等于字符串长度n
第3个循环用于计数器比较，操作次数总是26次
所以总操作次数T(n)=2n+26,其数量级为O(n)
这是一个线性数量级的算法，是4个变位词判断算法中性能最优的

注意：值得注意的是，本算法依赖于两个长度为26的计数器列表，来保存字符计数，这相比前3个算法需要更多的存储空间
如果考虑由大字符集构成的词（如中文具有上万不同字符)，还会需要更多存储空间。
牺牲存储空间来换取运行时间，或者相反,这种在时间空间之间的取舍和权衡，在选择问题解法的过程中经常会出现。
“不可随处小便”，“小处不可随便“
"""
