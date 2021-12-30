#https://www.acmicpc.net/problem/1316

import sys

#쉽게 생각했는데.. 자꾸 꼬이네.. 다시 생각 필요!!
def solve():
    input = sys.stdin.readline
    N = int(input())
    char = []
    cnt, check = 0, False
    for _ in range(N):
        char.append(input().rstrip())

    for c in char:
        cnt+=1
        for i in range(len(c)):
            temp = c.count(c[i])
            if temp > 1 and c[i] != c[i+temp-1]:
                check = True
        if check == True:
            cnt-=1
            check = False
                    
    print(cnt)

if __name__ == "__main__":
    solve()

    
                


