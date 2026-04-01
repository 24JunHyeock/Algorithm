#import sys

#sys.stdin = open('./input.txt', 'r')  # 제출시 주석
#input = sys.stdin.readline  # 속도위해 필수

T = int(input())
for tc in range(1, T+1):
    stack = []
    ans = "error"
    str1 = list(input().split())
    for term in str1:
        if term.isdigit():
            stack.append(term)
        elif len(stack)>1 and term != ".":
            right = int(stack.pop())
            left = int(stack.pop())
            if term == "+":
                stack.append(left + right)
            elif term == "-":
                stack.append(left - right)
            elif term == "*":
                stack.append(left * right)
            elif term == "/":
                stack.append(left // right)
        elif len(stack) == 1 and term == ".":
            ans = stack.pop()
        else:
            break

    print(f"#{tc} {ans}")
