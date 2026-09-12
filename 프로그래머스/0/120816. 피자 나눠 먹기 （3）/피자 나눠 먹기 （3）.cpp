#include <string>
#include <vector>

using namespace std;

int solution(int slice, int n) {
    int temp = n%slice;
    int temp2 = n/slice;
    return temp>0?temp2+1:temp2;
}