class Solution {
    public int characterReplacement(String s, int k) {
        int res = 0;
        int l = 0;
        int maxCharCount = 0;
        Map<Character, Integer> map = new HashMap<>();
        
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            map.put(c, map.getOrDefault(c, 0) + 1);
            maxCharCount = Math.max(maxCharCount, map.get(c));
            
            if (i - l + 1 - maxCharCount <= k)
                res = Math.max(res, i - l + 1);
            else {
                map.put(s.charAt(l), map.get(s.charAt(l)) - 1);
                l++;
            }
        }
        
        return res;
    }
}