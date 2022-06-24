
// TC => O(n^2)
// SC => O(n)

// we consider each number from 1 to n as the root of the binary search tree
// now we get the number of all possible left and right substrees of the current root by recursively calling for 
// for every j int 1 to n we call dp(j) and dp(i - 1 - j)

class Solution {
public:
    int numTrees(int n) {
        if(n == 1)
            return 1;
        int dp[n + 1];
        memset(dp, 0, sizeof(dp));
        dp[0] = 1;
        dp[1] = 1;
        for(int i = 2; i<=n; i++){
             for(int j = 0; j < i; j++){
                dp[i] += dp[j] * dp[i - 1 - j];
             }
        }
        return dp[n];
    }
};