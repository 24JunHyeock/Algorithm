#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> numbers) {
    vector<int> answer;
    vector<bool> ch (201,false);
    for(int i=0; i<numbers.size();i++){
        for(int j=i+1;j<numbers.size();j++){
            int sum = numbers[i]+numbers[j];
            if(!ch[sum]){
                answer.push_back(sum);
                ch[sum]=true;
            }
        }
        sort(answer.begin(), answer.end());
    }
    return answer;
}