#https://www.acmicpc.net/problem/2805
import sys

input = sys.stdin.readline

N, M = list(map(int, input().split()))
tree = list(map(int, input().split()))

ans =0
start = 0
end = max(tree)

while end-start>=0:
    sum = 0
    mid = (start+end)//2

    for i in tree:
        if i-mid >0:
            sum = sum + (i-mid)

    if sum >= M:
        ans = mid
        start = mid+1
    else:
        end = mid-1
print(ans)
    


        

