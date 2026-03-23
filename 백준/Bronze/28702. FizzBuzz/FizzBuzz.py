import sys

#sys.stdin = open('input.txt', 'r')  # 제출시 주석
input = sys.stdin.readline  # 속도위해 필수

numList = []
I = 0
for i in range(3):
    numList.append(input().strip())
for i in range(3):
    if numList[i].isdigit():
        I = int(numList[i]) + (3-i)
if I%3==0 and I%5==0:
    print('FizzBuzz')
elif I%3==0 and I%5!=0:
    print('Fizz')
elif I%3!=0 and I%5==0:
    print('Buzz')
elif I%3!=0 and I%5!=0:
    print(I)
