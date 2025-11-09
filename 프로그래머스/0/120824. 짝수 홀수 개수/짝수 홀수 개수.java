
class Solution {
    public int[] solution(int[] num_list) {
        int[] answer = new int[2];
        for(int x : num_list) {
           int i = (x%2==0)?answer[0]++:answer[1]++;
        }
            

        return answer;
    }
}