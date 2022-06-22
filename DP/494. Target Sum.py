# Brute force TC is O(2^n) because the decision tree has a height of n (index ranging from 0 - n - 1)
# at each level of the decision tree we have 2 choices to make, i.e. whether we add the current value to the totalSum or substract it hence O(2^n)


# if we perfor some optimization with caching the tc will be O(n * totalSum)
# this is becase the state of dp will be defined by (index, total) the value of target can range form -(sumOfAllElementsOfArray) to +(sumOfAllElementsOfArray)


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {} # (index, total) -> # of ways
        
        def backtrack(i, total):
            if i == len(nums):
                return 1 if total == target else 0
            if (i, total) in dp:
                return dp[(i, total)]
        
            dp[(i, total)] = (backtrack(i + 1, total + nums[i]) +
                              backtrack(i + 1, total - nums[i]))   
            return dp[(i, total)]
        return backtrack(0, 0)


# Here since the total can go negative so instead of using a two dimensional memo array to cache results we can use an unordered_map of pairs
# key => pair{index, total}
# value => number of ways to when target is total and starting index is index