#https://www.acmicpc.net/problem/9012
# 0209 skip
import sys

def solve1(): #잘못된 풀이 - 반례 : 1, )(
    input = sys.stdin.readline
    T = int(input())
    cnt = 0
    result = []
    for _ in range(T):
        PS = list(input().rstrip())
        while len(PS)>0:
            temp = PS.pop()
            if  temp == '(':
                cnt+=1
            else:
                cnt-=1
        if abs(cnt) : result.append("NO")
        else: result.append("YES")
    print("\n".join(result))

def solve2():
    input = sys.stdin.readline
    T = int(input())
    stack = []
    n=0
    for _ in range(T):
        PS = list(input().rstrip())
        for x in PS:
            if x == '(':
                stack.append(x)
                n+=1
            else:
                if len(stack) >0:
                    stack.pop()
                    n-=1
                else:
                    n+=1
        if len(stack) == 0 and n == 0 : print("YES")
        else : print("NO")

if __name__ == "__main__":
    solve2()