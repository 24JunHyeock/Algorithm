#include <string>
#include <vector>

using namespace std;

string solution(string phone_number) {
    string answer = phone_number.substr(0, phone_number.size()-4);
    phone_number.erase(0, phone_number.size()-4);
    int n = answer.size();
    for(int i=0;i<n;i++){
        answer.append("*");
    }
    answer.erase(0,n);
    answer.append(phone_number);
    return answer;
}