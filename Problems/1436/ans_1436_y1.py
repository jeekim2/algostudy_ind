#https://www.acmicpc.net/problem/1436

def solve():
    N = int(input())
    k, num =0, 0
    while k != N:
        num+=1
        if "666" in str(num):
            k+=1            
        
    return print(num)

if __name__ == "__main__":
    solve()