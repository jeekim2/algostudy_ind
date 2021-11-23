import sys


def solve():
    input = sys.stdin.readline
    N = int(input())
    up_level_sum = [0]
    for _ in range(N):
        level = list(map(int, input().split()))
        for i, v in enumerate(level):
            if i == 0:
                level[i] += up_level_sum[0]
                continue
            if i == len(level) - 1:
                level[i] += up_level_sum[i - 1]
                continue
            if up_level_sum[i - 1] >= up_level_sum[i]:
                level[i] += up_level_sum[i - 1]
            else:
                level[i] += up_level_sum[i]
        up_level_sum = level

    print(max(up_level_sum))
    return


if __name__ == "__main__":
    solve()
