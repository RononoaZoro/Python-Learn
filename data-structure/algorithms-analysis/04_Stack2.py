from typing_extensions import SupportsIndex


class Stack(list):
    def push(self, item):
        self.append(item)

    def peek(self, item):
        return self[-1]

    def isEmpty(self):
        return self == None or self.isEmpty()

    def size(self):
        return len(self)
