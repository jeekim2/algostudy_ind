#https://www.acmicpc.net/problem/15651

def solve():
    global N,M, list
    N,M = map(int,input().split())
    list = []
    seqMN()

def seqMN():
    if len(list) == M:
        return print(' '.join(map(str, list)))
    for i in range(1,N+1):
        list.append(i)
        seqMN()
        list.pop()

if __name__ == "__main__":
    solve()
            