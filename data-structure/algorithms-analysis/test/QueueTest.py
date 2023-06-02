import random

from pythonds.basic.queue import Queue


# def hotPotato(nameList, num):
#     simqueue = Queue()
#     for name in nameList:
#         simqueue.enqueue(name)
#
#     while simqueue.size() > 1:
#         for i in range(num):
#             simqueue.enqueue((simqueue.dequeue()))
#         simqueue.dequeue()
#
#     return simqueue.dequeue()
#
#
# print(hotPotato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7))


"""
**具体案例**：

一个实验室，在任意的一个小时内，大约有10名学生在场，这一小时中，每人会发起2次左右的打印，每次1~20页
打印机的性能是：以草稿模式打印的话，每分钟10页，以正常模式打印的话，打印质量好，但速度下降为每分钟5页。

**问题**：

怎么设定打印机的模式，让大家都不会等太久的前提下尽量提高打印质量？

这是一个典型的决策支持问题，但无法通过规则直接计算，我们要用一段程序来模拟这种打印任务场景，然后对程序运行结果进行分析，以支特对打印机模式设定的决策。

**解决思路**：对问题建模

- a、首先对问题进行抽象，确定相关的对象和过程
  - 抛弃那些对问题实质没有关系的学生性别、年龄、打印机型号、打印内容、纸张大小等等众多细节
- b、对象：打印任务、打印队列、打印机
  - 打印任务的属性：提交时间、打印页数
  - 打印队列的属性：具有 FIFO 性质的打印任务队列
  - 打印机的属性：打印速度、是否忙
- c、过程一：生成和提交打印任务
  - 确定生成概率：实例为每小时会有10个学生提交的20个作业，这样，概率是每180秒会有1个作业生成并提交，概率为每秒1/180。
  - 确定打印页数：实例是1一20页，那么就是1~20页之间概率相同。
- d、过程二：实施打印
  - 当前的打印作业：正在打印的作业
  - 打印结束倒计时：新作业开始打印时开始倒计时，回 0 表示打印完毕，可以处理下一个作业
- e、模拟时间：
  - 统一的时间框架：以最小单位（秒）均匀流逝的时间，设定结束时间
  - 同步所有过程：在一个时间单位里，对生成打印任务和实施打印两个过程各处理一次

**模拟流程**：

- 创建打印队列对象
- 时间按照秒的单位流逝
  - 按照概率生成打印作业，加入打印队列
  - 如果打印机空闲，且队列不空，则取出队首作业打印，记录此作业等待时间
  - 如果打印机忙，则按服打印速度进行1秒打印
  - 如果当前作业打印完成，则打印机进入空闲
- 时间用尽，开始统计平均等待时间
- 作业的等待时间
  - 生成作业时，记录生成的时间戳
  - 开始打印时，当前时间减去生成时间即可
- 作业的打印时间
  - 生成作业时，记录作业的页数
  - 开始打印时，页数除以打印速度即可
"""
class Printer:
    def __init__(self, ppm):
        # 打印速度 单位：页数/分钟
        self.pagerate = ppm
        # 打印任务
        self.currentTask = None
        # 打印倒计时
        self.timeRemaining = 0

    #     打印 1s
    def tick(self):
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    # 打印忙
    def busy(self):
        # 三元表达式
        # return True if self.currentTask != None else False
        if self.currentTask != None:
            return True
        else:
            return False

    # 打印新作业
    def startNext(self, newTask):
        self.currentTask = newTask
        self.timeRemaining = newTask.getPages() \
                             * 60 / self.pagerate


class Task:

    def __init__(self, time):
        # 生成时间戳
        self.timestamp = time
        # 打印页数
        self.pages = random.randrange(1, 21)

    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    def waitTime(self, currentTime):
        # 等待时间
        return currentTime - self.timestamp


# 1/180 概率生成作业
def newPrintTask():
    num = random.randrange(1, 181)
    return True if num == 180 else False
    # if num == 180:
    #     return True
    # else:
    #     return False
