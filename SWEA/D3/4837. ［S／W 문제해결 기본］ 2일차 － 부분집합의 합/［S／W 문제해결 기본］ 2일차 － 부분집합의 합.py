#import sys
#sys.stdin = open('input.txt', 'r') #제출시 주석
#input = sys.stdin.readline  #속도위해 필수
T = int(input())
for tc in range(T):
    N, K = map(int, input().split())

    arr = [i for i in range(1, 13)]
    n = 12
    cnt = 0

    for i in range(1<<n):
        elementsSum = 0
        if bin(i).count("1") == N:
            for j in range(n):
                if i&(1<<j):
                    elementsSum+=arr[j]
            if elementsSum == K:
                cnt+=1




    print(f"#{tc+1} {cnt}")