# very similar to house robber
# sort the input array
# instead of choosing 1 occurence of 4 we can chooses all occurences of 4 and delete all occurences of 3 and 5 if they exist

class Solution {
public:
    unordered_map<int, int> m;
    vector<int> newNums;
    int n;
    int memo[20000];
    int dfs(int i){
        if(i >= n)
            return 0;
        if(memo[i] != -1)
            return memo[i];
        int choice1 = newNums[i] * m[newNums[i]];
        if(i + 1 < n && newNums[i + 1] == newNums[i] + 1)
        # if adjecent element is precent we will have to skip it because in choice1 we are choosing to have newNums[i]
            choice1 += dfs(i + 2);
        else
            choice1 += dfs(i + 1);
        
        int choice2 = dfs(i + 1);
        
        return memo[i] = max(choice1, choice2);
            
    }
    int deleteAndEarn(vector<int>& nums) {
        memset(memo, -1, sizeof(memo));
        for(auto x : nums){
            if(m.find(x) == m.end()){
                m[x] = 1;
                newNums.push_back(x);
            }
            else
                m[x]++;
        }
        n = newNums.size();
        sort(newNums.begin(), newNums.end());
        return dfs(0);       
    }
};