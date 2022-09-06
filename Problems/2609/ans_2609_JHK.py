# https://www.acmicpc.net/problem/2609

def gcd(p,q):
    if p < q:
        p, q = q, p

    while q != 0:
        p, q = q, p % q
    return p


def solve():
    N, M = map(int,input().split())
    gcdTemp = gcd(N,M)
    print(gcdTemp)
    print(N*M//gcdTemp)
    return

if __name__=="__main__":
    solve()