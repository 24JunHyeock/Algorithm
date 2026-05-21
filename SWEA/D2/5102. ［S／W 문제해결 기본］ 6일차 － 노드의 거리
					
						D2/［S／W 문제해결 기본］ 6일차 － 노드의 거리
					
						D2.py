#import sys
from collections import deque

#sys.stdin = open('input.txt', 'r')  # 제출시 주석
#input = sys.stdin.readline  # 속도위해 필수

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    visited = [0] * (V+1)
    adjMat = [[0 for _ in range(V+1)] for _ in range(V+1)]
    for line in range(E):
        _from, _to = map(int, input().split())
        adjMat[_from][_to] = 1
        adjMat[_to][_from] = 1
    S, G = map(int, input().split())
    Queue = deque([S])
    visited[S] = 1
    ans = 0
    while Queue:
        here = Queue.popleft()
        if here == G:
            ans = visited[here]-1
            break
        for next in range(1, V+1):
            if adjMat[here][next] == 1 and visited[next] == 0:
                Queue.append(next)
                visited[next] =visited[here]+ 1
    print(f"#{tc} {ans}")




