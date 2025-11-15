class Solution {
    public int solution(int[] num_list) {
        int x = 0;
        int y = 1;
        for(int z : num_list){
            y *=z;
            x += z;
        }

        
        return y >x*x?0:1;
    }
}