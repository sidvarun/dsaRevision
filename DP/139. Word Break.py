
# Basic brute force time complexity it O(s^3), with s = len(s) and k = len(words)

# Optimised Time complexity it O(s^2 * k), with s = len(s) and k = len(words)
# String loop + word loop + slicing/comparison (takes s time each)

# dp[i] will store the ans for the substring from index i to n - 1

# for each dp[i], we will go through the word dictionary and see if we have a word with if  a prefix of the the string starting at index "i"


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        
        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break
        
        return dp[0]

