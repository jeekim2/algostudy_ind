'''
https://www.acmicpc.net/problem/11866
'''
import sys

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class Q(object):
    def __init__(self):
        self.head = Node(None)
        self.count = 0
    
    def pushLast(self,data):
        pushData = Node(data)
        current = self.head.next
        if self.count ==0:
            self.head.next = pushData
        else:
            while current.next != None:
                current = current.next
            current.next = pushData
        self.count += 1
        return

    def popFirst(self):
        if self.count == 0:
            return -1
        else:
            delData = self.head.next.data
            self.head = self.head.next
            self.count -= 1
            return delData
    
    def printData(self):
        tmp = self.head
        i=0
        while tmp.next !=None:
            print(tmp.data)
            tmp = tmp.next
        print(tmp.data)

def solve():
    input = sys.stdin.readline
    N, K = map(int, input().split())

    N_data = Q()
    for i in range(1, N+1):
        N_data.pushLast(i)

    print("<", end="")
    for i in range(N):
        for _ in range(K-1):
            N_data.pushLast(N_data.popFirst())  #1,2번째 pop
        if i < N-1:
            print(N_data.popFirst(), end=", ")    #3번째 출력
        else:
            print(N_data.popFirst(), end="")

    print(">")    

    # N_data.printData()

if __name__ == "__main__":
    solve()