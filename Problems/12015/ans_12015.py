#https://www.acmicpc.net/problem/12015
#LIS = Longest increasing subsequence
#배열에 대한 순차적 LIS를 구함
#LIS의 최대값보다 작은 값 x가 들어오면
# LIS[i-1]<k<=LIS[i] 를 찾고  LIS[i]=k로 대체

N = int(input())
A = list(map(int,input().split()))
LIS = [A[0]] #LIS 초기값

def binsearch(LIS, len, result): #0부터 시작이기 때문에 high고정/ low 증가 
    low = 0
    high = len-1

    while high-low >0:
        mid = (high+low)//2
        if LIS[mid]>=result:
            high = mid
        else:
            low = mid+1
    LIS[high] = result

for i in range(1,N): #A에 대한 비교시작
    if LIS[-1]> A[i]:
        binsearch(LIS, len(LIS), A[i])
    elif LIS[-1]==A[i]:
        continue
    else:
        LIS.append(A[i])

print(len(LIS))
