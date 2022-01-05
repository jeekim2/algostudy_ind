# https://www.acmicpc.net/problem/1991
# 2022-01-04 : 오늘 야근으로 인한 draft commit
# 2022-01-05 : 발전이 없네...후... 재귀 input과 return 값을 못 구하겠군..
import sys

def solve():
    input = sys.stdin.readline
    global N
    global result
    global nodes
    N = int(input())
    nodes = []
    result = []
    for _ in range(N):
        a,b,c = input().split()
        nodes.insert(a,b,c) # root : 1st index, left : 2*index + 1, right : 2*index + 2
    binary_tree()

def binary_tree(idx):
    result.append(root)
    for x in nodes:
        if x[0] == left:
           return binary_tree(x, mode)



