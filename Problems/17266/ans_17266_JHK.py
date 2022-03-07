# https://www.acmicpc.net/problem/17266


def solve():
    # Binary search 문제인데 그냥 풀릴거 같아서 해보니 됨.
    # Python류 풀이 3등 개꿀
    N = int(input())
    M = int(input())
    Points = list(map(int, input().split()))
    HalfGap = [0]
    # 최종 print max 문에서 M==1인 경우 error 방지를 위해 0을 넣어둠.
    for i in range(1, len(Points)):
        HalfGap.append((Points[i] - Points[i - 1] + 1) // 2)
        # 가로등 사이는 각 가로등이 절반(거리가 홀수인 경우 올림)만 커버하면 됨.
    FirstGap = Points[0]
    LastGap = N - Points[-1]
    # 양 끝은 온전히 한 가로등이 커버
    print(max(FirstGap, LastGap, max(HalfGap)))
    return


if __name__ == "__main__":
    solve()
