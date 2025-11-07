import java.util.Arrays;

class Solution {
    public int[] solution(int n, int[] numlist) {
        int[] answer = {};
        for(int x : numlist){
            if(x%n==0){
                answer = Arrays.copyOf(answer, answer.length+1);
                answer[answer.length-1] = x;
            }
        }
        return answer;
    }
}