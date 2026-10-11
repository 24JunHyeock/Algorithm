#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> sides) {
    sort(sides.rbegin(), sides.rend());
    int answer=2;
    if(sides[0] < sides[1]+sides[2])answer=1;
    return answer;
}