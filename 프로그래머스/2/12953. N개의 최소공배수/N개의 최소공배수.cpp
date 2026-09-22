#include <string>
#include <vector>
#include <numeric>

using namespace std;

int solution(vector<int> arr) {
    long long ans = arr[0];
    for(int i=1; i<arr.size();i++){
        ans = lcm(ans, arr[i]);
    }
    return ans;
}