class Solution {
public:
    int n, AliceScore, sum;
    int memo[500][500];
    int dfs(int i, int j, int AliceScore, vector<int>& piles){
        if(i > j)
            return AliceScore > sum/2;
        if(memo[i][j] != -1)
            return memo[i][j];
        int choice1 = dfs(i + 2, j, AliceScore + piles[i], piles) ||  dfs(i + 1, j - 1, AliceScore + piles[i], piles);
        int choice2 = dfs(i, j - 2, AliceScore + piles[j], piles) ||  dfs(i + 1, j - 1, AliceScore + piles[j], piles);
        return memo[i][j] = choice1 || choice2;
    }
    bool stoneGame(vector<int>& piles) {
        memset(memo, -1, sizeof(memo));
        n = piles.size();
        AliceScore = 0;
        for(auto x : piles)
            sum += x;
        return dfs(0, n - 1, AliceScore, piles);
    }
};