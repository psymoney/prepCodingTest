class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = [grid[0]] + [[100] * n for _ in range(n-1)]
        
        for y in range(1, n):
            for x in range(n):
                dp[y][x] = grid[y][x] + min(dp[y-1][:x] + dp[y-1][x+1:])
        
        return min(dp[-1])
        