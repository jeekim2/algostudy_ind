# https://www.acmicpc.net/problem/10818

# 문제 : N개의 정수가 주어지고, 최솟값과 최댓값 구하기

def find_min_max():
    num_max = int(input())
    num_val = list(map(int,input().split()))
    
    num_val.sort() # default min = first, max = last
    max_val = num_val.pop(-1)
    min_val = num_val.pop(0)
    print(min_val, max_val)
    
if __name__ == "__main__":
    find_min_max()