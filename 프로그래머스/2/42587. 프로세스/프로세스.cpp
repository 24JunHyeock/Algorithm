#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> priorities, int location) {
    int answer = 0;
    vector<int> arr1 = priorities;
    sort(arr1.rbegin(), arr1.rend());
    int S = priorities.size();
    int n = 0;
    for(int i=0; i<= S;i++){
        i%=S;
        if(priorities[i]==arr1[n]){
            answer++;
            n++;
            if(location==i)return answer;
            
        }
        
    }
}