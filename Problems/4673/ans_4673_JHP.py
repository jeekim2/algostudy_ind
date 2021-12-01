# https://www.acmicpc.net/problem/4673

# 문제 : Self-Numbers
# (e.g) 33 = 33 + 3 + 3 = 39 = 39 + 3 + 9 = ...

def d(x):
    result = x
    for i in str(x): # str(15) = ['1','5']
        result += int(i)
    return result

def find_self_num():
    all_num = list(range(1,10001))
    non_self_num = []

    for i in range(1, 10001):
        non_self_num.append(d(i)) # d(n)에 대한 함수 구성
    
    for i in range(1, 10001):
        if i in non_self_num:
            pass
        else:
            print(i)
    
if __name__ == "__main__":
    find_self_num()