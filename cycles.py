def cycle(graph,visited,parent_node=-1,node):
    visited[node]=True
    for neighbour in graph[node]:
        if not visited[neighbour]:
            if cycle(graph,visited,node,neighbour):
                return True
            elif neighbour!=parent_node:
                return True
    return False

# make visited node true first then we have to search for the neighbour nodes if they are visited or not previously , if they are not visited then do dfs for neighbours if they are visited then we got the cycle success if not and if the neighbour one is not  parent node then cycle is present else cycle is not present in there.

