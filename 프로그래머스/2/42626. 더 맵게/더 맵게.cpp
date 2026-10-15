#include <string>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

int solution(vector<int> scoville, int K) {
    int answer = 0;
     priority_queue<int, vector<int>, greater<int>> min_pq ;
    for(int num:scoville){
        min_pq.push(num);
    }
    
    int n = min_pq.top();
    if(n>=K)return answer;
    while(min_pq.size()>1){
        int n1 = min_pq.top();
        min_pq.pop();
        int n2 = min_pq.top();
        min_pq.pop();
        min_pq.push(n1+(n2*2));
        answer++;
        if(min_pq.top()>=K)return answer;
    }
    n = min_pq.top();
    if(n>=K)return answer;
    else return -1;
}