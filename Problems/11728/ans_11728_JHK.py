# https://www.acmicpc.net/problem/11728


def solve():
    N, M = map(int, input().split())
    ArrA = list(map(int, input().split()))
    ArrB = list(map(int, input().split()))
    i = 0
    j = 0
    while i < len(ArrA) and j < len(ArrB):
        if ArrA[i] < ArrB[j]:
            print(ArrA[i], end=" ")
            i += 1
        else:
            print(ArrB[j], end=" ")
            j += 1
    while i < len(ArrA):
        print(ArrA[i], end=" ")
        i += 1
    while j < len(ArrB):
        print(ArrB[j], end=" ")
        j += 1
    print()
    return


if __name__ == "__main__":
    solve()
