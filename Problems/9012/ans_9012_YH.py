#https://www.acmicpc.net/problem/9012

import sys

# def solve1(): #잘못된 풀이 - 반례 : 1, )(
#     input = sys.stdin.readline
#     T = int(input())
#     cnt = 0
#     result = []
#     for _ in range(T):
#         PS = list(input().rstrip())
#         while len(PS)>0:
#             temp = PS.pop()
#             if  temp == '(':
#                 cnt+=1
#             else:
#                 cnt-=1
#         if abs(cnt) : result.append("NO")
#         else: result.append("YES")
#     print("\n".join(result))

def solve2(): #Pass
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        PS = list(input().rstrip())
        stack = []
        for x in PS:
            if x == '(':
                stack.append(x)
            elif x == ')' and '(' not in stack:
                stack.append(x)
            else:
                stack.pop()
        if len(stack) == 0 : print("YES")
        else : print("NO")

if __name__ == "__main__":
    solve2()