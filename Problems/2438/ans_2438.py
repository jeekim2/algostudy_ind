# 문제 : 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개

def star():
    N = int(input())
    
    if 1<=N<=100:
        for i in range(N): # range(stop-1) : default setup = index(stop-1)
            print("*"*(i+1))
    else:
        return 0

if __name__ == "__main__":
    star()