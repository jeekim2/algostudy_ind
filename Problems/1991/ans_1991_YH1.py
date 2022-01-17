# https://www.acmicpc.net/problem/1991

import sys

def solve():
    input = sys.stdin.readline
    global N
    global result
    global nodes
    N = int(input())
    nodes = {}
    for _ in range(N):
        a,b,c = map(str,input().split())
        nodes[a] = [b,c] # {root : [left, right]} 형태로 입력

    root = list(nodes.keys()) #root node들의 모임
    for i in range(3):
        result=[]
        binary_tree(root[0],i)
        print("".join(result))

def binary_tree(root, mode):
    if mode == 0: #전위 순회 - root > left > right
        if root != '.':
            result.append(root)
            binary_tree(nodes[root][0],0)
            binary_tree(nodes[root][1],0)
    elif mode == 1: #중위 순회 - left > root > right
        if root != '.':
            binary_tree(nodes[root][0],1)
            result.append(root)
            binary_tree(nodes[root][1],1)
    else: #mode == 2: 후위 순회 - left > right > root
        if root != '.':
            binary_tree(nodes[root][0],2)
            binary_tree(nodes[root][1],2)
            result.append(root)

if __name__ == "__main__":
    solve()

    



