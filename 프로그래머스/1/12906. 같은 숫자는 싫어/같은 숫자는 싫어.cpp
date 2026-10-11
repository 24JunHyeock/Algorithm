#include <vector>
#include <iostream>

using namespace std;

vector<int> solution(vector<int> arr) 
{
    vector<int> answer;
    int tmp = -1;
    for(int num : arr){
        if(tmp != num){
            tmp = num;
            answer.push_back(num);
        }
    }

    return answer;
}