# https://www.acmicpc.net/problem/11053


def cntAscend(startidx):
    global N
    global series
    global dic
    maxVal = 1001
    # 경계값 확인이 중요한 이유... 이거 1000으로 했던걸 겨우 찾음.
    cntList = []
    suspIdx = []
    if dic.get(startidx):
        return dic[startidx]
    for i in range(startidx + 1, N):
        if series[i] > series[startidx] and series[i] < maxVal:
            maxVal = series[i]
            suspIdx.append(i)
    if suspIdx == []:
        dic[startidx] = 1
        return 1
    for s in suspIdx:
        cntList.append(cntAscend(s) + 1)
    dic[startidx] = max(cntList)
    return dic[startidx]


def solve():
    global N
    global series
    global dic
    dic = {}
    cntList = []
    N = int(input())

    series = list(map(int, input().split()))

    for i, v in enumerate(series):
        if v <= series[0]:
            cntList.append(cntAscend(i))

    print(max(cntList))
    return


if __name__ == "__main__":
    solve()
