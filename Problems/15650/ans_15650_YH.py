#https://www.acmicpc.net/problem/15650

import sys

def sequenceNM():
    if len(arry)==M:
        print(" ".join(map(str, arry)))
        return
    for i in range(1,N+1):
        if (i in arry):
            continue
        if (len(arry)>=1 and i<arry[-1]):
            continue
        arry.append(i)
        sequenceNM()
        arry.pop()
            
def solve():
    input = sys.stdin.readline
    global N,M,arry
    N,M = map(int,input().split())
    arry=[]
    sequenceNM()
    
if __name__=="__main__":
    solve() 