import java.util.ArrayList;

class Solution {
    public String[] solution(String[] quiz) {
        ArrayList<String> answer = new ArrayList<>();
        for(int i=0;i<quiz.length;i++){
            String[] str2 = quiz[i].split(" ");
            if(str2[1].equals("+")?Integer.parseInt(str2[0])+Integer.parseInt(str2[2])==Integer.parseInt(str2[4]):Integer.parseInt(str2[0])-Integer.parseInt(str2[2])==Integer.parseInt(str2[4])){
            answer.add("O");
        }else answer.add("X");
        }
        return answer.toArray(new String[quiz.length]);
    }
}