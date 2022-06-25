// we take all candels one by one and find how many valid arrangements can be made if the currently chosen candel is placed at last
// a candle placed at last will only be visible if it has the greatest value amongst all the candels
// base case : if(n == k) return 1; this is because suppose k = 3 and n = 3 then there is only 1 way to arrange the given n candles such 
// that all of them are visible
// eg n = 3 & k = 3 nums = {2, 1, 3}, then the only possible arrangement is {1, 2, 3}
// another base case : when only either n == 0 || k == 0, and not both of them are 0, then 0 possible combination    

// TC => O(N*K)

class Solution {
public:
    long long memo[1000][1000];
    
    long long dfs(int n, int k){
        
        if(k == n)
            return 1;
        
        if(n == 0 || k == 0)
            return 0;
        
        if(memo[n][k] != -1)
            return memo[n][k];
        
        long long subRes = 0; 
        
        subRes += dfs(n - 1, k - 1) % 1000000007;
        
        subRes = (subRes + (n - 1) * dfs(n - 1, k)) % 1000000007;
        
        // memo[n][k] = (dfs(n - 1, k - 1) % 1000000007 + // when we choose the max height candle out of n candles so the nth candle will be visible
        //              ((n - 1) * dfs(n - 1, k)) % 1000000007) % 1000000007;// we did not choose the max height candle so the candle placed at last wont be visible so dont decrement k
        return memo[n][k] = subRes;
    }
    
    int rearrangeSticks(int n, int k) {
        memset(memo, -1, sizeof(memo));
        return dfs(n, k);
    }
}; 