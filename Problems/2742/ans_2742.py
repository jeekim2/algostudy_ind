# 문제 : 자연수 N이 주어졌을 때, N부터 1까지 한 줄에 하나씩 출력

def solve ():
    num = int(input())
    
    for i in range(num,0,-1): # range(start,stop,step)
        print(i)
    else:
        return 0
    
if __name__ == "__main__":
    solve()
