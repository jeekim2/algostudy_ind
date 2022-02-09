#https://www.acmicpc.net/problem/2164
#시간 초과로 인한 deque 사용 , pop을 사용하게 되면 시간 초과가 됨

from collections import deque


N = int(input())

queue = deque()
for i in range(N):
  queue.append(i+1)

while len(queue)>1:
  queue.popleft()
  queue.append(queue.popleft())

print(queue[0])
