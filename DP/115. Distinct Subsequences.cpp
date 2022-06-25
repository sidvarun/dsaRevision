
// # checkout the premium solution for TC and SC and also the sapce optimized DP approach


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        cache = {}
        
        for i in range(len(s) + 1):
            cache[(i, len(t))] = 1
        for j in range(len(t)):
            cache[(len(s), j)] = 0
        
        for i in range(len(s) - 1, -1, -1):
            for j in range(len(t) - 1, -1, -1):
                if s[i] == t[j]:
                    cache[(i, j)] = cache[(i+1,j+1)] + cache[(i+1,j)]
                else:
                    cache[(i,j)] = cache[(i+1,j)]
        return cache[(0,0)]

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