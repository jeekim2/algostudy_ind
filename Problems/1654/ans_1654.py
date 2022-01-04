# https://www.acmicpc.net/problem/1654
import sys


def search_lan(ref_lan):
    global Lans
    global K
    sum_num = 0
    for lan in Lans:
        sum_num += lan // ref_lan
    if sum_num >= K:
        return True
    return False


def solve():
    input = sys.stdin.readline
    global Lans
    global K
    N, K = map(int, input().split())
    Lans = []
    for _ in range(N):
        Lans.append(int(input()))

    ref_lan_min = 0
    ref_lan_max = max(Lans) + 1

    while True:
        ref_lan = (ref_lan_min + ref_lan_max) // 2
        if ref_lan == 0:
            print(0)
            return
        ans = search_lan(ref_lan)
        if ref_lan_min + 1 >= ref_lan_max:
            print(ref_lan)
            return
        if ans:
            ref_lan_min = ref_lan
        else:
            ref_lan_max = ref_lan


if __name__ == "__main__":
    solve()
