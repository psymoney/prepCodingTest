class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadend = set(deadends)
        Q = deque([('0000', 0)])
        ans = 10 ** 4
        visited = {'0000': True}
        
        while Q:
            pw, cnt = Q.popleft()
            if pw in deadends:
                continue   
            if pw == target:
                ans = min(ans, cnt)
                
            for i in range(4):
                next_p = pw[:i] + str((int(pw[i]) + 1) % 10) + pw[i+1:]
                next_m = pw[:i] + str((int(pw[i]) - 1) % 10) + pw[i+1:]

                if not visited.get(next_p):
                    visited[next_p] = True
                    Q.append([next_p, cnt + 1])
                if not visited.get(next_m):
                    visited[next_m] = True
                    Q.append([next_m, cnt + 1])
            
        
        return ans if ans != 10 ** 4 else -1