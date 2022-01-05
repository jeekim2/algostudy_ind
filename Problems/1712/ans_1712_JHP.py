# https://www.acmicpc.net/problem/1712
# 문제 : 손익분기점 찾기 (A,B,C)
# 입력 : A = 고정비, B = 생산비, C = 판매비용
# 출력 : 손익분기점이 되는 판매량
# 계산식 = C * 판매량 - (A+B*판대량) > 0 = 손익분기점 ==> (C-B)*판매량 - A > 0

def solve():
    A,B,C = map(int,input().split())
    
    if (C-B) <= 0:
        print('-1')
    else:
        result = A//(C-B)+1
        print(result)
    
if __name__ == '__main__':
    solve()