import sys

#sys.stdin = open('input.txt', 'r') #제출시 주석
input = sys.stdin.readline  #속도위해 필수

N = int(input())
numList= list(map(int, input().split()))

sumList = [0]
for num in numList:
    sumList.append(sumList[-1]+num)
M = int(input())
for _ in range(M):
    start, end = map(int, input().split())
    print(sumList[end] - sumList[start-1])