# (Some test cases are failed. Need to update - 2021.11.24)
# https://www.acmicpc.net/problem/1065

# 문제 : 어떤 양의 정수 X의 각 자리가 등차수열이라면 그 수를 "한수"라함.
# 등차수열은 연속된 두개의 수의 차이가 일정한 수열을 말함.
# N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력

def solve():
    num = int(input())
    cnt = 0
    
    for val in range(1,num+1): # num까지 추가하기 위해서는 num + 1로 해야함.
        num_str = str(val)
        if val < 100:
            cnt += 1
        else: 
            for i in range(0,len(num_str)-2):   # index [0]~[2]
                if int(num_str[i]) - int(num_str[i+1]) == int(num_str[i+1])-int(num_str[i+2]):
                    print(num_str[i],i)
                    cnt += 1
    print(cnt)
    
    
if __name__ == "__main__":
    solve()
    
    