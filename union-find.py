parent=[x for x in range(n)]
def find(x):
    if x!=p[x]:
        p[x]=find(p[x])
    return p[x]
def union(x,y):
    p[find(x)]=find(y)

"""
Union Find is an algorithm which uses a disjoint-set data structure to solve the following problem: Say we have some number of items. We are allowed to merge any two items to consider them equal (where equality here obeys all of the properties of an Equivalence Relation). At any point, we are allowed to ask whether two items are considered equal or not.

"""        