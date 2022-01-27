#https://www.acmicpc.net/problem/1904

N = int(input())
result = [0,1,2]

# for i in range(3,N+1):        #메모리 초과 에러 발생.. 나눈 값을 미리 배열에 저장
#     result.append(result[i-2] + result[i-1])
# print(result[N]%15746)

for i in range(3,N+1):
    result.append((result[i-2] + result[i-1])%15746)
print(result[N])