#https://www.acmicpc.net/problem/10828

import sys

def solve():
    input = sys.stdin.readline
    N = int(input())
    global stack
    stack = []
    for _ in range(N):
        cmd = input().split()
        result = stack_cmd(cmd)
        if result != None:
            print(result)

def stack_cmd(cmd):
    if cmd[0] == "push":
        stack.append(int(cmd[1]))
    elif cmd[0] == "pop":
        if stack == []:
            result = -1
        else:
            result = stack.pop()
        return result
    elif cmd[0] == "size":
        result = len(stack)
        return result
    elif cmd[0] == "empty":
        if stack == []:
            result = 1
        else:
            result = 0
        return result
    else:
        if stack == []:
            result = -1
        else:
            result = stack[-1]
        return result

if __name__ == "__main__":
    solve()
        