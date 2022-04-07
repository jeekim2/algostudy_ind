'''
https://www.acmicpc.net/problem/18258

큐
'''
import sys

def solve():
    input = sys.stdin.readline
    N = int(input())
    Q = []
    head = 0    #pop 시간 줄이기 위해 사용, 메모리는 추가됨.
    for _  in range(N):
        req = input().split()
        if req[0] == 'push':
            Q.append(req[1])
        elif req[0] == 'size':
            print(len(Q)-head)
        elif req[0] == 'empty':
            if (len(Q)-head) == 0:
                print('1')
            else:
                print('0')
        elif (len(Q)-head) == 0:
            print('-1')
        else:
            if req[0] == 'front':
                print(Q[head])
            elif req[0] == 'back':
                print(Q[-1])
            elif req[0] == 'pop':
                print(Q[head])
                head += 1

if __name__ == "__main__":
    solve()