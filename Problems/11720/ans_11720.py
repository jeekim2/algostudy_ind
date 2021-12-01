# https://www.acmicpc.net/problem/11720

# 문제 : N개의 숫자를 모두 합하여 출력

def solve():
    N_of_num = int(input())
    num = str(input())  # str[index]
    sum_num = i = 0
    
    while i < N_of_num:
        sum_num = sum_num + int(num[i])
        i += 1
     
    print(sum_num)

if __name__ == "__main__":
    solve()