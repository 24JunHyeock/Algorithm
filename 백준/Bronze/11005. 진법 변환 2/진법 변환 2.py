import sys
#sys.stdin = open('input.txt', 'r') #제출시 주석
input = sys.stdin.readline  #속도위해 필수

R = []
R2 = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
M = list(map(int, input().split()))
while(M[0]>0):
    R.append(R2[M[0]%M[1]])
    M[0]//=M[1]


print(''.join(R[::-1]))
