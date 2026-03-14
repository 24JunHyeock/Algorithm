#import sys
#sys.stdin = open('input.txt', 'r') #제출시 주석
#input = sys.stdin.readline  #속도위해 필수
T = int(input())

for tc in range(T):
    length = int(input())
    numbers = list(map(int, input().split()))
    maxNumber = numbers[0]
    miuNumber = numbers[0]
    for i in numbers:
        if i > maxNumber:
            maxNumber = i
        if i < miuNumber:
            miuNumber = i


    print(f'#{tc+1} {maxNumber-miuNumber}')