import sys

#sys.stdin = open('input.txt', 'r')  # 제출시 주석
input = sys.stdin.readline  # 속도위해 필수

myMap = [list(map(int, input().split())) for _ in range(9)]

max = -1
wX,wY=0,0
for y in range(9):
    for x in range(9):
        if max < myMap[y][x]:
            max = myMap[y][x]
            wX = x + 1
            wY =y+1

print(max)
print(wY,wX)
