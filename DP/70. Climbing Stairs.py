# tc of brute force dfs will O(2^(height of the the tree)) and the height of the tree is roughly n
# so TC => O(2^n)

# after caching the TC is O(n) (where n is the target stair we wanna reach) because we are calculation each subproblem only once

# we can also do the true dynamic programing.
# here se start filling the values form the end;
# dp[n - 1] = 1;
# dp[n - 2] = 1;
# d[i] = dp[i + 1] + dp[i + 2];

# return dp[0];

# dp[i] will represend the number of steps needed to reach the nth stair starting from the ith index

# also at any point to calc dp[i] we only need 2 values d[i + 1] & dp[i + 2] so instead of storing the entire array, we can do some space optimization
# and store dp[i + 1] as variable "one" and dp[i + 2] as variable "two"