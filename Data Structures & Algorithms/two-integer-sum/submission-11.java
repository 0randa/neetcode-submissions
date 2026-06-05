class Solution {
    public int[] twoSum(int[] nums, int target) {
        int i = 0;
        int j = nums.length - 1;
        int[] res = new int[2];
        while (i < j) {
            int _sum = nums[i] + nums[j];
            if (_sum == target) {
                res[0] = i; 
                res[1] = j;
                return res;
            } else if (_sum < target) {
                // sum less than target, increment i
                i++;
            } else {
                j--;
            }
        }
        return res;
    }
}
