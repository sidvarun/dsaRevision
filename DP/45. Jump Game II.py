# so we maintain a window from l to r
# this window contains the subarray of positions we can reach from the previous jumps.
# we traverse this window to find the farthest we can go in the next jump
# once we have traversed the entire window we increemnent l = r + 1 and r = farthese which is the minmum and maximum jump we can make 
# from the urrent window to the next window

# TC => O(N)


class Solution:
    def jump(self, nums: List[int]) -> int:    
        l, r = 0, 0
        res = 0
        while r < (len(nums) - 1):
            maxJump = 0
            for i in range(l, r + 1):
                maxJump = max(maxJump, i + nums[i])
            l = r + 1
            r = maxJump
            res += 1
        return res

# DP solution is also available with TC => O(N^2)