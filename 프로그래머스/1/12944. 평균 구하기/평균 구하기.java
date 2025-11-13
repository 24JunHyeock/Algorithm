class Solution {
    public double solution(int[] arr) {
        double answer = 0;
        for(double x:arr){
            answer +=x;
        }
        return answer/arr.length;
    }
}