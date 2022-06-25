
https://leetcode.com/problems/burst-balloons/discuss/76228/Share-some-analysis-and-explanations

# We then think can we apply the divide and conquer technique? After all there seems to be many self similar sub problems 
# from the previous analysis.

# Well, the nature way to divide the problem is burst one balloon and separate the balloons into 2 
# sub sections one on the left and one one the right. However, in this problem the left and right become 
# adjacent and have effects on the maxCoins in the future.

# Then another interesting idea come up. Which is quite often seen in dp problem analysis. 
# That is reverse thinking. Like I said the coins you get for a balloon does not depend on 
# the balloons already burst. Therefore
# instead of divide the problem by the first balloon to burst, we divide the problem 
# by the last balloon to burst.
# Why is that? Because only the first and last balloons we are sure of their adjacent balloons before hand!

# For the first we have nums[i-1]*nums[i]*nums[i+1] for the last we have nums[-1]*nums[i]*nums[n].

# OK. Think about n balloons if i is the last one to burst, what now?

# We can see that the balloons is again separated into 2 sections. But this time since the balloon i is the
# last balloon of all to burst, the left and right section now has well defined boundary and do not affect each other! Therefore we can do either recursive method with memoization or dp.


class Solution {
public:
    int memo[303][303];
    int dfs(int l, int r, vector<int>& nums){
        
        if(l > r)
            return 0;
        if(memo[l][r] != -1)
            return memo[l][r];
        
        if(l == r)
            return memo[l][r] = nums[l] * nums[l - 1] * nums[l + 1];
        
        int subRes = 0;
        
        for(int k = l; k <= r; k++){
            
            int left = dfs(l, k - 1, nums);
            int right = dfs(k + 1, r, nums);
            
            subRes = max(subRes, left + nums[l - 1] * nums[k] * nums[r + 1] + right);
        }
        
        return memo[l][r] = subRes;
    }
    
    int maxCoins(vector<int>& nums) {
        
        memset(memo, -1, sizeof(memo));
        nums.push_back(1);
        nums.insert(nums.begin(), 1);
        
        return dfs(1, nums.size() - 2,  nums);
    }
};





















class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        cache = {}
        nums = [1] + nums + [1]
        
        for offset in range(2, len(nums)):
            for left in range(len(nums) - offset):
                right = left + offset
                for pivot in range(left + 1, right):
                    coins = nums[left] * nums[pivot] * nums[right]
                    coins += cache.get((left, pivot), 0) + cache.get((pivot, right), 0)
                    cache[(left, right)] = max(coins, cache.get((left, right), 0))
        return cache.get((0, len(nums) - 1), 0)