from string import digits, hexdigits

from pythonds.basic.stack import Stack

# def payChecker(symbolString):
#     s = Stack()
#     balanced = True
#     index = 0
#     while index < len(symbolString) and balanced:
#         symbol = symbolString[index]
#         if symbol == "(":
#             s.push(symbol)
#         else:
#             if s.isEmpty():
#                 balanced = False
#             else:
#                 s.pop()
#         index += 1
#
#     if balanced and s.isEmpty():
#         return True
#     else:
#         return False
#
#
# print(payChecker('(((()))())'))
# print(payChecker('(((()'))
#
#
# def parChecker(symbolString):
#     s = Stack()
#     balanced = True
#     index = 0
#     while index < len(symbolString) and balanced:
#         symbol = symbolString[index]
#         if symbol in "([{":
#             s.push(symbol)
#         else:
#             if s.isEmpty():
#                 balanced = False
#             else:
#                 top = s.pop()
#                 if not matches(top, symbol):
#                     balanced = False
#         index = index + 1
#     if balanced and s.isEmpty():
#         return True
#     else:
#         return False
#
#
# def matches(open, close):
#     opens = "([{"
#     closers = ")]}"
#     return opens.index(open) == closers.index(close)
#
#
# print(parChecker('{{([][])}()}'))
# print(parChecker('[{()]'))

"""
十进制转二进制
“除以2”的过程，得到的余数是从低到高的次序，而输出则是从高到低，所以需要一个栈来反转次序
"""

# def divideBy2(decNumber):
#     remstack = Stack()
#     while decNumber > 0:
#         rem = decNumber % 2
#         remstack.push(rem)
#         decNumber //= 2
#
#     binString = ""
#     while not remstack.isEmpty():
#         binString += str(remstack.pop())
#
#     return binString
#
#
# print(divideBy2(155))
# print(155 // 155)
#
#
# def baseConverter(decNumber,base):
#     remstack = Stack()
#     while decNumber > 0:
#         rem = decNumber % base
#         remstack.push(rem)
#         decNumber //= base
#
#     binString = ""
#     while not remstack.isEmpty():
#         binString += hexdigits[remstack.pop()]
#
#     return binString
#
# print(baseConverter(155,155))
# print(baseConverter(155,16))

"""
- 后面的算法描述中，约定中缀表达式是由空格隔开的一系列单词(token)构成
  - 操作符单词包括`*/+-()`，而操作数单词则是大写单字母标识符`A、B、C`等。
- 首先，创建空栈opstack用于暂存操作符,空表postfixList用于保存后缀表达式
- 将中缀表达式转换为单词(token)列表
  - `A+B*C=split=>['A','+',B',*','C']`

- 从左到右扫描中缀表达式单词列表
  - 如果单词是操作数，则直接添加到后缀表达式列表的末尾
  - 如采单词是左括是“`(`”，则压入opstack栈顶
  - 如果单词是右括是“`)`”，则反复弹出opstack栈顶操作符，加入到输出列表末尾，直到碰到左括号
  - 如果单词是操作符“`*/+-`”，则压入opstack栈顶
    - 但在入之前，要比较其与栈顶操作符的优先级
    - 如果栈顶的高于或等于它，就要反复弹出栈顶操作符，加入到输出列表末尾
    - 直到栈顶的操作符优先级低于它
  - 中缀表达式单词列表扫描结束后，把opstack栈中的所有剩余操作符依次弹出，添加到输出列表末尾
  - 把输出列表再用join方法合并成后缀表达式字符串，算法结束。
"""


def infixToPostfix(infixespr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()
    postfixList = []
    tokenList = infixespr.split()
    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != None and topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and \
                    (prec[opStack.peek()] >= prec[token]):
                postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())

    return " ".join(postfixList)


#
#
# print(infixToPostfix("A * B + C * D"))
# print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))


"""
##### 后缀表达式求值

- 作为栈结构的结束，我们来讨论“后缀表达式求值”问题

>跟中缀转换为后缀问题不同，在对后缀表达式从左到右扫描的过程中，由于操作符在操作数的后面
>所以要暂存操作数，在碰到操作符的时候,再将暂存的两个操作数进行实际的计算，这仍然是栈的特性：操作符只作用于离它最近的两个操作数

如“456*+”，我们先扫描到4、5两个操作数,但还不知道对这两个操作数能做什么计算
需要继续扫描后面的符号才能知道,继续扫描，又碰到操作数6
还是不能知道如何计算，继续暂存入栈,直到”*”,现在知道是栈顶两个操作数5、6做乘法

我们弹出两个操作数，计算得到结果30,需要注意：先弹出的是右操作数,后弹出的是左操作数，这个对于-/很重要！
为了继续后续的计算，需要把这个中间结果30压入栈顶,继续扫描后面的符号,当所有操作符都处理完毕，栈中只留下1个操作数，就是表达式的值

1、创建空栈operandStack用于暂存操作数
2、将后缀表达式用split方法解析为单词(token)的列表
3、从左到右扫描单词列表
    - a、如果单词是一个操作数，将单词转换为整数int,压入operandStack栈顶
    - b、如果单词是一个操作符（*/+-），就开始求值，从栈顶弹出2个操作数，先弹出的是右操作数，后弹出的是左操作数，计算后将值重新压入栈顶
4、单词列表扫描结束后，表达式的值就在栈顶
5、弹出栈顶的值，返回。
"""


def doMath(token, leftOperand, rightOperand):
    if token == '+':
        return leftOperand + rightOperand
    elif token == '-':
        return leftOperand - rightOperand
    elif token == '*':
        return leftOperand * rightOperand
    else:
        return leftOperand / rightOperand


def postfixEval(postfixExpr):
    operandStack = Stack()
    tokenList = postfixExpr.split()

    for token in tokenList:
        if token in "0123456789":
            operandStack.push(int(token))
        else:
            rightOperand = operandStack.pop()
            leftOperand = operandStack.pop()
            result = doMath(token, leftOperand, rightOperand)
            operandStack.push(result)

    return operandStack.pop()


print(infixToPostfix('1 + 2 * 4 + 5 - 6'))
print(postfixEval(infixToPostfix('1 + 2 * 4 + 5 - 6')))
