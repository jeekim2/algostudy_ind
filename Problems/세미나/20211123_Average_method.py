# 일시 : 2021.11.23
# 주제 : Python을 통한 평균 구하기 방법
# https://blog.naver.com/pmw9440/221373863065
# https://blockdmask.tistory.com/559 
# https://blog.naver.com/youndok/222205066435

# -------------------------------------------------------------------------
# 방법 (1). 파이썬 Sum을 이용한 평균 구하기
def avg_method_1(x):
    x_n = len(x)
    result = sum(x) / x_n
    return result

def avg_method_1_arr(x):
    x_n = len(x[:,0])
    x_c = len(x[0,:])
    result_n = np.zeros(x_n)
    result_c = np.zeros(x_c)
    i=j=0
    sum_x = sum_y = 0
    
    # row 평균 구하기
    while i < x_n:
        for val in x[i,:]:
            sum_x += val
        result_n[i] = sum_x/len(x[i,:])
        sum_x = 0
        i += 1
    # colum 평균 구하기
    while j < x_c:
        for val in x[:,j]:
            sum_y += val
        result_c[j] = sum_y/len(x[:,j])
        sum_y = 0
        j += 1        
    return result_n, result_c

# -------------------------------------------------------------------------
# 방법 (2). for 반복문
def avg_method_2(x):
    x_n = len(x)
    sum_x = 0
    
    for val in x:
        sum_x += val
    result = sum_x / x_n
    return result

# -------------------------------------------------------------------------
# 방법 (3). numpy module 사용 - 산술평균(arithmetic mean)
# Sum / number - 계산 방식
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

def avg_method_3_arr(x):
    n_result = np.array(x) #
    result = n_result.mean() # total 평균
#    result = n_result.mean(axis=0) # axis=0(column), axis=1(row)별 평균
    return result

# -------------------------------------------------------------------------
# 방법 (4). statistics 사용
import statistics

def avg_method_4(x):
    result = statistics.mean(x)
#    result = statistics.median(x)
    return result

def avg_method_4_arr(x):
    x_n = len(x[:,0])
    x_c = len(x[0,:])
    result_n = np.zeros(x_n)
    result_c = np.zeros(x_c)
    i=j=0
    sum_x = sum_y = 0
    
    # row 평균 구하기
    while i < x_n:
        result_n[i] = statistics.mean(x[i,:])
        i += 1
    # colum 평균 구하기
    while j < x_c:
        result_c[j] = statistics.mean(x[:,j])
        j += 1        
    return result_n, result_c

# -------------------------------------------------------------------------
# Input / Output : 
if __name__ == "__main__":
# (1) single-array 일 경우, 모두 동일함.
    input_x = list(map(int,input().split()))

# (2) multi-array일 경우, 결과 달라짐.
#    input_x = np.zeros((2, 2*2), dtype=np.float32)
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

#    print(avg_method_1_arr(input_x))
#    print(avg_method_3_arr(input_x))    
#    print(avg_method_4_arr(input_x))

# -------------------------------------------------------------------------
# 기타 : Averaging 방법론
# Moving Average : https://wendys.tistory.com/178 
# VAMA (Volume Adjusted Moving Average) : https://blog.naver.com/breezehome50/222342190125

