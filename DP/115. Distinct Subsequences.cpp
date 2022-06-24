
# checkout the premium solution for TC and SC and also the sapce optimized DP approach

class Solution {
public:
    int memo[1000][1000];
    
    int dfs(int i, int j, string &s, string &t){
        
        if(i == s.length() && j == t.length())
            return 1;
        
        if(i == s.length())
            return 0;
        
        if(j == t.length())
            return 1;
        
        if(memo[i][j] != -1)
            return memo[i][j];
        
        int res = 0;
        
        if(s[i] == t[j])
            res += dfs(i + 1, j + 1, s, t);
        
        res += dfs(i + 1, j, s, t);
        
        return memo[i][j] = res;
    }
    
    
    int numDistinct(string s, string t) {
        memset(memo, -1, sizeof(memo));
        return dfs(0, 0, s, t);
    }
};