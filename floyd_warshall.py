n=5
row=n+1
col=n+1
graph=[]
for _ in range(row):
    temp=[]
    for _ in range(col):
        temp.append(10**8+1)
    graph.append(temp)
for i in range(row):
    for j in range(col):
        if i==j:
            graph[i][j]=0
for u,v,d in inputs:
    graph[u][v]=d
for k in range(1,n+1):
    for i in range(1,row):
        for j in range(1,col):
            if i==j or j==k or i==k:
                pass
            else:
                if graph[i][j]>graph[i][k]+graph[k][j]:
                    graph[i][j]=graph[i][k]+graph[k][j]

for item in graph:
    print(item)

    
                        