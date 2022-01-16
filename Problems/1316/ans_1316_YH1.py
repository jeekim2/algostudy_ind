#https://www.acmicpc.net/problem/1316

import sys

#쉽게 생각했는데.. 자꾸 꼬이네.. 다시 생각 필요!!
#다른 풀이보니까 dictionary로 풀어버리네... 2번째 풀이로 따라해보겠음
def solve():
    input = sys.stdin.readline
    N = int(input())
    char_list = []
    cnt= 0
    for _ in range(N):
        char_list.append(input().rstrip())

    for char in char_list:
        if len(char) != len(set(char)):
            cnt1 = 1            
            for i in range(len(char)-2):
                if char[i] != char[i+1] and char[i] in char[i+2:]:
                    cnt1 = 0
            cnt+=cnt1
        else:
            cnt+=1
                   
    print(cnt)

if __name__ == "__main__":
    solve()

    
                


