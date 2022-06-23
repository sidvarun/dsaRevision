# idea is to maintain 2 thigs, the maximum Product subArray till now as well as the minimum product subarray till now
# if we encounter a +ve elelment the max product will be the max product till how * the curr element
# if we encounter a -ve element the max product will be the min product till now * the curr element
# if we get a '0' anywhere, we reset both maxProduct and minProduct equal to 1 -> actually we don't need this check, it will be done automatically

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # O(n)/O(1) : Time/Memory
        res = max(nums)
        curMin, curMax = 1, 1
        
        for n in nums: 
            tmp = curMax * n
            curMax = max(n * curMax, n * curMin, n) 
            curMin = min(tmp, n * curMin, n)
            res = max(res, curMax)
        return res