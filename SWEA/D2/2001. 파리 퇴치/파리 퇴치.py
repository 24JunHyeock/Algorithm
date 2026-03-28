#import sys
#sys.stdin = open('input.txt', 'r')  # 제출시 주석
#input = sys.stdin.readline  # 속도위해 필수

def isSafe(new):
    return new<=N




T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    numList1 = [list(map(int, input().split())) for _ in range(N)]
    numList2 = [[0]*((N-M)+1) for _ in range(N)]
    for y in range(N):
        for x in range(N):
            newX = x+M
            if isSafe(newX):
                numList2[y][x] = sum(numList1[y][x:newX])
    maxList = []
    for y in range(len(numList2)):
        newY = y + M
        if isSafe(newY):
            for x in range(len(numList2[y])):
                current_sum = 0
                for i in range(y, newY):
                    current_sum += numList2[i][x]
                maxList.append(current_sum)
    maxNum = max(maxList)




    print(f'#{tc+1} {maxNum}')