#Topological sorting for Directed Acyclic Graph (DAG) is a linear ordering of vertices such that for every directed edge uv, vertex u comes before v in the ordering. Topological Sorting for a graph is not possible if the graph is not a DAG.

def topologicalSort(self):
    indegree=[0]*(self.v)
    for i in range(self.graph):
        for j in range(self.graph[i]):
            indegree[j]+=1
    queue=[]
    for i in range(self.v):
        if indegree[i]==0:
            queue.append(i)
    counter=0
    top_order=[]
    while queue:
        u=queue.pop(0)
        top_order.append(u)
        for i in self.graph[u]:
            indegree[i]-=1
            if indegree[i]==0:
                queue.append(i)
    counter+=1
                                