//Problem: https://leetcode.com/problems/two-sum/

class TwoSumOnePassHashMap {
    public int[] twoSum(int[] nums, int target) {
        
        Map<Integer, Integer> m = new HashMap<>();
        int other;
        
        for (int i=0; i<nums.length; i++){
            other = target - nums[i];
            if (m.containsKey(other)){
                return new int []{m.get(other), i};
            }
            m.put(nums[i], i);
        }
   
        
        throw new IllegalArgumentException("No two sum solution");
    }
}
