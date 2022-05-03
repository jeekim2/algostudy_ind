#https://www.acmicpc.net/problem/10866


class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

class Deque:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
    def Push_front(self,data):
        if self.head == None:
            self.head = self.tail = Node(data)
        else:
            NewNode = Node(data)
            NewNode.prev = self.head
            NewNode.next = self.head.next
            self.head = NewNode
        self.size +=1
    def Push_back(self,data):
        if self.tail == None:
            self.head = self.tail = Node(data)
        else:
            NewNode = Node(data)
            NewNode.prev = self.tail.prev
            NewNode.next = self.tail
            self.tail = NewNode
        self.size +=1
    def Pop_front(self):
        if self.size !=0:
            temp = self.head.data
            self.head = self.head.next
            self.size-=1
            return temp
        return -1
    def Pop_back(self):
        if self.size !=0:
            temp = self.tail.data
            self.tail = self.tail.prev
            self.size-=1
            return temp
        return -1
    def qsize(self):
        return self.size
    def is_empty(self):
        if self.size == 0:
            return 1
        return 0
    def qfront(self):
        if self.size !=0:
            return self.head.data
        return -1
    def qback(self):
        if self.size !=0:
            return self.tail.data
        return -1

def solve():
    N = int(input())
    deque = Deque()
    for _ in range(N):
        cmd = list(input().split())
        if cmd[0] == "push_front":
            deque.Push_front(int(cmd[1]))
        elif cmd[0] == "push_back":
            deque.Push_back(int(cmd[1]))
        elif cmd[0] == "front":
            res = deque.qfront()
            print(res)
        elif cmd[0] == "back":
            res = deque.qback()
            print(res)
        elif cmd[0] == "size":
            res = deque.qsize()
            print(res)
        elif cmd[0] == "empty":
            res = deque.is_empty()
            print(res)
        elif cmd[0] == "pop_front":
            res = deque.Pop_front()
            print(res)
        else:
            res = deque.Pop_back()
            print(res)

if __name__== "__main__":
    solve()