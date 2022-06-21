# This is a linked list cycle detection problem
# We need to find the beginning of the cycle

# To find start of cycle - 
# 1. Take fast and slow pointers
# 2. Increment fast by 2 steps at a time and slow by 1
# 3. mark the point when they meet for the first time
# 4. now start the slow pointer again from beginning 
# 5. now increment both fast and slow by 1
# 6. the point they meet is the start of the cycle.

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow

# Time Complexity: O(n)
# Space Complexity: O(1)