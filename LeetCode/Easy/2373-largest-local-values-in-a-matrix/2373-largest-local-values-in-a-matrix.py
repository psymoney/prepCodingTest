class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        self.grid = grid
        n = len(grid)
        ans = []
        
        for y in range(1, n - 1):
            ans.append([self.get_local_max(x, y) for x in range(1, n - 1)])
                
        return ans
                
    def get_local_max(self, x, y):
        local_max = 0
        
        for j in range(y - 1, y + 2):
            for i in range(x - 1, x + 2):
                local_max = max(local_max, self.grid[j][i])
                
        return local_max