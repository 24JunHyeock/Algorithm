import sys

#sys.stdin = open('input.txt', 'r')  # 제출시 주석
input = sys.stdin.readline  # 속도위해 필수


isbn = input().strip()
sumIsbn = 0
idxIsbn = 0
for i in range(13):
    if isbn[i]!="*":
        if i%2==0:
            sumIsbn += int(isbn[i])
        else:
            sumIsbn += 3*int(isbn[i])
    else:
        idxIsbn = i
result = (10 - sumIsbn % 10) % 10

if idxIsbn%2==0:
    print(result)
else:
    print((result * 7) % 10)


