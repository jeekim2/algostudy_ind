# https://www.acmicpc.net/problem/1010

# 강의 서쪽에는 N개의 사이트가 있고 동쪽에는 M개의 사이트가 있다는 것을 알았다. (N ≤ M)
# 재원이는 서쪽의 사이트와 동쪽의 사이트를 다리로 연결하려고 한다. (이때 한 사이트에는 최대 한 개의 다리만 연결될 수 있다.)
# 재원이는 다리를 최대한 많이 지으려고 하기 때문에 서쪽의 사이트 개수만큼 (N개) 다리를 지으려고 한다.
# 다리끼리는 서로 겹쳐질 수 없다고 할 때 다리를 지을 수 있는 경우의 수를 구하는 프로그램을 작성하라.
# 입력의 첫 줄에는 테스트 케이스의 개수 T가 주어진다.
# 그 다음 줄부터 각각의 테스트케이스에 대해 강의 서쪽과 동쪽에 있는 사이트의 개수 정수 N, M (0 < N ≤ M < 30)이 주어진다.


import sys


def combinat(M, N):
    if dic.get((M, N)):
        return dic[(M, N)]
    if N == 0:
        dic[(M, N)] = 1
        return 1
    if M == N:
        dic[(M, N)] = 1
        return 1
    if N == 1:
        dic[(M, N)] = M
        return M
    if M - N == 1:
        dic[(M, N)] = M
        return M
    dic[(M, N)] = combinat(M - 1, N - 1) + combinat(M - 1, N)
    return dic[(M, N)]


def solve():
    global dic
    dic = {}
    T = int(input())
    TCs = []
    for _ in range(T):
        TCs.append(list(map(int, input().split())))
    for TC in TCs:
        N = TC[0]
        M = TC[1]
        print(combinat(M, N))
    return


if __name__ == "__main__":
    solve()
