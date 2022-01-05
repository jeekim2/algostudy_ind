#https://www.acmicpc.net/problem/2805

def solve():
    N, M = map(int, input().split())
    tree_group = list(map(int, input().split()))
    # left = min(tree_group) # 모든 나무가 똑같은 높이일 때 문제 발생.
    left = 0
    right = max(tree_group)
    result=[]
    
    while (left <= right):
        sum = 0
        mid = (left+right)//2
        for x in tree_group:
            if x > mid:
                sum+=(x-mid)
        if sum >= M :
            result.append(mid) #HINT : "적어도 M이상의 나무길이"
            left = mid+1
        else :
            right = mid-1
    print(max(result))
    
def solve_fail():
    # 문제 이해를 잘못 
    # - 적어도 M이상이기 때문에 나무의 길이가 M보다 길어도 된다는 것을 간과함.
    # - 아래 풀이는 나무의 길이가 딱 M인 경우를 구하는 방법.
    N, M = map(int, input().split())
    tree_group = list(map(int, input().split()))
    left = 0
    right = max(tree_group)
    
    while (left <= right):
        sum = 0
        mid = (left+right)//2
        for x in tree_group:
            if x > mid:
                sum+=(x-mid)
        if sum > M :
            left = mid+1
        elif sum < M :
            right = mid-1
        else:
            break

    print(mid)

if __name__=="__main__":
    solve()
    