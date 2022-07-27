# https://www.acmicpc.net/problem/4889
import sys


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

        data = self.head.next.data
        self.head.next = self.head.next.next
        self.size -= 1
        return data

    def top(self):
        if self.size == 0:
            return -1
        data = self.head.next.data
        return data

    def isEmpty(self):
        return self.size == 0


def solve():
    input = sys.stdin.readline
    TC = []
    while True:
        temp = input().rstrip()
        if temp[0] == "-":
            break
        TC.append(temp)
    i = 1
    for s in TC:
        cnt = 0
        stack1 = Stack()
        stack2 = Stack()
        for c in s:
            stack1.push(c)
        direction = True
        while not (stack1.isEmpty() and stack2.isEmpty()):
            if direction:
                # stack1 to stack2
                if stack1.isEmpty():
                    direction = False
                    continue
                c = stack1.pop()
                if stack2.isEmpty():
                    if c == "{":
                        cnt += 1
                    stack2.push("}")
                    continue
                if stack2.top() == "}" and c == "{":
                    stack2.pop()
                    continue
                stack2.push(c)
            else:
                # stack2 to stack1
                if stack2.isEmpty():
                    direction = True
                    continue
                c = stack2.pop()
                if stack1.isEmpty():
                    if c == "}":
                        cnt += 1
                    stack1.push("{")
                    continue
                if stack1.top() == "{" and c == "}":
                    stack1.pop()
                    continue
                stack1.push(c)
        print(f"{i}. {cnt}")
        i += 1
    return


if __name__ == "__main__":
    solve()
