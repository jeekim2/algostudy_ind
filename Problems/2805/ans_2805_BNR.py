# https://www.acmicpc.net/problem/2805

# 나무 자르기, 이분 탐색
# N개의 나무, M미터 필요, H의 최댓값

from pickle import FALSE, TRUE
import sys

class refSys: #function overriding, 이 함수 호출이 많아야 편한듯...?
    def funcInput(self):
        result = sys.stdin.readline().split() 
        return result
Defobj = refSys()

def check(tree_list,mid,M): #자른 나무가 충분하면 TRUE, 아니면 FALSE
    dum = 0
    for i in tree_list:
        if i > mid:
            dum += i-mid
        else:
            continue
    if dum >= M:
        return TRUE
    else:
        return FALSE

def bs(tree_list, M):
    left = 1
    right = max(tree_list)

    while left <= right:
        mid = (left+right)//2
        
        if check(tree_list,mid,M) == TRUE: #나무가 충분하니 최대 높이를 늘려가
            left = mid + 1
        else: 
            right = mid - 1
            result = right
    return result

def solve():
    N, M = map(int, Defobj.funcInput())   #N개 나무, M 필요
    tree = list(map(int, Defobj.funcInput()))
    print(bs(tree, M))

if __name__ == "__main__":
    solve()