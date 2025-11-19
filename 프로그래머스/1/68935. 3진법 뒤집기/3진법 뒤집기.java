import java.util.Arrays;

class Solution {
    public int solution(int n) {
        int answer = 0;
        int[] th = {};
        while (n>0){
            th = Arrays.copyOf(th, th.length+1);
            th[th.length-1] = n%3;
            n/=3;
        }
        int m = th.length-1;
        for(int num : th){
            answer+=(int)(Math.pow(3,m)*num);
            m--;
        }
        return answer;
    }
}