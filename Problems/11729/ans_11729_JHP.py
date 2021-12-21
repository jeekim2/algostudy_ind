# https://www.acmicpc.net/problem/11729
# 문제 : 하노이 탑 이동 순서
# 장대 3개가 있고, 1번째 장대에 있는 N개의 직경이 다른 링을 3번째까지 옮기는데 걸리는 최소 횟수 출력
# Input : N개의 링
# Output : (1) 최소 이동횟수 (2) Sequence

# 재귀함수 사용하여 풀기
# step(1). N-1개의 원판을 시작점에서 중간점으로 옮긴다.
# step(2). N번째 원판을 시작점에서 목적지로 옮긴다.
# step(3). N-1개의 원판을 중간점에서 목적지로 옮긴다.

def move_hanoi(N, start, mid, end):
    global ring
    global cnt
    
    if N == 1:
        ring.append(f"{start} {end}")
        cnt += 1
    else:
        move_hanoi(N-1,start,end,mid) # N-1개의 원판을 시작점에서 중간점으로 옮긴다.
        move_hanoi(1,start,mid,end)   # N번째 원판은 시작점에서 목적지로 이동
        move_hanoi(N-1,mid,start,end) # N-1개의 원판을 중간점에서 목적지로 옮긴다.

def solve():
    global ring
    global cnt
    
    N = int(input())
    ring = []
    cnt = 0
    
    move_hanoi(N, 1, 2, 3)
    print(cnt)
    for val in ring:
        print(val)

if __name__ == "__main__":
    solve()