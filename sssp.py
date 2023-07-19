#Shortest path algorithms are a family of algorithms designed to solve the shortest path problem. The shortest path problem is something most people have some intuitive familiarity with: given two points, A and B, what is the shortest path between them? In computer science, however, the shortest path problem can take different forms and so different algorithms are needed to be able to solve them all.
def sssp(graph,node,d,distance,parent):
    distance[node]=d
    for child in graph[node]:
        if child != parent:
            sssp(graph,child,distance[node]+1,distance,node)
    sssp(graph,start,0,distance,-1)
    
            