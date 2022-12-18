class Solution {
    public String minWindow(String s, String t) {
        // left pointer
        int l = 0;
        
        String res = "";

        // hashmap stores unique char and counts of t
        Map<Character, Integer> map = new HashMap<>();
        for (int i = 0; i < t.length(); i++)
            map.put(t.charAt(i), map.getOrDefault(t.charAt(i), 0) + 1);
        
        // unique char count of t
        int tCount = map.size();
        
        // hashmap for the window
        Map<Character, Integer> window = new HashMap<>();        
        
        // unique char count of window
        int windowCount = 0;
        
        for (int r = 0; r < s.length(); r++) {
            if (!map.containsKey(s.charAt(r)))
                continue;
            
            // update window hashmap
            window.put(s.charAt(r), window.getOrDefault(s.charAt(r), 0) + 1);
            
            // update windowCount if the count of char at r matches
            if (window.get(s.charAt(r)).intValue() == map.get(s.charAt(r)).intValue())
                windowCount++;
            
            // move l++ if the window contians all chars in t
            while (l <= r && windowCount == tCount) {
                if (res.equals(""))
                    res = s.substring(l, r + 1);
                else {
                    if (s.substring(l, r + 1).length() < res.length())
                        res = s.substring(l, r + 1);
                }
                window.put(s.charAt(l), window.getOrDefault(s.charAt(l), 0) - 1);
                if (map.containsKey(s.charAt(l)) && window.get(s.charAt(l)).intValue() < map.get(s.charAt(l)).intValue())
                    windowCount--;
                l++;
            }
        }
        
        return res;
    }
}