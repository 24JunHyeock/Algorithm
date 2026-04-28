#import sys
from collections import deque

#sys.stdin = open('input.txt', 'r') #제출시 주석
#input = sys.stdin.readline  #속도위해 필수


T = int(input())

for tc in range(T):
    N, M, L = map(int, input().split())
    numList = deque(list(input().split()))
    for _ in range(M):
        idx, n = map(int, input().split())
        numList.insert(idx, n)

    print(f"#{tc+1} {numList[L]}")