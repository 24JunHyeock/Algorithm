import sys

#sys.stdin = open('./input.txt', 'r')  # 제출시 주석
input = sys.stdin.readline  # 속도위해 필수

stack = []

n = int(input())
for _ in range(n):
    num = int(input())
    if num == 0:
        stack.pop()
    else:
        stack.append(num)
print(sum(stack))


