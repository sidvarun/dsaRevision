// we can either rob the first house or the last house
// we cannot be robbing both the houses
// for other houses the constraing remains the same as house robber 1
// so we can split the given array into 2 parts
// 1st array will contain all the element except the last element 
// 2nd array will contain all the elements except the first element

class Solution {
public:
    unordered_map<int, int> memo;
    int robHelper(vector<int> nums, int n){
        if(n == 0)
            return 0;
        if(n == 1)
            return nums[0];
        if(memo.find(n) == memo.end())
            memo[n] = max(nums[n - 1] + robHelper(nums, n - 2), robHelper(nums, n - 1));
        return memo[n];
    }
    int robHouse(vector<int>& nums) {
        memo.clear();
        int n = nums.size();
        return robHelper(nums, n);
    }
    int rob(vector<int>& nums) {
        int n = nums.size();
        vector<int> v1(n - 1);
        vector<int> v2(n - 1);
        v1 = vector<int>(nums.begin(), nums.end() - 1);
        v2 = vector<int>(nums.begin() + 1, nums.end());
        return max({nums[0], robHouse(v1), robHouse(v2)});
    }
};