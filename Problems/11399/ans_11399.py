# import sys


def solve():
    # input = sys.stdin.readline
    N = int(input())
    t = list(map(int, input().split()))
    t.sort()
    sum = 0
    w = 0
    for i in t:
        w += i
        sum += w
    print(sum)


if __name__ == "__main__":
    solve()
