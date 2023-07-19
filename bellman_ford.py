n=5
distance={}
for i in range(1,n+1):
    distance[i]=10**8+1
distance[1]=0
for _ in range(n-1):
    for u,v,d in inputs:
        if distance[u]<10**8 and d+distance[u]<distance[v]:
            distance[v]=d+distance[u]
print(distance)
                