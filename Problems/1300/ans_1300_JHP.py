# https://www.acmicpc.net/problem/1300
# 문제 : K번째 수 찾기 (B[k] 구하기)
# 입력 : 첫번째줄 = 배열의 크기 N, 둘째줄 = k
# 출력 : B[k] 출력

# N*N 숫자를 정렬해서 for로 풀려고 하니 시간초과 남. 다른 방식 접근 필요

# (접근방식) B[k]를 찾기 위해 i*j보다 작은 숫자 찾기 
# N=10일 때, 30보다 작은 수 
# [1 2 3 4 ... 1*N] -> 1*10
# [2 4 6 8 ... 2*N] -> 2*10
# [3 6 9 12 .. 3*N] -> 3*10
# [4 8 12 k .. 4*N] -> 4*7
# 즉, 37개의 숫자이고 3개의 숫자가 30보다 큼
# 다른 의미로, 30을 행으로 나눠보면 똑같은 것을 의미함
# 30//1 = 10개 (N개 이상은 불가)
# 30//2 = 10개 (N개 이상은 불가)
# 30//3 = 10개
# 30//4 = 7개 
# 위에 뜻과 동일함.

def bs(n,target):
    left = 0
    right = target

    while left <= right:
        mid = (left+right)//2
        cnt = 0
        for i in range(1, n+1):
            cnt += min(mid//i,n) 
            
        if cnt >= target:
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    return result

def solve():
    N = int(input())
    k = int(input())
    
    print(bs(N,k))

if __name__ == "__main__":
    solve()