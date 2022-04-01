# https://www.acmicpc.net/problem/11444
# 문제 : n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램 작성
# 입력 : 숫자 n
# 출력 : n번째 피보나치 % 1000000007 출력
# 어려웠던 점 : 동적 계획법으로 풀면 심플한데 메모리 초과가 된다고 함...
# 그래서 Matrix를 곱해서 연산량을 줄이는 방식을 생각해야 하는데, 이걸 도저히 떠올릴 수 없어서 원리를 좀 찾아봄...
'''(참고 링크) 
https://claude-u.tistory.com/406
https://www.acmicpc.net/blog/view/28
https://shoark7.github.io/programming/algorithm/%ED%94%BC%EB%B3%B4%EB%82%98%EC%B9%98-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%EC%9D%84-%ED%95%B4%EA%B2%B0%ED%95%98%EB%8A%94-5%EA%B0%80%EC%A7%80-%EB%B0%A9%EB%B2%95.html
'''

import sys

def matrix_mul(A, B):
    result = [[0, 0], [0, 0]]
    
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j]+=A[i][k]*B[k][j]
            result[i][j] %= 1000000007
    return result

def fibonacci(n):
    A = [[1,1],[1,0]]
    
    if n==1:
        return A
    m = fibonacci(n//2)
    if n % 2:
        return matrix_mul(matrix_mul(m, m), A)
    else:
        return matrix_mul(m, m)

def solve():
    input = sys.stdin.readline
    N = int(input())
    
    ans = fibonacci(N)
    print(ans[1][0])

if __name__ == "__main__":
    solve()