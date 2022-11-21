class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> res = new ArrayList<>();
        
        for (int i = 0; i < strs.length; i++) {
            boolean found = false;
            for (int j = 0; j < res.size(); j++) {
                String temp = res.get(j).get(0);
                if (anagram(temp, strs[i])) {
                    res.get(j).add(strs[i]);
                    found = true;                    
                }
            }
            if (!found) {
                res.add(new ArrayList<String>());
                res.get(res.size() - 1).add(strs[i]);
            }
        }
        
        return res;
    }
    
    private boolean anagram(String str1, String str2) {
        if (str1.length() != str2.length())
            return false;
        
        int[] arr = new int[26];
        for (int i = 0; i < str1.length(); i++) {
            arr[str1.charAt(i) - 'a']++;
            arr[str2.charAt(i) - 'a']--;
        }
        
        for (int i = 0; i < 26; i++) {
            if (arr[i] != 0)
                return false;
        }
        
        return true;
    }
}