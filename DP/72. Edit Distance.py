# easy question just follow memoization 
class Solution {
public:
    vector<vector<int>> memo;
    int minDistance(string word1, string word2) {
        int n=word1.length();
        int m=word2.length();
        memo=vector<vector<int>>(n,vector<int>(m,-1));
        return dp(word1,word2,0,0,memo);
    }
    int dp(string s1,string s2, int n ,int m,vector<vector<int>> &memo)
    {
        if(n==s1.length())
            return s2.length() - m;
        if(m==s2.length())
            return s1.length() - n;
        if(memo[n][m]!=-1)
            return memo[n][m];
        if(s1[n]==s2[m])
            return memo[n][m]=dp(s1,s2,n + 1,m + 1,memo);
        else
            return memo[n][m]=1+ min({dp(s1,s2,n + 1,m + 1,memo), dp(s1,s2,n + 1,m,memo), dp(s1,s2,n,m + 1,memo)});
    }
};