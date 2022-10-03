# https://softeer.ai/practice/info.do?idx=1&eid=804

import sys


def get_alpha_id(c):
    if ord(c) < ord("J"):
        id = ord(c) - ord("A")
    else:
        id = ord(c) - ord("A") - 1
    return id


def get_alpha(i):
    if i < ord("J") - ord("A"):
        return chr(i + ord("A"))
    return chr(i + ord("A") + 1)


def get_x_y(idx):
    return idx // 5, idx % 5


def get_idx(x, y):
    return ((x % 5) * 5) + (y % 5)


def solve():
    input = sys.stdin.readline
    MSG = input().rstrip()
    KEY = input().rstrip()
    KeyTable = [-1] * 25
    # input = Alpha / Output = idx
    idx = 0
    for k in KEY:
        if KeyTable[get_alpha_id(k)] == -1:
            KeyTable[get_alpha_id(k)] = idx
            idx += 1
    for i in range(len(KeyTable)):
        if KeyTable[i] == -1:
            KeyTable[i] = idx
            idx += 1

    AlphaTable = [-1] * 25
    # Input = idx / Output = Alpha
    for i in range(25):
        AlphaTable[KeyTable[i]] = i

    i = 0
    Fixed = []
    while i < len(MSG) - 1:
        if MSG[i] == MSG[i + 1]:
            if MSG[i] == "X":
                Fixed.append(get_alpha_id(MSG[i]))
                Fixed.append(get_alpha_id("Q"))
                i += 1
                continue
            else:
                Fixed.append(get_alpha_id(MSG[i]))
                Fixed.append(get_alpha_id("X"))
                i += 1
                continue
        else:
            Fixed.append(get_alpha_id(MSG[i]))
            Fixed.append(get_alpha_id(MSG[i + 1]))
            i += 2
            continue
    if i == len(MSG) - 1:
        Fixed.append(get_alpha_id(MSG[i]))
        # if MSG[i] == "X":
        #     Fixed.append(get_alpha_id("Q"))
        # else:
        Fixed.append(get_alpha_id("X"))

    i = 0
    while i < len(Fixed):
        x1, y1 = get_x_y(KeyTable[Fixed[i]])
        x2, y2 = get_x_y(KeyTable[Fixed[i + 1]])
        if x1 == x2:
            print(get_alpha(AlphaTable[get_idx(x1, y1 + 1)]), end="")
            print(get_alpha(AlphaTable[get_idx(x1, y2 + 1)]), end="")
        elif y1 == y2:
            print(get_alpha(AlphaTable[get_idx(x1 + 1, y1)]), end="")
            print(get_alpha(AlphaTable[get_idx(x2 + 1, y1)]), end="")
        else:
            print(get_alpha(AlphaTable[get_idx(x1, y2)]), end="")
            print(get_alpha(AlphaTable[get_idx(x2, y1)]), end="")
        i += 2
    print()
    return


if __name__ == "__main__":
    solve()
