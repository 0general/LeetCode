class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        Max = 10**4 + 1
        dp = [Max]*(amount + 1)
        dp[0] = 0
        coins = [x for x in coins if x <= amount]
        for i in range(amount + 1):
            if dp[i] == -1:
                continue
            for coin in coins:
                if i + coin <= amount:
                    dp[i+coin] = min(dp[i] + 1, dp[i+coin])
        return dp[amount] if dp[amount] < Max else -1
        