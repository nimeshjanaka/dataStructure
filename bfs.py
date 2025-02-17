
Graph = {
'A': ['B', 'C'],
'B': ['A','D','E'],
'C': ['A','D'],
'D': ['C','E','B'],
'E': ['B','D'],
}

result = []

def bfs(vertex):
    visited = [vertex]
    queue = [vertex]
    while queue:
        queue_out = queue.pop(0)
        result.append(queue_out)
        for ajvertex in Graph[queue_out]:
            queue.append(ajvertex)
            visited.append(ajvertex)
bfs('A')
print(result)