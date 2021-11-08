def search2(k):
    if k == M:
        for i in range(M):
            print(arr[i], end=" ")
        print()
        return
    for i in range(N):
        if is_not_visited[i]:
            arr[k] = i + 1
            is_not_visited[0:i] = [False for j in range(i + 1)]
            search2(k + 1)
            is_not_visited[i + 1] = True


def solve():
    global N
    global M
    global is_not_visited
    global arr
    N, M = map(int, input().split())
    is_not_visited = [True for _ in range(N)]
    arr = [0 for _ in range(M)]

    search2(0)


if __name__ == "__main__":
    solve()
