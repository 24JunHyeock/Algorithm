import java.util.Arrays;

class Solution {
    public int[] solution(String[] strlist) {
        int[] answer = {};
        for(String s : strlist){
            answer = Arrays.copyOf(answer, answer.length +1);
            answer[answer.length-1] = s.length();
        }
        
        
        return answer;
    }
}