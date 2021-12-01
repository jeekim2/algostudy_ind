# https://www.acmicpc.net/problem/2675

# 문제 : input str(S) -> Repeat R for each str(S[N]) to create new str(P)

def solve():
    test_n = int(input())
    input_list = []
    i = k = 0
    
    while i < test_n:
        input_list.append(input().split(" "))
        i += 1
    
    for j in input_list:
        for letter in j[1]:
            while k < int(j[0]):
                print(letter, end="")
                k += 1
            k = 0
        print() # need for make line change
    
if __name__ == "__main__":
    solve()