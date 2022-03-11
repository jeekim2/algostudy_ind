#https://www.acmicpc.net/problem/1874

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Stack:
    def __init__(self):
        self.head = None
    def push(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def pop(self):
        if self.is_empty():
            return -1
        data = self.head.data
        self.head = self.head.next
        return data
    def is_empty(self):
        if self.head:
            return False
        return True
    def peak(self):
        if self.is_empty():
            return -1
        return self.head.data

def solve():
    N = int(input())
    Seq = []
    stack = Stack()
    for _ in range(N):
        Seq.append(int(input()))
    i, k=1, 0
    stack.push(i)
    while not stack.is_empty():
        i+=1
        if stack.peak() == Seq[k]:
            stack.pop()
            print("-")
        else:
            stack.push(i)
            print("+")

if __name__ == "__main__":
    solve()


