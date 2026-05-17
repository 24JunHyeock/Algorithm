#import sys
from collections import deque

#sys.stdin = open('input.txt', 'r')  # 제출시 주석
#input = sys.stdin.readline  # 속도위해 필수


for tc in range(1, 11):
    V, E= map(int, input().split())
    node_Degree = [0] * (V + 1)
    node_Graph = [[] for _ in range(V + 1)]
    Data = list(map(int, input().split()))
    for i in range(E):
        node, degree = Data[i*2], Data[i*2+1]
        node_Degree[degree] += 1
        node_Graph[node].append(degree)
    q = deque()
    result = []
    for i in range(1, V+1):
        if node_Degree[i] == 0:
            q.append(i)
    while q:
        now_Node = q.popleft()
        result.append(now_Node)
        for next_Node in node_Graph[now_Node]:
            node_Degree[next_Node] -= 1
            if node_Degree[next_Node] == 0:
                q.append(next_Node)



    print(f"#{tc}",*result)