class Solution {
    public long solution(int a, int b) {
        
        return b > a ? ((long)b - a + 1) * ((long)a + b) / 2 : ((long)a - b + 1) * ((long)a + b) / 2;
    }
}