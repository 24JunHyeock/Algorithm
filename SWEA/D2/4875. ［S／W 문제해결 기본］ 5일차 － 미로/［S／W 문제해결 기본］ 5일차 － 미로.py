#import sys

#sys.stdin = open('./input.txt', 'r')  # 제출시 주석
#input = sys.stdin.readline  # 속도위해 필수
def should_turn(newY, newX):
    if 0<=newY<N and 0<=newX<N:
        if arr[newY][newX]==0 or arr[newY][newX]==3:
            return True
    return False

T = int(input())
for tc in range(1, T+1):
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]
    N = int(input())
    arr = [list(map(int, input().strip())) for _ in range(N)]
    startY, startX = 0, 0
    for y in range(len(arr)):
        for x in range(len(arr[y])):
            if arr[y][x] == 2:
                startY, startX = y, x
    stackXY = [(startY, startX)]
    ans = 0
    while stackXY:
        startY, startX = stackXY.pop()
        if arr[startY][startX] == 3:
            ans = 1
            break
        if arr[startY][startX] == 2 or arr[startY][startX] == 0:
            arr[startY][startX] = 1

        for dir in range(4):
            newY = startY + dy[dir]
            newX = startX + dx[dir]
            if should_turn(newY, newX) and arr[newY][newX] != 1:
                stackXY.append((newY, newX))

    print(f"#{tc} {ans}")






