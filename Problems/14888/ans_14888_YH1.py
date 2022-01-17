#https://www.acmicpc.net/problem/14888

#백트래킹 방식에 대한 생각 틀을 정립해봐야겠다....#
#현재 유망 여부를 따지는 방식으로 For문과 재귀호출 형태로 계속 풀고 있는데,
#아직 접근하는데 시간도 오래 걸리고 복잡하게 접근하고 있다는 생각...
import sys
 
def solve():
    input = sys.stdin.readline
    global operand, operator, n, result, final
    n = int(input())
    result = [] # 연산 과정의 값들 저장
    final = [] # 최종 연산의 결과값들 저장
    operand = list(map(int,input().split())) #피연산자 리스트 입력
    operator = list(map(int,input().split())) #연산자 리스트 입력
    result.append(operand[0]) # 피연산자 초기값 설정
    calc(1)
    print(max(final))
    print(min(final))
    
def calc(idx): # parameter : 연산할 피연산자 위치
    global operand, operator, result, final
    if idx == n: # 모든 피연산자 대입이 완료되면 종료
        final.append(result[-1]) # 연산 중간값들 중 최종값을 연산 결과로 채택
        return 
    else:
        for i in range(len(operator)): 
            # 백트래킹 방식으로 For문과 재귀호출 혼합 형태로 많이 풀고 있는 듯.. 다른 방향은 없는가..?
            temp = 0
            if operator[i] !=0: # 사용할 연산자에 대해 유망한가 Promising 검토
                if i == 0:
                    temp = result[-1]+operand[idx]
                elif i == 1:
                    temp = result[-1]-operand[idx]
                elif i == 2:
                    temp = result[-1]*operand[idx]
                else:
                    if result[-1] < 0: #C++14방식
                        temp = -(abs(result[-1])//operand[idx])
                    else:
                        temp = result[-1]//operand[idx]
                result.append(temp) #연산 결과 정리
                operator[i]-=1 # 연산자 사용함에 따라 Promising reset
                calc(idx+1) # 다음 연산할 피연산자 적용
                operator[i]+=1 # 최종 연산값 추출에 따른 Promising set
                result.pop() # 최종 연산값 추출 후 중간값에 대한 삭제 > 다음 cycle을 위한 조치

if __name__ == "__main__":
    solve()
