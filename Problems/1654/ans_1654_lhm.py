#https://www.acmicpc.net/problem/1654

K, N =map(int, input().split())
array = []
for i in range(K):
    array.append(int(input()))

high = max(array)
low = 1


while high-low>=0:
    mid = (high+low)//2
    cnt = 0
    for i in array:
        cnt += i//mid

    if cnt<N:
        high = mid-1
    else:
        low = mid+1


print(high)
