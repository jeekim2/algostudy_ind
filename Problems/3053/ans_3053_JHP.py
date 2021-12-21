# https://www.acmicpc.net/problem/3053
# 문제 : 택시 기하학
# 입력 : 반지름 R (R<=10,000)
# 출력 : (1) 유클리드 기하학 반지름이 R인 원의 넓이, (2) 택시 기하학 반지름 R인 원의 넓이
# 오차 <=0.0001까지 허용

# 유클리드 기하학 : area of circle = pi()*(r**2)
# 택시 기하학 : d = abs(x1-x2) + abs(y1-y2)

import math

def solve():

    r = float(input())
    pi= math.pi
    
    euclid_area = pi*(r**2)
    taxi_area = 2*(r**2) # x + y = r, area = r**(0.5) * r**(0.5)

    print('%.6f'%(euclid_area))
    print('%.6f'%(taxi_area))
    
if __name__ == "__main__":
    solve()