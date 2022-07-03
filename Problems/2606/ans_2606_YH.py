#https://www.acmicpc.net/problem/2606
from collections import deque

def bfs(node, graph, visited):
    queue = deque([node])
    visited[node] = True
    cnt = 0

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
                cnt+=1
    return cnt

def solve():
    n = int(input())
    m = int(input())
    graph = {}
    for _ in range(m):
        a,b =map(int, input().split())
        if a not in graph:
            graph[a] = [b]
        else:
            graph[a].append(b)
        if b not in graph:
            graph[b] = [a]
        else:
            graph[b].append(a)
    print(graph)
    visited = [False]*(n+1)
    print(bfs(1, graph, visited))

    return

if __name__ == "__main__":
    solve()