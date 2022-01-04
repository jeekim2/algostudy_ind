# https://www.acmicpc.net/problem/1904

# A1 = 1  # 1
# A2 = 2  # 00 11
# A3 = 3  # 001 111 / 100
# A4 = 5  # 0011 1111 1001 / 0000 1100
# A5 = 8  # 00111 10011 11001 11111 / 00100 10000 11100 00001
# An = An-1(+1) + An-2(+00)
# 피보나치 수열을 따르게 됨.


def solve():
    N = int(input())
    inputA = 1
    inputB = 2
    if N == 1:
        print(inputA)
        return
    if N == 2:
        print(inputB)
        return
    for _ in range(N - 2):
        outputC = (inputA + inputB) % 15746
        inputA = inputB
        inputB = outputC
    print(outputC)
    return


if __name__ == "__main__":
    solve()
