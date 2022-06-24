# top down and bottom up dp solution are also there, TC for them is O(N^2)

# the following dp approach has TC => O(N)

# we start by setting our goal to the last index. Then we move back and see that can be make ith index the new goal
# condition for that is if i + nums[i] >= goal
# like this gradually goal will come closer to the start position
# finally we return true if goal = 0


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) -1
        
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return True if goal == 0 else False