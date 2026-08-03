class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [0]* (n+1)
        for i in range(n-1,-1,-1):
            turn = 0
            optimal = float('-inf')
            for j in range(1,4):
                if i + j - 1 < n:
                    turn = turn + stoneValue[i+j-1]
                    optimal = max(optimal, turn - dp[i+j])
            dp[i] = optimal
        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        return "Tie"

