#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    int ch =0;
    while(ch<progresses.size()){
        int cnt =0;
        
        for(int i =ch;i<progresses.size();i++){
            progresses[i]+=speeds[i];
            if(progresses[ch]>99){
                ch++;
                cnt++;
            }
            
        }
        if(cnt>0)answer.push_back(cnt);
        
        
        
    }
    return answer;
}