# https://www.acmicpc.net/problem/10942

# 팰린드롬 : 다시합창합시다


import sys


def checkPalindrome(data, results, s, e):
    if results[s][e] != None:
        return results[s][e]
        # DP load
    if data[s] == data[e]:
        if s + 1 == e:
            results[s][e] = True
            # 사잇값이 없는경우 (2자리 수열)
        else:
            results[s][e] = checkPalindrome(data, results, s + 1, e - 1)
            # 양 끝값이 같으면, 양 끝값 제외 그 사잇값이 팰린드롬이면 그 수열은 팰린드롬임.
    else:
        results[s][e] = False
    return results[s][e]


def solve():
    input = sys.stdin.readline
    N = int(input())
    data = tuple(map(int, input().split()))
    M = int(input())
    TC = []
    for _ in range(M):
        S, E = map(int, input().split())
        S -= 1
        E -= 1
        # 배열 index에 맞도록 처리
        TC.append((S, E))

    results = [[None] * N for _ in range(N)]
    # results : [s][e] - S부터 E까지 팰린드롬인지 검사 결과
    for i in range(N):
        results[i][i] = True
        # 한자리 수열은 무조건 팰린드롬임.
    for s, e in TC:
        print(int(checkPalindrome(data, results, s, e)))
    return


if __name__ == "__main__":
    solve()
