# https://www.acmicpc.net/problem/9251

import sys


def checkLCS(startIdxSrc, startIdxTar):
    global src, tar
    global maxVals
    if (startIdxSrc, startIdxTar) in maxVals:
        # memoization return
        return maxVals[(startIdxSrc, startIdxTar)]
    if startIdxTar == len(tar) or startIdxSrc == len(src):
        return 0
    findIdx = tar[startIdxTar:].find(src[startIdxSrc])
    if findIdx == -1:
        maxVals[(startIdxSrc, startIdxTar)] = checkLCS(startIdxSrc + 1, startIdxTar)
    else:
        # startIdxSrc의 문자열을 찾았을 경우,
        # 해당 문자를 포함시켜서 처리
        notIgnoreThis = 1 + checkLCS(startIdxSrc + 1, startIdxTar + findIdx + 1)
        # 해당 문자를 무시하고 처리 (찾지 못한 경우와 같음)
        ignoreThis = checkLCS(startIdxSrc + 1, startIdxTar)
        # TC 2번에서, source 첫번째 D 문자로 target 마지막 D 문자를 "찾아버리는" 경우
        # 그 뒤의 문자열은 갯수로 포함되지 않기 때문에, max 처리 하여 ignoreThis 를 사용
        maxVals[(startIdxSrc, startIdxTar)] = max(ignoreThis, notIgnoreThis)
    return maxVals[(startIdxSrc, startIdxTar)]


def solve():
    global src, tar
    global maxVals
    maxVals = {}
    temp1 = input()
    temp2 = input()
    if len(temp1) > len(temp2):
        src = temp2
        tar = temp1
    else:
        src = temp1
        tar = temp2
    maxVals[(-1, -1)] = 0
    for i in range(len(src) - 1, -1, -1):
        for j in range(len(tar) - 1, -1, -1):
            # Dynamic programming by Bottom up
            checkLCS(i, j)

    # for i in range(len(src)):
    #     # TopDown 인 경우 - input이 커질 경우 재귀제한으로 인해 Recursion error 발생 (Input 갯수 1000 by 1000)
    #     checkLCS(i, 0)

    print(max(maxVals.values()))
    return


if __name__ == "__main__":
    solve()
