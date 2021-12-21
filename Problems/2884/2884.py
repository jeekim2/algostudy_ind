"""
Name: Bitnuri Kim
Problem: 2884

https://www.acmicpc.net/problem/2884

첫째 줄에 두 정수 H와 M이 주어진다. (0 ≤ H ≤ 23, 0 ≤ M ≤ 59) 그리고 이것은 현재 상근이가 설정한 놓은 알람 시간 H시 M분을 의미한다.
입력 시간은 24시간 표현을 사용한다. 24시간 표현에서 하루의 시작은 0:0(자정)이고, 끝은 23:59(다음날 자정 1분 전)이다. 

설정해야 하는 알람 시간을 출력
"""

#Hour = int(input("시간 입력하세요. H \n"))
#Min = int(input("분 입력하세요. M \n"))

Hour, Min = map(int, input("시간을 입력하세요").split(' '))

if Min >= 45:
    Min = Min - 45
else:
    Min = Min + 60 - 45
    if Hour == 0:
        Hour = 23
    else:
        Hour = Hour - 1

print("알람은", Hour,"시", Min, "분에 울립니다.")
