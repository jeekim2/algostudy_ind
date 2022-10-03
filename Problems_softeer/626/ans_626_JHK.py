# https://softeer.ai/practice/info.do?idx=1&eid=626

import sys


def print_room_cond(arr):
    cnt = 0
    old = False
    res = []
    s = 0
    for i, v in enumerate(arr):
        if v and not old:
            cnt += 1
            s = i + 9
        elif not v and old:
            if s == 9:
                res.append("09-" + str(i + 9))
            else:
                res.append(str(s) + "-" + str(i + 9))
            s = 0
        old = v
    if s != 0:
        if s == 9:
            res.append("09-" + str(18))
        else:
            res.append(str(s) + "-" + str(18))
    print(f"{cnt} available:")
    for s in res:
        print(s)


def solve():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    Rooms = {}
    TempRooms = []
    for _ in range(N):
        TempRooms.append(input().rstrip())
    TempRooms.sort()
    for r in TempRooms:
        Rooms[r] = [True] * 9

    for _ in range(M):
        Name, Start, End = input().split()
        s = int(Start) - 9
        e = int(End) - 9
        for i in range(s, e):
            Rooms[Name][i] = False

    neg = True
    for R in Rooms:
        if neg:
            neg = False
        else:
            print("-----")
        print(f"Room {R}:")
        if any(Rooms[R]) == False:
            print("Not available")
        else:
            print_room_cond(Rooms[R])
    return


if __name__ == "__main__":
    solve()
