# https://www.acmicpc.net/problem/2750
# 문제 : N개의 수가 주어졌을 때 오름차순 정렬
# 입력 : 첫째 줄 = 수의 개수, 둘쨰 줄부터 N개의 줄에 숫자 입력
# 출력 : 첫째 줄부터 N개의 오름차순 정렬 결과
# 시간 복잡도가 O(n²)인 정렬 알고리즘. (예)삽입 정렬, 거품 정렬 등

def insert_sort():
    global num
    for i in range(1,N):
        while i > 0 and num[i] < num[i-1]:
            num[i], num[i-1] = num[i-1], num[i]
            i -= 1
    return num

def solve():
    global num
    global N
    N = int(input())
    num = [0]*N
    for i in range(N):
        num[i] = int(input())
    
    for val in insert_sort():
        print(val)
    
if __name__ == '__main__':
    solve()