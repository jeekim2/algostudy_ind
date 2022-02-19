'''
https://www.acmicpc.net/problem/10828

스택
LIFO(Last In First Out)

'''
import sys

global stack_list
stack_list = []

def push(num):
    stack_list.append(num)

def pop_func():
    if len(stack_list) == 0:
        print(-1)
    else:
        print(stack_list.pop())

def size():
    print(len(stack_list))

def empty():
    if len(stack_list) == 0:
        print(1)
    else:
        print(0)

def top():
    if len(stack_list) == 0:
        print(-1)
    else:
        print(stack_list[-1])        

def solve():
    N = int(sys.stdin.readline())
    order_list = []
    for i in range(N):
        order_list.append(list(sys.stdin.readline().split()))
        if order_list[i][0]=='push':
            push(order_list[i][1])
        elif order_list[i][0]=='pop':
            pop_func()
        elif order_list[i][0]=='size':
            size()
        elif order_list[i][0]=='empty':
            empty()
        else:
            top()

if __name__ == "__main__":
    solve()