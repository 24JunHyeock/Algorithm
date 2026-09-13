#include <string>
#include <vector>

using namespace std;

int solution(int num) {
    int cnt = 0;
    long long n = num;
    while(n!=1 and cnt<500){
        if(n%2==0) n /=2;
        else n = n*3+1;
        cnt+=1;
    }
    if (n != 1) return -1;
    return cnt;
}