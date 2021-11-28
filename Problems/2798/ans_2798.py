#https://www.acmicpc.net/problem/2798

def solve():
    N, M = input().split()
    Card = list(map(int, input().split()))
    Max = 0
    
    #와 모르겠다...
    for x in range(int(N)-2):
        for y in range(x+1, int(N)-1):
            for z in range(y+1,int(N)):
                Sum = Card[x]+Card[y]+Card[z] 
                if Sum <=int(M):
                    if Sum >= Max:
                        Max = Sum
    print(Max)
    
if __name__ == "__main__":
    solve()