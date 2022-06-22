# TC for brute force is O(3^n) since we have n index so height of tree is n and at each index we have 3 choices to make.
# TC after optimization => O(38 * n)

Algorithm

dp(i) stores the minimum cost starting from day number days[i]
to calculate dp(i), we will try buying all possible tickets.
For each ticket we buy, we will now decide for what index j should we call the dp for now.
i.e. if we buy a ticket at days[i], when will be the next day we will again need a ticket.
This is done using while(days[j] < days[i] + [1 or 7 or 15])

a better way is using binary search to find j hence making the time complexity => O(nlog(n))
