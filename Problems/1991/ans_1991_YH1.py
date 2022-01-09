# https://www.acmicpc.net/problem/1991
# 2022-01-04 : 오늘 야근으로 인한 draft commit
# 2022-01-05 : 발전이 없네...후... 재귀 input과 return 값을 못 구하겠군..
# 2022-01-06 : 입력부터 난제... 문자 중복 제외하는 것도 난제...
# 2022-01-07 : 생략...

import sys

def solve():
    input = sys.stdin.readline
    global N
    global result
    global nodes
    N = int(input())
    nodes, result = [], []
    for _ in range(N):
        temp = list(map(str,input().split()))
        for x in temp:
            nodes.append(x)
    #3n : root, 3n+1 : left, 3n+2 : right
    print(nodes)
    binary_tree1(0)
    print(result)

def binary_tree1(idx): #전위 순회
    if (3*idx+1 > 3*N or 3*idx+2 > 3*N) : return
    if idx == 0: 
        result.append(nodes[3*idx])
    if nodes[3*idx+1] !='.':
        result.append(nodes[3*idx+1])
        binary_tree1(3*idx+1)
    if nodes[3*idx+2] !='.':
        result.append(nodes[3*idx+2])
        binary_tree1(3*idx+2)

if __name__ == "__main__":
    solve()

    



