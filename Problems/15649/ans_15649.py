def search(k, arr, is_not_visited):
    if k == M:
        for i in range(M):
            print(arr[i], end=" ")
        print()
        return
    for i in range(N):
        if is_not_visited[i]:
            arr[k] = i + 1
            is_not_visited[i] = False
            search(k + 1, arr, is_not_visited)
            is_not_visited[i] = True


def solve():
    # solved by recursion function
    global N
    global M
    # global is_not_visited
    # global arr
    N, M = map(int, input().split())
    is_not_visited = [True for _ in range(N)]
    arr = [0 for _ in range(M)]

    search(0, arr, is_not_visited)


if __name__ == "__main__":
    solve()
