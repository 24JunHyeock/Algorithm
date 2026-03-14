#import sys
#sys.stdin = open('input.txt', 'r') #제출시 주석
#input = sys.stdin.readline  #속도위해 필수
T = int(input())

for tc in range(T):
    length = int(input())
    numbers = list(map(int, input().split()))


    print(f'#{tc+1} {max(numbers)-min(numbers)}')