class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        D = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        
        def dfs(x, y):
            perimeter = 4
            
            for dx, dy in D:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid) and grid[ny][nx]:
                    perimeter -= 1
                    if not visited[ny][nx]:
                        visited[ny][nx] = 1
                        perimeter += dfs(nx, ny)
            
            return perimeter
        
        
        total_perimeter = 0
        
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] and not visited[y][x]:
                    visited[y][x] = 1
                    total_perimeter += dfs(x, y)
                    
        return total_perimeter
            
            
        