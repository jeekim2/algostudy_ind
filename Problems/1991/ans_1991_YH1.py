# https://www.acmicpc.net/problem/1991
# 2022-01-04 : 오늘 야근으로 인한 draft commit
# 2022-01-05 : 발전이 없네...후... 재귀 input과 return 값을 못 구하겠군..
# 2022-01-06 : 입력부터 난제... 문자 중복 제외하는 것도 난제...
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
        a,b,c = map(str,input().split())
        nodes.append(a) # root : 1st index, left : 2*index + 1, right : 2*index + 2
        nodes.append(b)
        nodes.append(c)
    binary_tree(0)
    print(result)

def binary_tree(idx):
    left, right = 2*idx+1, 2*idx+2
    if len(result) == N : return
    #전위순회
    result.append(nodes[idx])
    if left <= N and nodes[left] != '.': return binary_tree(left)
    if right <= N and nodes[right] != '.': return binary_tree(right)

if __name__ == "__main__":
    solve()

    



