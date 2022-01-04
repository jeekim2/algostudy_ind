# https://www.acmicpc.net/problem/2805


def solve():
    N, M = map(int, input().split())
    trees = list(map(int, input().split()))
    left = 0
    right = max(trees)
    while right - left > 1:
        mid = (left + right) // 2
        sumTree = 0
        for t in trees:
            if t > mid:
                sumTree += t - mid
        if sumTree > M:
            left = mid
        elif sumTree < M:
            right = mid
        else:
            left = mid
            right = mid
    print(left)


if __name__ == "__main__":
    solve()
