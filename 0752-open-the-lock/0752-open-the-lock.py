class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        if '0000' in deadends:
            return -1
        Q = deque([('0000', 0)])
        ans = 10 ** 4
        visited = set('0000')
        
        while Q:
            pw, cnt = Q.popleft()
            
            if pw == target:
                ans = min(ans, cnt)
                
            for i in range(4):
                next_p = pw[:i] + str((int(pw[i]) + 1) % 10) + pw[i+1:]
                next_m = pw[:i] + str((int(pw[i]) - 1) % 10) + pw[i+1:]

                if next_p not in visited and next_p not in deadends:
                    visited.add(next_p)
                    Q.append([next_p, cnt + 1])
                if next_m not in visited and next_m not in deadends:
                    visited.add(next_m)
                    Q.append([next_m, cnt + 1])
            
        
        return ans if ans != 10 ** 4 else -1