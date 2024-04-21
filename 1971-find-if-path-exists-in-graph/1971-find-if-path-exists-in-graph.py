class Vertex:
    def __init__(self, value: int) -> None:
        self.value = value
        self.visited = False
        self.adjacents = []

    def insert_adjacent(self, adjacent) -> None:
        self.adjacents.append(adjacent)

    def __eq__(self, other):
        return self.value == other

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        def bfs():
            pass
        
        vertices = {}
        
        for e1, e2 in edges:
            v1, v2 = vertices.get(e1), vertices.get(e2)
            
            if not v1:
                v1 = Vertex(e1)
                vertices.setdefault(e1, v1)
                
            if not v2:
                v2 = Vertex(e2)
                vertices.setdefault(e2, v2)
            
            v1.insert_adjacent(v2)
            v2.insert_adjacent(v1)
        
        if not vertices.get(source): return source == destination
        
        Q = [vertices.get(source)]
        
        while Q:
            e = Q.pop()
            
            for v in e.adjacents:
                if v == destination:
                    return True
                if not v.visited:
                    v.visited = True
                    Q.append(v)
                
        return False
        