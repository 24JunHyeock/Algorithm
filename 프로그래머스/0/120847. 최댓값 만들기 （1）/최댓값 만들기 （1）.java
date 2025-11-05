class Solution {
    public int solution(int[] numbers) {
        int answer = 0;
        
        for(int i=0;i<=numbers.length-2;i++){
            for(int j=i+1;j<=numbers.length-1;j++){
                if(answer<numbers[i]*numbers[j]) answer = numbers[i]*numbers[j];
            }
        }
        return answer;
    }
}