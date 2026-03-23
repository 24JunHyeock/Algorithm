import sys
from collections import deque

#sys.stdin = open('input.txt', 'r')  # 제출시 주석
input = sys.stdin.readline  # 속도위해 필수

T = int(input())

for i in range(T):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))
    queue = deque([(any, idx) for idx, any in enumerate(data)])
    cnt = 0
    while queue:
        num1 = max(queue)
        num2 = queue.popleft()
        if num1[0] == num2[0]:
            cnt += 1
            if num2[1] == M:

                break
        else:
            queue.append(num2)





    print(cnt)


