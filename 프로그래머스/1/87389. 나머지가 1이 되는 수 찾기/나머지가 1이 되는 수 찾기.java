class Solution {
    public int solution(int n) {
        int answer = 1;
        if(n==3){
            return n-1;
        }
        while(n>0){
            if(n%answer==1)break;
            answer++;
        }
        return answer;
    }
}