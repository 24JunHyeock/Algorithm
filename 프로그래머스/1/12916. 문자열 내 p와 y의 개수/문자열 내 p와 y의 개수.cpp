#include <string>
#include <iostream>
using namespace std;

bool solution(string s)
{
    int pCnt = 0;
    int yCnt = 0;
    for(char c: s){
        char cUpper = toupper(c);
        if(cUpper=='P') pCnt+=1;
        else if(cUpper=='Y') yCnt+=1;
    }

    return pCnt==yCnt?true:false;
}