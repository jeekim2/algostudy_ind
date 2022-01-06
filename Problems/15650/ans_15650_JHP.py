# https://www.acmicpc.net/problem/15650
# 문제 : 1~N까지의 숫자 중 M개의 수열을 오름차순으로 표출
# 입력 : N, M
# 출력 : 1~N까지 중복되지 않는 M개를 고른 수열 출력

# 접근방법 : 15649에서 시작시점을 추가하여 depth를 설정하는 컨셉 추가 필요

def dfs(idx,start,N,M):
    global check
    global result
    
    if idx == M:
        print(' '.join(map(str,result)))
    else:
        for i in range(start,N+1):
            if check[i] == True:
                continue
            else:
                check[i] = True     # 사용한 숫자 check
                result[idx] = i     # 해당 index에 i 값 저장
                dfs(idx+1,i+1,N,M)  # 재귀로 시작점부터 다시 오름차순 확인
                check[i] = False

def solve():
    global check
    global result
    
    N,M = map(int,input().split())
    check = [False]*(N+1)
    result = [0]*M
    
    dfs(0,1,N,M)

if __name__ == "__main__":
    solve()