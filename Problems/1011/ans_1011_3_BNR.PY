"""
https://www.acmicpc.net/problem/1011

입력의 첫 줄에는 테스트케이스의 개수 T가 주어진다. 각각의 테스트 케이스에 대해 현재 위치 x 와 목표 위치 y 가 정수로 주어지며, x는 항상 y보다 작은 값을 갖는다. (0 ≤ x < y < 231)

각 테스트 케이스에 대해 x지점으로부터 y지점까지 정확히 도달하는데 필요한 최소한의 공간이동 장치 작동 횟수를 출력한다.

"""

def times(D):
    halfD=D/2
    n=1
    while (n**2 +n)/2 < halfD: # 거리의 반까지 등차수열의 합의 n값 찾기
        n=n+1
    T = n-1
    i = 0
    while i <= n:
        if (T**2+T)+i == D: #(등차수열의 합)*2 == 전체 거리 비교
            ti = 2*T+1 #같으면 출력
            break
        else:
            i = i +1
            if i == T: #등차수열로 안떨어질 때
                ti = 2*T+2
    return ti

TCNum=int(input())
for n in range(TCNum):
    TC = list(map(int, input().split()))
    dis = TC[1]-TC[0]
    print(times(dis))