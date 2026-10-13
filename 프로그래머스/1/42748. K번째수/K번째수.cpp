#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> array, vector<vector<int>> commands) {
    vector<int> answer;
    for(int a=0;a<commands.size();a++){
        int i = commands[a][0];
        int j = commands[a][1];
        int k = commands[a][2];
        vector<int> ns(array.begin() + i-1, array.begin() + j);
        sort(ns.begin(), ns.end());
        answer.push_back(ns[k-1]);
    }
    return answer;
}