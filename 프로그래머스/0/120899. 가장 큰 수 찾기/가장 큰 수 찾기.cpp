#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> array) {
    auto max_it = max_element(array.begin(), array.end()); 
    int max_val = *max_it;
    int idx = distance(array.begin(), max_it);
    return {max_val, idx};
}