class Solution {
    public int[] solution(long n) {

        String s = String.valueOf(n);
        int length = s.length();
        int [] answer = new int[length];
        

        long tempN = n; 
        int index = 0; 
        
        while(tempN > 0){
            answer[index] = (int) (tempN % 10);
            tempN /= 10;
            index++;
        }
        
        return answer;
    }
}