class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        D = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        
        def bfs(c, r):
            rc = [r, c]
            Q = [(c, r)]
            
            while Q:
                x, y = Q.pop()
                if y >= rc[0] and x >= rc[1]:
                    rc = [y, x]
                    
                for dx, dy in D:
                    nx, ny = x + dx, y + dy

                    if 0 <= nx < len(land[0]) and 0 <= ny < len(land) and land[ny][nx]:
                        land[ny][nx] = 0
                        Q.append((nx, ny))
            
            return [r, c] + rc
        
        results = []
        
        for row in range(len(land)):
            for col in range(len(land[0])):
                if land[row][col]:
                    land[row][col] = 0
                    results.append(bfs(col, row))
                
        return results