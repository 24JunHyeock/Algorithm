#import sys

#sys.stdin = open('input.txt', 'r') #제출시 주석
#input = sys.stdin.readline  #속도위해 필수

T = int(input())
for tc in range(T):
    N = int(input())
    redSet = set()
    blueSet = set()
    for i in range(N):
        xYColor = list(map(int, input().split()))
        for x in range(xYColor[0], xYColor[2]+1):
            for y in range(xYColor[1], xYColor[3]+1):
                if xYColor[4] ==1:
                    redSet.add((x,y))
                else:
                    blueSet.add((x,y))

    cntSet = redSet & blueSet

    print(f'#{tc + 1} {len(cntSet)}')

