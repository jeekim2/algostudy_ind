# https://www.acmicpc.net/problem/4344
# 문제 : 자신이 반에서 평균은 넘는다는 생각에 대해 결과를 알려줘야 함.

# import numpy

def the_truth_is():
    C = int(input())
    
    for i in range(C):
        N = list(map(int,input().split(" ")))
        cnt = N.pop(0)
        avr_score = sum(N)/cnt
        avg_cnt, avr_percent = 0, 0.0
    
        for j in N:
            if j > avr_score:
                avg_cnt = avg_cnt + 1
        avr_percent = avg_cnt / cnt * 100
        
        # print(round(avr_percent,3),"%") # round(num,소수점) -> 40.0% 표기
        print("{:.3f}".format(avr_percent),"%", sep='') # "{:.소수점f}".format(num) -> 40.000% 표기
#        i += 1

if __name__ == "__main__":
    the_truth_is()