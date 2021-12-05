# https://www.acmicpc.net/problem/4344
# 문제 : 시험 성적을 넣고, 본인이 평균을 넘는지 확인

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
        
        # print(round(avr_percent,3),"%") # round((num,소숫점)) -> 40.0%
        print("{:.3f}".format(avr_percent),"%", sep='') # "{:.(소숫점)f}".format(num) -> 40.000% 
#        i += 1

if __name__ == "__main__":
    the_truth_is()