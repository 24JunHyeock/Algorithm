import java.util.Arrays;

class Solution {
    public int[] solution(String my_string) {
        String [] strArray1 = my_string.split("");
        return Arrays.stream(strArray1)
            .filter(s -> s.matches("[0-9]"))
            .mapToInt(Integer::parseInt)
            .sorted()
            .toArray();
    }
}