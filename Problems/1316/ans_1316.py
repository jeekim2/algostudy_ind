# https://www.acmicpc.net/problem/1316

import sys


def solve():
    N = int(input())
    Words = []
    for _ in range(N):
        Words.append(input())

    ans = 0
    for word in Words:
        dic = {}
        groupWord = True
        for idx, char in enumerate(word):
            if dic.get(char) == None:
                dic[char] = idx
            else:
                if dic[char] + 1 != idx:
                    groupWord = False
                else:
                    dic[char] = idx

        if groupWord:
            ans += 1

    print(ans)


if __name__ == "__main__":
    solve()
