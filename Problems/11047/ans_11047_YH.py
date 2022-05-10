#https://www.acmicpc.net/problem/11047

def solve():
    N,Cost = map(int, input().split())
    Coin = [int(input()) for _ in range(N)]
    cnt = 0
    for i in range(N-1,-1,-1):
        if Cost == 0: break
        if Cost>=Coin[i]:
            cnt += Cost//Coin[i]
            Cost%=Coin[i]
    return print(cnt)

if __name__ =="__main__":
    solve()