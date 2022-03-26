#https://www.acmicpc.net/problem/2166
#신발끈 공식 활용
import sys
input = sys.stdin.readline

N = int(input())
input_array = []
temp = 0

for i in range(N):
    input_array.append(list(map(int,input().split())))
input_array.append(input_array[0])


for i in range(N):
    temp+=input_array[i][0]*input_array[i+1][1]
    temp-=input_array[i][1]*input_array[i+1][0]

print('%.1f'%(abs(temp)/2))