import itertools


def solve():
    MAN_NUM = int(input())
    MANS = []
    for i in range(MAN_NUM):
        MANS.append(tuple(list(map(int, input().split())) + [i]))

    ans = [1] * MAN_NUM
    for a, b in itertools.combinations(MANS, 2):
        if a[0] > b[0] and a[1] > b[1]:
            ans[MANS.index(b)] += 1
        elif b[0] > a[0] and b[1] > a[1]:
            ans[MANS.index(a)] += 1
    print(" ".join(map(str, ans)), end="")


if __name__ == "__main__":
    solve()
