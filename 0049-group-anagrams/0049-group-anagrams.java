class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List> map = new HashMap<>();
        
        for (String str : strs) {
            char[] cArr = str.toCharArray();
            Arrays.sort(cArr);
            // String sorted = cArr.toString();
            String sorted = String.valueOf(cArr);
            
            if (map.containsKey(sorted)) {
                List<String> list = map.get(sorted);
                list.add(str);
                map.put(sorted, list);
            }
            else {
                List<String> list = new ArrayList<>();
                list.add(str);
                map.put(sorted, list);
            }
        }
        
        return new ArrayList(map.values());
    }
}