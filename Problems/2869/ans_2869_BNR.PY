"""
https://www.acmicpc.net/problem/2775

문제 : V미터인 나무 오르는데 걸리는 시간 출력
입력 : 낮 = A미터, 밤 = -B미터, 나무 길이 = V
"""

A, B, V = map(int, input().split())

# max = V//(A-B)
# if V%(A-B) !=0:
#     max = max +1
# for n in range(1, max+1):
 
#     if n == 1:
#         temp = V - A
#     else:
#         temp = temp - A
#     if temp <= 0:
#         break
#     else:
#         temp = temp +B


n = (V-A)//(A-B)
r = (V-A)%(A-B)
if r == 0:
    ti = n + 1
else:
    ti = n + 2
print(ti)    