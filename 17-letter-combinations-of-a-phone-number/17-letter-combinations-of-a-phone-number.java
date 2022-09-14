class Solution {
    List<String> res = new ArrayList<>();

    public List<String> letterCombinations(String digits) {
        StringBuilder sb = new StringBuilder();
        String[] arr = new String[digits.length()];
        
        Map<Integer, String> map = new HashMap<>();
        map.put(2, "abc");
        map.put(3, "def");
        map.put(4, "ghi");
        map.put(5, "jkl");
        map.put(6, "mno");
        map.put(7, "pqrs");
        map.put(8, "tuv");
        map.put(9, "wxyz");
        
        for (int i = 0; i < digits.length(); i++) {
            arr[i] = map.get(Integer.parseInt(digits.substring(i, i + 1)));
        }
        
        dfs(arr, sb, 0, 0);
        return res;
    }
    
    private void dfs(String[] arr, StringBuilder sb, int startDigit, int startLetter) {
        if (sb.length() == arr.length) {
            if (arr.length != 0)
                res.add(sb.toString());
            return;
        }
        
        for (int i = startDigit; i < arr.length; i++) {
            for (int j = startLetter; j < arr[i].length(); j++) {
                sb.append(arr[i].charAt(j));
                dfs(arr, sb, i + 1, startLetter);
                sb.setLength(sb.length() - 1);
            }
        }
    }
}