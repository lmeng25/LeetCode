class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        // return list
        List<List<Integer>> res = new ArrayList<>();
        
        // sort the given array
        Arrays.sort(nums);
        
        // first number
        int num1 = nums[0] - 1;
        
        for (int i = 0; i < nums.length; i++) {
            // check for dupulicate
            if (nums[i] != num1) {
                Map<Integer, Integer> map = new HashMap<>();
                
                // find numbers pair == -nums[i]
                int left = i + 1;
                int right = nums.length - 1;
                while (left < right) {
                    if (nums[left] + nums[right] == -nums[i]) {
                        map.put(nums[left], nums[right]);
                        left++;
                        right--;
                    }
                    else if (nums[left] + nums[right] < -nums[i])
                        left++;
                    else
                        right--;
                }
                
                // add to res
                if (!map.isEmpty()) {
                    for (Map.Entry<Integer, Integer> set : map.entrySet()) {
                        List<Integer> list = new ArrayList<>();
                        list.add(nums[i]);
                        list.add(set.getKey());
                        list.add(set.getValue());
                        res.add(list);
                    }
                }
            }
            // update num1
            num1 = nums[i];
        }
        return res;
    }
}