# https://www.acmicpc.net/problem/10828

def solve():
    N = int(input())
    words = []
    result = []
    
    for _ in range(N):
        words.append(list(input().split()))
    
    for i in range(N):
        # push
        if words[i][0] == 'push':
            result.append(words[i][1])
            
        # pop
        elif words[i][0] == 'pop':
            if len(result) == 0:
                print('-1')
            else:
                print(result[-1])
                result.pop(-1)
                
        # size
        elif words[i][0] == 'size':
            print(len(result))
            
        # empty
        elif words[i][0] == "empty":
            if len(result) == 0:
                print('1')
            else:
                print('0')
                
        # top
        elif words[i][0] == 'top':
            if len(result) == 0:
                print('-1')
            else:
                print(result[-1])

if __name__ == "__main__":
    solve()
