class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        suffix_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]

        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for m in range(1, n + 1):

                for x in range(1, min(2 * m, n - i) + 1):

                    take = suffix_sum[i] - suffix_sum[i + x]

                    opponent_best = dp[i + x][min(n, max(m, x))]
                    
                    remaining_total = suffix_sum[i + x]
                    my_remaining = remaining_total - opponent_best
                    

                    total = take + my_remaining
                    
       
                    dp[i][m] = max(dp[i][m], total)
        
        return dp[0][1]