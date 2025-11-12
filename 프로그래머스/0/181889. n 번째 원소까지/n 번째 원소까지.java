class Solution {
    public int[] solution(int[] num_list, int n) {
        int[] answer = new int[n];
        while(n>0){
            n--;
            answer[n] = num_list[n];
            
        }
        return answer;
    }
}