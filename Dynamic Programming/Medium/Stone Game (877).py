class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n  = len(piles)
        dp = [[0]* n for i in range(n)]
        for i in range(n):
            dp[i][i] = piles[i]

        for i in range(2,n+1):
            for p in range(n - i +1):
                j = p + i -1
                takeLeft = piles[p] - dp[p+1][j]
                takeRight = piles[j] - dp[p][j-1]

                dp[p][j] = max(takeLeft, takeRight)

        return dp[0][n-1] > 0