#https://www.acmicpc.net/problem/5585
import sys
input = sys.stdin.readline

N = int(input())
cal_Result = 1000-N
cnt = 0
while cal_Result>0:
    if cal_Result>=500:
        cal_Result-=500
        cnt+=1
    elif cal_Result>=100:
        cal_Result-=100
        cnt+=1
    elif cal_Result>=50:
        cal_Result-=50
        cnt+=1
    elif cal_Result>=10:
        cal_Result-=10
        cnt+=1
    elif cal_Result>=5:
        cal_Result-=5
        cnt+=1
    elif cal_Result>=1:
        cal_Result-=1
        cnt+=1

print(cnt)     
