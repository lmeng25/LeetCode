class Solution {
    public String reverseStr(String s, int k) {
        String res = "";
        
        for (int i = 0; i < s.length(); i += 2 * k) {
            if (i + k < s.length()) {
                res += reverse(s.substring(i, i + k));
                
                if (i + 2 * k < s.length())
                    res += s.substring(i + k, i + 2 * k);
                else
                    res += s.substring(i + k, s.length());
            }
            else
                res += reverse(s.substring(i, s.length()));
        }
        
        return res;
    }
    
    private String reverse(String s) {
        String res = "";
        for (int i = s.length() - 1; i >= 0; i--)
            res += s.charAt(i);
        
        return res;
    }
}