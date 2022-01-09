#https://www.acmicpc.net/problem/10828
import sys
input = sys.stdin.readline
T = int(input())
stack = []
out = []

for i in range(T):
    stack.append(input().split())

    #print("------------")
    #print("stack[0][0]:",stack[0][0])
    #print("stack:",stack)


    if stack[0][0] == "push":
        out.append(stack[0][1])
    elif stack[0][0] == "pop":
        if len(out) == 0:
            print("-1")
        else:
            print(out[-1])
            out.pop(-1)
    elif stack[0][0] == "size":
        print(len(out))
    elif stack[0][0] == "empty":
        if len(out) == 0:
            print("1")
        else:
            print("0")
    elif stack[0][0] == "top":
        if len(out) == 0:
            print("-1")
        else:
            print(out[-1])

    stack.pop(-1)
    #print("out:",out)

