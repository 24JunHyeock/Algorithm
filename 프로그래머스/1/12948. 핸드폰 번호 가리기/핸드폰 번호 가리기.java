class Solution {
    public String solution(String phone_number) {
        String m = "*".repeat(phone_number.length()-4);
        String answer = phone_number.substring(phone_number.length()-4);
        return m+answer;
    }
}