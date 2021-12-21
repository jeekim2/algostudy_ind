#https://www.acmicpc.net/problem/2750

def solve():
    num_size = int(input())
    num_list = []
    for i in range(num_size):
        num_list.append(input())
    num_list = list(map(int, num_list))
    
    for i in range(len(num_list)-1):
        for j in range(i+1,len(num_list)):
            if num_list[i] > num_list[j]: #중복되는 경우가 있다면?
                num_list[i],num_list[j] = num_list[j], num_list[i]
    return print(num_list, end="")               
    
if __name__ == "__main__":
    solve()