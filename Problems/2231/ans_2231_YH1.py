#https://www.acmicpc.net/problem/2231
import sys

def solve():
    input = sys.stdin.readline
    n = int(input())
    result=[]
    low = n - len(str(n))*9 #분해합 9x크기로 생성자의 min 설정
    if low < 0: # 생성자의 min은 0이상임.
        low = 0
    for i in range(low,n):
        num_div = list(str(i)) # 각 자리수를 분해
        if (i+sum(map(int,num_div))) == n:
            result.append(i)
    if result ==[]:
        print(0)
    else:
        print(min(result))

if __name__ == "__main__":
    solve()          
    