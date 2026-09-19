#include <iostream>
#include<vector>
#include <algorithm>

using namespace std;

int solution(vector<int> A, vector<int> B)
{
    int answer = 0;
    sort(A.begin(), A.end());
    sort(B.rbegin(), B.rend());
    while(!(A.empty())){
        int x =A.back(); A.pop_back();
        int y =B.back(); B.pop_back();
        answer+=x*y;
    }
    return answer;
}