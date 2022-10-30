# https://www.acmicpc.net/problem/2812


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.size = 0

    def push(self, data):
        NewNode = Node(data)
        NewNode.next = self.head.next
        self.head.next = NewNode
        self.size += 1

    def pop(self):
        if self.size == 0:
            return -1
        TarNode = self.head.next
        self.head.next = TarNode.next
        self.size -= 1
        return TarNode.data

    def top(self):
        if self.size == 0:
            return 10
        return self.head.next.data

    def print(self):
        TarNode = self.head.next
        res = []
        while TarNode != self.tail:
            res.append(TarNode.data)
            TarNode = TarNode.next
        for n in res[::-1]:
            print(n, end="")
        print()


def solve():
    N, K = map(int, input().split())
    NumList = input()
    S = Stack()
    Top = 10
    for num in NumList:
        while int(num) > Top and K > 0:
            K -= 1
            S.pop()
            Top = S.top()
        # if int(num) <= Top:
        Top = int(num)
        S.push(Top)
    while K > 0:
        K -= 1
        S.pop()
    S.print()
    return


if __name__ == "__main__":
    solve()
