T = int(input())
ans = []
for i in range(T):
    w, h = map(int, input().split()) 
    ans.append((w,h))

for i in range(T):
    count = 1
    for j in range(T):
        if i != j:
            if ans[i][0] < ans[j][0] and ans[i][1] < ans[j][1]:
                count = count +1
    print(count)
