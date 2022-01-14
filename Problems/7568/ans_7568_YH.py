#https://www.acmicpc.net/problem/7568
#반례가 뭐냐 이거...

import sys
def solve():
    input = sys.stdin.readline
    N = int(input())
    person, Ratings = [], []
    for _ in range(N):
        person.append(list(input().split()))

    for p1 in person:
        rating = 1
        for p2 in person:
            if p1 != p2 :
                if p1[0] < p2[0] and p1[1] < p2[1]:
                    rating+=1
        print(rating, end=" ")
if __name__=="__main__":
    solve()
