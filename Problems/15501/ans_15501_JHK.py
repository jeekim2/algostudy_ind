# https://www.acmicpc.net/problem/15501


def solve():
    N = int(input())
    Org = list(map(int, input().split()))
    Target = list(map(int, input().split()))
    for targetIdx, v in enumerate(Target):
        if v == Org[0]:
            break
    direction = False
    if N == 1:
        print("good puzzle")
        return

    if targetIdx == N - 1:
        if Target[0] == Org[1]:
            direction = True
    else:
        if Target[targetIdx + 1] == Org[1]:
            direction = True

    orgIdx = 0
    while orgIdx < N:
        if targetIdx == N:
            targetIdx = 0
        if direction:
            if Target[targetIdx] != Org[orgIdx]:
                print("bad puzzle")
                return
        else:
            if Target[targetIdx] != Org[-orgIdx]:
                print("bad puzzle")
                return
        orgIdx += 1
        targetIdx += 1
    print("good puzzle")
    return


if __name__ == "__main__":
    solve()
