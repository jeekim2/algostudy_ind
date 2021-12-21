# https://www.acmicpc.net/problem/15650
# 문제 : 1~N까지의 숫자 중 M개의 수열을 오름차순으로 표출
# 입력 : N, M
# 출력 : 중복되지 않는 M개의 수열

def search2(dep,idx,N,M):
    global check
    global result
    
    if dep == M:
        for i in range(M):
            print(' '.join(map(str,result)))
    elif N == M :
        for i in range(idx,N):
            result.append(i+1)
        print(' '.join(map(str,result)))
    else:
        for i in range(idx,N):
            if check[i] == True:
                continue
            else:
                check[i] = True
                result.append(i+1)
                search2(dep+1,idx+1,N,M)
                check[i] = False
                result.pop()

def solve():
    global check
    global result
    
    N,M = map(int,input().split())
    check = [False]*N
    result = []
    
    search2(0,0,N,M)

if __name__ == "__main__":
    solve()