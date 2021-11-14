# 문제 : 정수 A,B를 입력 받아 A/B를 출력

def solve():
    # A,B = map(int,input().split(" "))
    A,B = map(float,input().split(" "))
    if A > 0 and B < 10:
        print(A/B)
    else:
        print("wrong input")

if __name__ == "__main__":
    solve()