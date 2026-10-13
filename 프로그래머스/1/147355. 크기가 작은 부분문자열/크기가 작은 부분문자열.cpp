#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(string t, string p) {
    int answer = 0;
    for(int i=0;i<t.size()-p.size()+1;i++){
        string s = t.substr(i,p.size());
        long long si = stoll(s);
        long long pi = stoll(p);
        if(pi>=si)answer++;
    }
    return answer;
}