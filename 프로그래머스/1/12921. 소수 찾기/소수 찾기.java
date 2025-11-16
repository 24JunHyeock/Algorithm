import java.util.Arrays;

class Solution {
    public int solution(int n) {
        int answer = 1;
        boolean nums [] = new boolean[n + 1];
        Arrays.fill(nums, true);
        nums[0] = false;
        nums[1] = false;
        for(int x =2;x*x<=n;x++){
            if(nums[x]){
                for (int y = x * x; y <= n; y += x) {
                nums[y] = false;
                }
            }
        }
        for (int i = 3; i <= n; i++) {
            if (nums[i]) {
            answer++;
            }
        }
        return answer;
    }
}