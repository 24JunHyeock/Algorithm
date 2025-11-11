class Solution {
    public int solution(int n) {
        int answer = 0;
        if(n%2==0){
            while(n>0){
                answer += n*n;
                n-=2;
            }
        }else{
            n = (n+1)/2;
            answer = n * n;
        }
        return answer;
    }
}