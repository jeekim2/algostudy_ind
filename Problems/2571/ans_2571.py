#https://www.acmicpc.net/problem/2751
""" input() vs sys.stdin.readline()
input() 내장 함수는 parameter로 prompt message를 받을 수 있다. 
따라서 입력받기 전 prompt message를 출력해야 한다. 
물론 prompt message가 없는 경우도 있지만, 이 경우도 약간의 부하로 작용할 수 있다. 
하지만, sys.stdin.readline()은 prompt message를 인수로 받지 않는다.
또한, input() 내장 함수는 입력받은 값의 개행 문자를 삭제시켜서 리턴한다. 
즉 입력받은 문자열에 rstrip() 함수를 적용시켜서 리턴한다. 
반면에 sys.stdin.readline()은 개행 문자를 포함한 값을 리턴한다. 
결론적으로 input() 내장 함수는 sys.stdin.readline()과 비교해서 prompt message를 출력하고, 
개행 문자를 삭제한 값을 리턴하기 때문에 느리다.
"""
import sys

#시간 초과
def solve():
    N = int(sys.stdin.readline().strip())
    num_list=[]
    while len(num_list)< N:        
        num_list.append(int(sys.stdin.readline().strip()))
    
    for i in range(len(num_list)-1):
        for j in range(i+1, len(num_list)):
            if num_list[i] > num_list[j]:
                num_list[i], num_list[j] = num_list[j], num_list[i]
    for x in num_list : 
        print(x)

if __name__ == "__main__":
    solve()
    