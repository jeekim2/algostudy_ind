# https://www.acmicpc.net/problem/2675

'''
첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)가 주어진다. 각 테스트 케이스는 반복 횟수 R(1 ≤ R ≤ 8), 문자열 S가 공백으로 구분되어 주어진다. S의 길이는 적어도 1이며, 20글자를 넘지 않는다. 

각 테스트 케이스에 대해 P를 출력한다.
'''



TCNum = int(input())
TC = []

for i in range(TCNum):
    TC.append(input())
    # print(TC)

for i in range(TCNum):
    for j in range(len(TC[i][2:])):
        print(TC[i][j+2]*int(TC[i][0]), end="")