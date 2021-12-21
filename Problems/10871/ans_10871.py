# https://www.acmicpc.net/problem/10871

# 입력 : 정수 N개로 이루어진 수열 A와 정수 X
# 출력 : X보다 작은 수를 입력 받은 순서대로 출력

def compare():
    N,X = map(int,input().split())
    A = list(map(int,input().split()))
    # input().split()) -> output = string type
    # map(int,input().split()) -> output = map object at address
    
    for i in range(N):
        if A[i] < X :
            print(A[i], end=" ")

if __name__ == "__main__":
    compare()    