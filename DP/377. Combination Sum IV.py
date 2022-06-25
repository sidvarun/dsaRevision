







# TC => O(n * m)
# SC => O(n * m)
# where n is the target and m is the size of array

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        cache = { 0:1 }
        
        for total in range(1, target + 1):
            cache[total] = 0
            for n in nums:
                cache[total] += cache.get(total - n, 0)
        return cache[target]
        
        def dfs(total):
            if total == target:
                return 1
            if total > target:
                return 0
            if total in cache:
                return cache[total]
            
            cache[total] = 0
            for n in nums:
                cache[total] += dfs(total + n)
            return cache[total]
        return dfs(0)











class Solution {
public:
    int memo[1000];
    int combination(vector<int> &nums, int target){
        if(target == 0)
            return 1;
        if(target < 0)
            return 0;
        if(memo[target] != -1)
            return memo[target];
        
        int subres = 0;
        for(int i = 0; i<nums.size(); i++){
            subres += combination(nums, target - nums[i]);
        }
        return memo[target] = subres;
    }
    int combinationSum4(vector<int>& nums, int target) {
        memset(memo, -1, sizeof(memo));
        return combination(nums, target);
    }
};