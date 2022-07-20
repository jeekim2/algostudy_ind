# https://www.acmicpc.net/problem/1747


from operator import is_


def is_Pallendrom(num):
    strNum = str(num)
    for i in range(len(strNum)):
        if strNum[i] != strNum[-1 - i]:
            return False
    return True


def solve():
    PrimeMax = 1003002
    N = int(input())
    if N <= 2:
        print(2)
        return
    Num = 2
    for Num in range(2, PrimeMax):
        is_Prime = True
        for i in range(2, int(Num**0.5) + 1):
            if Num % i == 0:
                is_Prime = False
                break
        if is_Prime:
            if Num >= N:
                if is_Pallendrom(Num):
                    print(Num)
                    return
    return


if __name__ == "__main__":
    solve()
