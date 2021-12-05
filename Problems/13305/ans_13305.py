import sys


def solve():
    input = sys.stdin.readline
    N = int(input())
    route = list(map(int, input().split()))
    city = list(map(int, input().split()))
    del city[-1]  # Not used
    # list(zip(city,route))
    cost = 0
    cur = 0
    i = 0
    for i in range(N - 2):
        if city[i] < city[i + 1]:
            city[i + 1] = city[i]

    for i in list(zip(city, route)):
        cost += i[0] * i[1]
    print(cost)


if __name__ == "__main__":
    solve()
