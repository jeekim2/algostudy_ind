# https://www.acmicpc.net/problem/2775

# 문제 : V미터인 나무 오르는데 걸리는 시간 출력
# 입력 : 낮 = A미터, 밤 = -B미터, 나무 길이 = V

def solve():
    A,B,V = list(map(int,input().split()))

    # (1) 반복문 구현 시, 시간 초과 에러 발생
    # temp = 0
    # day_mov = 1
    # while temp <= V:
    #     temp = (A-B)*day_mov
    #     if V-temp > A:
    #         day_mov += 1
    #     else:
    #         day_mov += 1
    #         break
    
    # (2) 나누기 방법으로 구현 하기
    if (V-A)%(A-B) == 0:
        day_mov = (V-A)//(A-B) + 1
    else:
        day_mov = (V-A)//(A-B) + 2

    print(day_mov)


if __name__ == "__main__":
    solve()

# 2 1 5 -> 4
# 5 1 6 -> 2
# 100 99 1000000000 -> 999999901
