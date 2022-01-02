#https://www.acmicpc.net/problem/15649
import sys

# 풀이 2.
def search(Arry,Switch):
    if len(Arry) == M:
        print(" ".join(map(str,Arry)))
        return
    else:
        for i in range(1,N+1):
            if Switch[i-1] == False:
                Arry.append(i)
                Switch[i-1] = True
                search(Arry, Switch)
                Switch[i-1] = False
                Arry.pop()

def solve():
    global N,M
    N,M = map(int,sys.stdin.readline().split())
    Arry=[]
    Switch = [False]*N
    search(Arry,Switch)   
    
if __name__ == "__main__":
    solve()