# 일시 : 2021.11.23
# 주제 : Python을 통한 평균 구하기 방법

# 방법 (1). 파이썬 Sum을 이용한 평균 구하기
def avg_method_1(x):
    x_n = len(x)
    result = sum(x) / x_n
    return result


# 방법 (2). for 반복문
def avg_method_2(x):
    x_n = len(x)
    sum_x = 0
    
    for val in x:
        sum_x += val
    result = sum_x / x_n
    return result

# 방법 (3). numpy module 사용
import numpy as np

def avg_method_3(x):
    result = np.mean(x) # float16 result (computed by using float32)
    return result

def avg_method_3_flt32(x):
    result = np.mean(x, dtype=np.float32) # float32
    return result

def avg_method_3_flt64(x):
    result = np.mean(x, dtype=np.float64) # float64
    return result

# 방법 (4). statistics 사용
import statistics

def avg_method_4(x):
    result = statistics.mean(x)
    return result

if __name__ == "__main__":
# (1) single-array 일 경우, 모두 동일함.
    input_x = list(map(int,input().split(',')))
# (2) multi-array일 경우, 결과 달라짐.
#    input_x = np.zeros((2, 512*512), dtype=np.float32)
#    input_x[0,:] = 1
#    input_x[1,:] = 0.1
#    print(input_x)

# 각 방법 Result : 
    print(avg_method_1(input_x))
    print(avg_method_2(input_x))
    print(avg_method_3(input_x))
    print(avg_method_3_flt32(input_x))
    print(avg_method_3_flt64(input_x))
    print(avg_method_4(input_x))