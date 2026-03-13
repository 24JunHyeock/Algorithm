import sys
#sys.stdin = open('input.txt', 'r') #제출시 주석
input = sys.stdin.readline  #속도위해 필수

R = []
R2 = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
M = list(map(int, input().split()))
while(M[0]>0):
    R.append(R2[M[0]%M[1]])
    M[0]//=M[1]

R.reverse()
print(''.join(R))
