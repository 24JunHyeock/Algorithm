#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> arr) {
    vector<int> answer;
    int min =9876543;
    for(int n:arr){
        if(min>n){
            min = n;
        }
    }
    auto idx = find(arr.begin(), arr.end(), min);
    arr.erase(idx);
    if(arr.empty()) arr.push_back(-1);
    return arr;
}