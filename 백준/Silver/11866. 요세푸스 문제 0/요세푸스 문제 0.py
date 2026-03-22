import sys
from collections import deque

#sys.stdin = open('input.txt', 'r') #제출시 주석
input = sys.stdin.readline  #속도위해 필수


N, K = map(int, input().split())
queue = deque(range(1, N + 1))
rQ = deque()
while queue:
    queue.rotate(-K+1)
    rQ.append(queue.popleft())
print("<" + ", ".join(map(str, rQ)) + ">")

