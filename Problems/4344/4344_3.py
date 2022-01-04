# https://www.acmicpc.net/problem/4344

'''
첫째 줄에는 테스트 케이스의 개수 C가 주어진다.
둘째 줄부터 각 테스트 케이스마다 학생의 수 N(1 ≤ N ≤ 1000, N은 정수)이 첫 수로 주어지고, 이어서 N명의 점수가 주어진다. 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.

각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째 자리까지 출력한다.
'''

TC_N = int(input("테스트할 개수"))
Score = []
TestList = []

# 평균 이상인 학생 수 리턴
def over(N, List):
    cnt = 0
    for i in List:
        if i > N:
            cnt = cnt + 1
    return cnt

for i in range(0,TC_N):
    avg = 0
    Score = list(map(int,input("학생수, 점수들 입력").split()))
    
    avg = sum(Score[1:])/Score[0]

    Result = over(avg,Score)/Score[0]*100
    print('%0.3f' %Result, "%")

    # TestList.append(Score[1:])

    # for j in range(0,N):
    #     sum = sum + TestList[i][j]

    # avg = sum(TestList[i])/Score[0]

