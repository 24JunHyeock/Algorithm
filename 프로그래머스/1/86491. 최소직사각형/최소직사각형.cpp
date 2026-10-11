#include <string>
#include <vector>

using namespace std;

int solution(vector<vector<int>> sizes) {
   for(int i=0; i<sizes.size();i++){
       if(sizes[i][0]<sizes[i][1]) {
           int tmp = sizes[i][0];
           sizes[i][0] = sizes[i][1];
           sizes[i][1] = tmp;    
       }
   }
    int max = 0;
    for(int i=0;i<sizes.size();i++){
        if(max<sizes[i][0]){
            max = sizes[i][0];
        }
    }
    int answer = max;
     max = 0;
    for(int i=0;i<sizes.size();i++){
        if(max<sizes[i][1]){
            max = sizes[i][1];
        }
    }
    return answer *= max;
}