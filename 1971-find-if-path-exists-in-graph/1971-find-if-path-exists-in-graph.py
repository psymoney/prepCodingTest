class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:     
        if source == destination: return True
        vertices = {}
        
        for e1, e2 in edges:
            if (e1 == source and e2 == destination) or (e1 == destination and e2 == source): return True          
            if not vertices.get(e1):
                vertices.setdefault(e1, [])
                
            if not vertices.get(e2):
                vertices.setdefault(e2, [])
            vertices[e1].append(e2)
            vertices[e2].append(e1)
        
        visited = [False] * n
        visited[source] = True
        Q = [source]
        while Q:
            e = Q.pop()
            
            for v in vertices[e]:
                if v == destination:
                    return True
                if not visited[v]:
                    visited[v] = True
                    Q.append(v)
                
        return False
        