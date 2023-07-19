#Given a graph and a source vertex in the graph, find the shortest paths from the source to all vertices in the given graph.
from heapq import *

n=5
graph={}
distance={}
visited={}
for i in range(1,n+1):
    graph[i]=[]
    distance[i]=10**8+1
    visited[i]=0
for u,v,d in inputs:
    graph[u].append([d,v])
    graph[v].append([d,u])
start=1


def dijkstras(graph,start,visited,distance):
    distance[start]=0
    bag=[]
    heappush(bag,[0,start])
    while bag:
        d,n=heappop(bag)
        for childnode,childdistance in graph[n]:
            if not visited[childnode] and distance[d]+childdistance<distance[childnode]:
                distance[childnode]=distance[n]+childdistance
            heappush(bag,[distance[n]+childdistance,childnode])
    print(distance)



dijkstras(graph,start,distance,visited)
