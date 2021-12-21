# https://www.acmicpc.net/problem/8958

# 문제 : OX퀴즈 결과에 대한 점수 구하기
# input : Test case 숫자(N) & OX 정답 결과 
# output : 점수 (O가 연속적으로 나오면 점수는 중첩)

import sys

def score_result():
    input = sys.stdin.readline
    n_test = int(input())
    sc_result = []
    
    for n in range(0,n_test):
        sc_test = str(input())
        result = []
        sc_result.append(0)

        for i in range(0,len(sc_test)-1):
            result.append(-1)
            if i == 0:
                if sc_test[i] == 'O':
                    result[i] = 1
                else:
                    result[i] = 0
            elif sc_test[i] == 'O':
                result[i] = 1
                if sc_test[i-1] == sc_test[i]:
                    result[i] = result[i-1] + 1
            else:
                result[i] = 0
        sc_result[n] = sum(result)
    
    for val in sc_result:
        print(val)
    
if __name__ == "__main__":
    score_result()