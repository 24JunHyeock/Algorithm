#include <stdio.h>

int main() {
    int arr[101] = {0};
    int N, M =0;
    scanf("%d %d",&N,&M);
    for (int i = 1; i<=N;i++){
        arr[i] = i;
    }
    for (int i = 0; i<M;i++){
        int x,y,box=0;
        scanf("%d %d",&x,&y);
        box=arr[x];
        arr[x]=arr[y];
        arr[y]=box;
    }
    for (int i = 1; i <=N; i++)
    {
       printf("%d ",arr[i]);
    }
    
    
    return 0;
}