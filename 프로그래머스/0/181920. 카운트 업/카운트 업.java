import java.util.Arrays;

class Solution {
    public int[] solution(int start_num, int end_num) {
        int[] answer = new int[end_num-start_num+1];
        Arrays.setAll(answer, i -> start_num+i);
        return answer;
    }
}