import sys
from collections import deque

#sys.stdin = open('./input.txt', 'r')  # 제출시 주석
input = sys.stdin.readline  # 속도위해 필수

N, K = map(int, input().split())
myQueue = deque(range(1, N + 1))
result = []
while myQueue:
    myQueue.rotate(-(K-1))
    result.append(myQueue.popleft())
print("<", end="")
print(*result, sep=", ", end=">")

