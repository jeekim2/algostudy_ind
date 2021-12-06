# https://www.acmicpc.net/problem/8958
'''
첫째 줄에 테스트 케이스의 개수가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 길이가 0보다 크고 80보다 작은 문자열이 주어진다. 문자열은 O와 X만으로 이루어져 있다.
OOXXOXXOOO"와 같은 OX퀴즈의 결과가 있다. O는 문제를 맞은 것이고, X는 문제를 틀린 것이다. 문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수가 된다.
"OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점이다.

각 테스트 케이스마다 점수를 출력한다.
'''

Num = int(input("TC 개수"))
TC = []

for i in range(0, Num):
    TC = input("OX입력")
    score = 0
    Total = 0
    for j in TC:
        if j == 'O':
            score = score + 1
        else:
            score = 0
        Total = Total + score
    print(Total)



