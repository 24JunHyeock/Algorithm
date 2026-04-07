import sys

#sys.stdin = open('./input.txt', 'r')  # 제출시 주석
input = sys.stdin.readline  # 속도위해 필수

N = int(input())
stack = []

for _ in range(N):
    str = input().split()
    if str[0]=="1":
        stack.append(str[1])
    elif str[0]=="2":
        print(stack.pop() if stack else -1)
    elif str[0]=="3":
        print(len(stack))
    elif str[0]=="4":
        print(0 if stack else 1)
    elif str[0]=="5":
        print(stack[-1] if stack else -1)
