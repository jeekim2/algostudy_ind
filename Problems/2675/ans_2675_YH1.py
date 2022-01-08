#https://www.acmicpc.net/problem/2675

def solve1():
    T = int(input())
    result = []
    for _ in range(T):
        TC = input().split()
        temp = ""
        for s in TC[1]:
            temp += s*int(TC[0])
        result.append(temp)
    print("\n".join(result))

def solve2(): #더 간단히 풀기
    T = int(input())
    for _ in range(T):
        result = ''
        R, S = input().split()
        for s in S:
            result+=s*int(R)
        print(result)

if __name__ == "__main__":
    solve2()
    