class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        count = [float('inf')] * (amount+1)
        count[0] = 0
        for i in range(1, amount+1):
            for j in coins:
                if j<=i:
                    count[i]=min(count[i], count[i-j]+1)
        return count[amount] if count[amount] != float('inf') else -1
