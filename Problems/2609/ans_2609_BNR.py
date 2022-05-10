'''
https://www.acmicpc.net/problem/2609

'''
import sys


def solve():
    input = sys.stdin.readline
    A, B = map(int, input().split())
    if A>B:
        big = A
        small = B
    else:
        big = B
        small = A

    while small != 0:
        big = big%small
        big,small = small,big
    GCD = big
    print(GCD)
    print(A*B//GCD)

if __name__ == "__main__":
    solve()