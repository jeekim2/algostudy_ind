# https://www.acmicpc.net/problem/1110

# 입력 : 0~99 사이의 정수 (0 < N < 99)
# 출력 : N의 사이크 길이 출력

def sum_up():
    N = new_num = int(input())
    cnt = 0
    
    while True:
        sum_num = new_num//10 + new_num%10 # 10의 자리 + 1의 자리
        new_num = int(new_num%10)*10 + int(sum_num%10)
        # new_num = int(str(new_num%10) + str(sum_num%10))
        cnt = cnt + 1
        if (new_num == N):
            break
    print(cnt)

if __name__ == "__main__":
    sum_up()