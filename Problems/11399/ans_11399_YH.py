#https://www.acmicpc.net/problem/11399
def selection_sort(arr):
    for i in range(len(arr)-1):
        minIdx = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[minIdx]:
                minIdx = j
        arr[i], arr[minIdx] = arr[minIdx], arr[i] 
    return arr

def solve():
    N = int(input())
    Withdraw_Time = list(map(int, input().split()))
    # Withdraw_Time.sort()
    Withdraw_Time = selection_sort(Withdraw_Time)
    cnt = 1
    temp = 0
    while True:
        if cnt == (N+1) :
            break
        for i in range(cnt):
            temp+=Withdraw_Time[i]
        cnt+=1
    return print(temp)

if __name__ == "__main__":
    solve()