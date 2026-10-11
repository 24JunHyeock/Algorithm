#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> answers) {
    vector<int> answer;
    vector<int> one = {1, 2, 3, 4, 5};
    vector<int> two = {2, 1, 2, 3, 2, 4, 2, 5};
    vector<int> thr = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
    int n = 0;
    vector<int> cnt (3);
    for(int ans : answers){
        if(ans == one[n%5])cnt[0]++;
        if(ans == two[n%8])cnt[1]++;
        if(ans == thr[n%10])cnt[2]++;
        n++;
    }
    int max = 0;
    for(int i=0;i<3;i++){
        if(max<cnt[i]) max=cnt[i];
    }
    for(int i=0;i<3;i++){
        if(max==cnt[i]) answer.push_back(i+1);
    }
    return answer;
    
}