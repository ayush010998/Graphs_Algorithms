
#dfs


#Depth First Traversal (or DFS) for a graph is similar to Depth First Traversal of a tree. The only catch here is, that, unlike trees, graphs may contain cycles (a node may be visited twice). To avoid processing a node more than once, use a boolean visited array. A graph can have more than one DFS traversal.

visited=set()
def dfs(visited,graph,node):
    if node not in visited:
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited,graph,node)

            
