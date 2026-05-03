#import sys
#sys.stdin = open('input.txt', 'r') #제출시 주석
#input = sys.stdin.readline  #속도위해 필수

def binary_Search(r, p):
    l = 1
    cnt = 0
    c = 0
    while p != c:
        c = int((l+r)/2)
        if c > p:
            cnt +=1
            r = c
        else:
            cnt +=1
            l = c
    return cnt

T = int(input())
for tc in range(T):
    r, pA, pB = map(int, input().split())
    A = binary_Search(r, pA)
    B = binary_Search(r, pB)
    if A == B:
        res = 0
    elif A < B:
        res = 'A'
    else:
        res = 'B'

    print(f"#{tc+1} {res}")