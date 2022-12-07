class Solution {
    public int shortestDistance(String[] wordsDict, String word1, String word2) {
        ArrayList<Integer> list1 = new ArrayList<>();
        ArrayList<Integer> list2 = new ArrayList<>();
        
        for (int i = 0; i < wordsDict.length; i++) {
            if (wordsDict[i].equals(word1))
                list1.add(i);
            if (wordsDict[i].equals(word2))
                list2.add(i);
        }
        
        int res = Math.abs(list1.get(0) - list2.get(0));
        
        for (int i = 0; i < list1.size(); i++) {
            for (int j = 0; j < list2.size(); j++) {
                if (Math.abs(list1.get(i) - list2.get(j)) < res)
                    res = Math.abs(list1.get(i) - list2.get(j));
            }
        }
        
        return res;
    }
}