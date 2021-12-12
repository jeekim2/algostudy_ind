# https://www.acmicpc.net/problem/15649

# ---------------------------------------------------------------------
# 알고리즘 - 백트래킹(Back-Tracking)
# 정의 : 해를 찾는 도중 해가 아니어서 막히면, 되돌아가서 다시 해를 찾는 기법
# 참고 자료 : https://chanhuiseok.github.io/posts/algo-23/
# (1) 불필요한 부분을 쳐내고, 반복문의 횟수를 줄일 수 있어 효율적 
# (2) N!의 경우의 수를 가진 뭄제에서는 최악의 경우 지수함수 시간을 필요함.
# (3) 모든 경우의 수를 탐색하는 과정에서 조건문 등을 걸어 불필요한 부분 제거 
# 즉, 얼마만큼 가지치기를 잘하느냐에 따라 효율성이 결정

# 백트래킹 접근 방식 : 
# (1) DFS 수행 - 깊이 우선탐색인 DFS를 수행하여 노드 탐색
# (2) 유망한 노드 검토 - 방문한 노드를 포함해서 유망한 노드이면 서브트리로 이동, 아니면 백트래킹 수행
# (3) 서브트리 이동 - 방문한 노드의 하위 노드로 이동하여 다시 재귀를 통해 DFS 수행
# (4) 백트래킹 수행 -방문한 노드를 가지치기하고 사우이 노드로 백트래킹한 후 DFS를 다시 수행

# ---------------------------------------------------------------------
# 문제 : 자연수 N과 M이 주어졌을 때 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열을 모두 구하기
# 입력 : N, M (M <= N)
# 출력 : 한 줄에 문제의 조건을 만족하는 수열 사전 순서대로 출력 (중복 수열 출력 금지)

def find_num(idx,N,M):
    global check
    global result
    
    if idx == M:  # index가 M개가 되는 순간 수열 완료
        for i in range(M):
            print(result[i], end=' ')
        print()
        return
    else :
        for i in range(1,N+1):
            if check[i] == True: # 이미 사용된 숫자일 경우, 다음 i 확인
                continue
            else:
                check[i] = True # 사용한 숫자 check 하기
                result[idx] = i # 수열 저장
                find_num(idx+1,N,M) # 재귀로, 다음 숫자 선택
                check[i] = False
        # for 부모 노드가 가진 자식 노드:
        # if 유망한가:
        #     if 해결책 있나:
        #         해결책 제시
        #     elif 없으면:
        #         find_num() - 재귀

def solve_1():
    global check
    global result
    
    N, M = map(int,input().split())
    check = [False]*(N+1)
    result = [0]*M
    
    find_num(0,N,M)

# 인터넷에서 찾아본 library 활용법 : Back-tracking 알고리즘 공부에는 도움 X
from itertools import permutations
def solve_2():
    N, M = map(int,input().split())
    num = list(range(1,N+1))
    k = list(permutations(num,M))
    
    for i in k:
        print(' '.join(map(str,i)))

if __name__ == '__main__':
    solve_1() # 일반적인 Back-Tracking 방법
    solve_2() # permutations module 사용하는 방법