
// dfs(i, j) will return the amount of water poured into the glass at i, j 

// left will tell amount of water poured in glass at i - 1, j - 1
// right will tell amount of water poured in the glass at i - 1, j

// now we want how much of water from the left glass comes to the current glass which is given by leftContribution = fmax(0.0, (left - 1) / 2.0);
// similarly we find how much of water from the left glass comes to the current glass which is given by rightContribution = fmax(0.0, (right - 1) / 2.0);

// so total water poured in current glass leftContribution + rightContribution

// TC - O(r*c)


class Solution {
public:
    double p;
    double memo[100][100];
    
    double dfs(int i, int j){
        if(i == 0 && j == 0)
            return p;
        
        if(i < 0 || j < 0 || j > i)
            return 0.0;
        
        if(memo[i][j] > -1.0)
            return memo[i][j];
        
        double left = dfs(i - 1, j - 1);
        double right = dfs(i - 1, j);
        
        double leftContribution = fmax(0.0, (left - 1) / 2.0);
        double rightContribution = fmax(0.0, (right - 1) / 2.0);
        
        return memo[i][j] = leftContribution + rightContribution;
    }
    
    
    double champagneTower(int poured, int query_row, int query_glass) {
        p = poured;
        
        memset(memo, -1.0, sizeof(memo));
        
        double res = dfs(query_row, query_glass);
        
        return fmin(1.0, res);
        
    }
};