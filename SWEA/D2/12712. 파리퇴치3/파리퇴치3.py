#import sys

#sys.stdin = open('./input.txt', 'r')  # 제출시 주석
#input = sys.stdin.readline  # 속도위해 필수

def isSafe(newY,newX):
    return 0<=newY<N and 0<=newX<N

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]


    ans = 0
    for y in range(N):
        for x in range(N):
            sum = arr[y][x]
            for dir in range(4):
                for size in range(1, M):
                    newY = y + dy[dir]*size
                    newX = x + dx[dir]*size
                    if isSafe(newY,newX):
                        sum += arr[newY][newX]

            if sum > ans:
                ans = sum
    dy2 = [-1, -1, 1, 1]
    dx2 = [-1, 1, -1, 1]
    for y in range(N):
        for x in range(N):
            sum = arr[y][x]
            for dir in range(4):
                for size in range(1, M):
                    newY = y + dy2[dir]*size
                    newX = x + dx2[dir]*size
                    if isSafe(newY,newX):
                        sum += arr[newY][newX]

            if sum > ans:
                ans = sum

    print(f"#{tc} {ans}")