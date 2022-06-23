
# TC => O(n^2)
# SC => O(1)
# iterate over each character and for each iteration find the longest palindrome with current character as the middle element
# check for both cases:
    # longest even length palindrome with curr character as the middle  
    # longest odd length palindrome with curr character as the middle  

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0
        
        for i in range(len(s)):
            # odd length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1
            
            # even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1
                
        return res



# recursive memoization approach

# TC => O(n^2)
# SC => O(n^2)

class Solution {
public:
    string longestPalindrome(string s) {
        int memo[1001][1001];
        memset(memo, -1, sizeof(memo));
        vector<int> answer = {0, 0, 1};
        helper(0, s.size() - 1, s, memo, answer);
        return s.substr(answer[0], answer[2]);
    }
    
    bool helper(int l, int r, string &s, int memo[][1001], vector<int> &answer) {
		# Check if [ L ... R ] is already calculated before
        if (memo[l][r] != -1) {
            return memo[l][r];         
        }
        
		# Base case, every single letter or empty string is also a palindrome
        if (l >= r) {
            return true;
        }
        
        # Possible palindrome beginning
        bool found = false;
        if (s[l] == s[r]) {
            found = true && helper(l + 1, r - 1, s, memo, answer);
        }
        
        # Try other possibilities
        helper(l + 1, r , s, memo, answer);
        helper(l, r - 1, s, memo, answer);
        
        # Update longest palindrome position and width
        if (found && (r - l + 1) > answer[2]) {
            answer = {l, r, (r - l + 1)};
        }
        
        # Memoization
        memo[l][r] = found;
        
        return found;
    }
};