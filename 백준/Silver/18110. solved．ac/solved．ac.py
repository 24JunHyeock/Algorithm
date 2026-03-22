import sys

#sys.stdin = open('input.txt', 'r') #제출시 주석
input = sys.stdin.readline  #속도위해 필수

def new_round(n):
    return int(n+0.5)

level = 0
n = int(input())
if n==0:
    print(level)
    sys.exit()
numList = []
for i in range(n):
    numList.append(int(input()))
numList.sort()
numR = new_round(n*0.15)
if numR>0:
    numList = numList[numR:-numR]
level = new_round(sum(numList) / len(numList))

print(level)

