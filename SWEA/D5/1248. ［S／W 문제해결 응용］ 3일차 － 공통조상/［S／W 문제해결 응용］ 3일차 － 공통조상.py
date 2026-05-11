#import sys

#sys.stdin = open('input.txt', 'r')  # 제출시 주석
#input = sys.stdin.readline  # 속도위해 필수

#sys.setrecursionlimit(20000)
def depth(node, d):
    Tree[node][4] = d  # 현재 깊이 저장
    for i in range(2): # 왼쪽(0), 오른쪽(1) 자식 탐색
        child = Tree[node][i]
        if child != 0:
            depth(child, d + 1)
def preorder_traversal(N):
    if N:
        print("%d" % N, end=" ")
        preorder_traversal(Tree[N][0])
        preorder_traversal(Tree[N][1])

def node_Size(n):
    if n == 0:
        return 0
    return node_Size(Tree[n][0]) + node_Size(Tree[n][1]) + 1

def LCA(n1, n2):
    while Tree[n1][4] != Tree[n2][4]:
        if Tree[n1][4] > Tree[n2][4]:
            n1 = Tree[n1][3]
        else:
            n2 = Tree[n2][3]

    while n1 != n2:
        n1 = Tree[n1][3]
        n2 = Tree[n2][3]
    return n1

T = int(input())

for tc in range(T):
    V, E, N1, N2 = map(int, input().split())
    Tree = [[0] * 5 for _ in range(V + 1)]
    Data = list(map(int, input().split()))
    for i in range(V+1):
        Tree[i][3] = Tree[i][4] = -1
    Tree[1][4] = 0

    # 여기까지가 초기값

    for i in range(E):  # 간선의 수만큼 입력을 받음
        parent, child = Data[i * 2], Data[i * 2 + 1]
        if Tree[parent][0] == 0:
            Tree[parent][0] = child
            Tree[parent][2] += 1
            Tree[child][3] = parent
        else:
            Tree[parent][1] = child
            Tree[parent][2] += 1
            Tree[child][3] = parent
    depth(1, 0)
    CA = LCA(N1, N2)
    S = node_Size(CA)
    print(f"#{tc+1} {CA} {S}")

