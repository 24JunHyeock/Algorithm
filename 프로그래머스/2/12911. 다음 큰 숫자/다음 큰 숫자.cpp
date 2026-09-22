#include <vector>
#include <iostream>
#include <format>
#include <string>

using namespace std;

int solution(int n) {
    string b_s = format("{:b}", n);
    int cnt = 0;
    for(int i=0;i<b_s.size();i++){
        if(b_s[i] == '1') cnt+=1;
    }
    int ans_cnt=0;
    while(cnt!=ans_cnt){
        ans_cnt = 0;
        n+=1;
        string b_s = format("{:b}", n);
        for(int i=0;i<b_s.size();i++){
        if(b_s[i] == '1') ans_cnt+=1;
        }
        
    }
    return n;
}