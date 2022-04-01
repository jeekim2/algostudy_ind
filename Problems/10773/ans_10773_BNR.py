# https://www.acmicpc.net/problem/10773

#https://appia.tistory.com/126
#https://koosco.tistory.com/82?category=848858

import sys

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class linked_stack(object):
    def __init__(self):
        self.head = None

    def pushFirst(self, data):
        newnode = Node(data)
        newnode.next = self.head  #값이 아니고 head가 가르키고 있던 주소
        self.head = newnode
        return self.head.data

    def pop(self):
        
        popitem = self.head.data
        self.head = self.head.next
        return popitem

def solve():
    input = sys.stdin.readline
    N = int(input())
    TC = linked_stack()
    stacksum = 0
    for _ in range(N):
        num = int(input())
        if num != 0:
            stacksum += TC.pushFirst(num)
        else:
            stacksum -= TC.pop()
    
    print(stacksum)

if __name__ == "__main__":
    solve()