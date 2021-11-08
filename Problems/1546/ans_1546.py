def solve():
    num = int(input())
    score = list(map(int, input().split()))
    score_sum = 0
    max_score = 0

    for i in score:
        score_sum += int(i)
        if int(i) > max_score:
            max_score = int(i)

    avg = score_sum / max_score * 100 / num

    print(avg)


if __name__ == "__main__":
    solve()
