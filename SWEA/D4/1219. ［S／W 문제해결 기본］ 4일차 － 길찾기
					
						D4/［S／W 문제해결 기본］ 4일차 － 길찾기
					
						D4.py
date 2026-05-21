#import sys
from collections import deque

#sys.stdin = open('input.txt', 'r')  # 제출시 주석
#input = sys.stdin.readline  # 속도위해 필수

for _ in range(1, 11):
    tc, L = map(int, input().split())
    Vs = list(map(int, input().split()))

    adjMat = [[0] * 100 for _ in range(100)]
    for line in range(0, L * 2, 2):
        _from, _to = Vs[line], Vs[line + 1]
        adjMat[_from][_to] = 1
    Queue = deque([0])
    visited = [False] * 100
    visited[0] = 1
    ans = 0
    Queue = deque([0])
    visited[0] = True
    ans = 0
    while Queue:
        here = Queue.popleft()
        if here == 99:
            ans = 1
            break
        for next in range(100):
            if adjMat[here][next] == 1 and not visited[next]:
                Queue.append(next)
                visited[next] = True
    print(f"#{tc} {ans}")




