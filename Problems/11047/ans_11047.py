def solve():
    N, K = map(int, input().split())
    coins = []
    for _ in range(N):
        coins.append(int(input()))
    coins.reverse()  # ascending input by problem condition
    cnt = 0
    for c in coins:
        # 반복문으로 counting 시 시간복잡도 O(N)
        c_cnt = K // c
        cnt += c_cnt
        K -= c * c_cnt
    print(cnt)


if __name__ == "__main__":
    solve()
