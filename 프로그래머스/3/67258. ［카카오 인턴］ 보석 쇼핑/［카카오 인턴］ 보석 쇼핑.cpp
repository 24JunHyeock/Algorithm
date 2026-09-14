#include <string>
#include <vector>
#include <unordered_map>
#include <set>

using namespace std;

vector<int> solution(vector<string> gems) {
    set<string> gem_types(gems.begin(), gems.end());
    int total_types = gem_types.size();
    
    unordered_map<string, int> gem_count;
    int start = 0, end = 0;
    int min_len = gems.size() + 1;
    vector<int> answer(2, 0);

    while (end < gems.size()) {
        gem_count[gems[end]]++;
        end++;


        while (gem_count.size() == total_types) {
            if (end - start < min_len) {
                min_len = end - start;
                answer[0] = start + 1; 
                answer[1] = end;       
            }
            gem_count[gems[start]]--;
            if (gem_count[gems[start]] == 0) {
                gem_count.erase(gems[start]);
            }
            start++;
        }
    }

    return answer;
}