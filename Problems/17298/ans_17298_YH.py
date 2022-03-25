#https://www.acmicpc.net/problem/17298

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        return
#Singularly linked list
class Stack:
    def __init__(self):
        self.head = None
        return
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        return
    def pop(self):
        if self.isthere():
            data = self.head.data
            self.head = self.head.next
            return data
        return -1
    def isthere(self):
        if self.head:
            return True
        return False
    def peak(self):
        if self.isthere():
            return self.head.data
        return -1    

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    stack = Stack()
    res = [-1 for _ in range(N)]
    for i in range(N):
        while stack.isthere() and A[stack.peak()] < A[i]:
            res[stack.pop()] = A[i]
        stack.push(i)  

    return print(*res)

if __name__ =="__main__":
    solve()