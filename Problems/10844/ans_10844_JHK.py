# https://www.acmicpc.net/problem/10844


def solve():
    N = int(input())
    if N == 1:
        print(9)
        return
    dic = {}
    # 1의 자리가 해당 key 값으로 끝나는 갯수를, N에 따라 list로 append
    # ex. dic[0] : [1,2,3,4] 라면, 1000자리(N=4) 인 경우 마지막이 0으로 끝나는 계단수는 4개

    dic[0] = [0]
    for i in range(1, 10):
        dic[i] = [1]
    for i in range(1, N):
        dic[0].append(dic[1][i - 1])
        # 마지막이 0이 되게 하는 개수는 N-1자리 계단수에서 마지막이 1인 경우만 가능
        for j in range(1, 9):
            dic[j].append(dic[j - 1][i - 1] + dic[j + 1][i - 1])
            # 마지막이 j가 되게 하는 개수는 N-1자리 계단수에서 마지막이 j-1 혹은 j+1인 경우만 가능
        dic[9].append(dic[8][i - 1])
        # 마지막이 9가 되게 하는 개수는 N-1자리 계단수에서 마지막이 8인 경우만 가능
    sum = 0
    for i in range(10):
        sum += dic[i][-1]
    print(sum % 1000000000)
    return


if __name__ == "__main__":
    solve()
