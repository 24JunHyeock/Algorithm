#import sys
#sys.stdin = open('input.txt', 'r') #제출시 주석
#input = sys.stdin.readline  #속도위해 필수

T = int(input())
cnt = [0]*T
for tc in range(T):
    Data = list(map(int, input().split()))
    array = [None] * (Data[1]+1)
    M = list(map(int, input().split()))
    for j in range(len(M)):
        array[M[j]] = True
    num = Data[1]
    K = 0
    errorNum = 0
    while num>0:
        if K == Data[0]:
            if (errorNum >= Data[0]):
                cnt[tc] = 0
                break
            if array[num]:
                cnt[tc]+=1
                K=0;
                errorNum =0
            else :
                num+=1
                errorNum+=1
        else:
            num-=1
            K+=1
    print(f'#{tc+1} {cnt[tc]}')



