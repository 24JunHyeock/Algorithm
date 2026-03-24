import sys

#sys.stdin = open('input.txt', 'r')  # 제출시 주석
input = sys.stdin.readline  # 속도위해 필수

N, K = map(int, input().split())
sumList = []
inputList = list(map(int, input().split()))
cnt = 0
sumList = [0]
sumNum=0
for i in inputList:
    sumNum = sumNum + i
    sumList.append(sumNum)
rList = []
for i in range(K,N+1):
    rList.append(sumList[i]-sumList[i-K])

print(max(rList))