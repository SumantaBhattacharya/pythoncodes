# the complete implimentation of disjoint set with path compression and union by rank
class DisSet:
    def __init__(self, n):
        self.rank = [0] * n  # Initialize ranks to zero
        self.parent = [i for i in range(n)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def Union(self, x, y):
        xset = self.find(x)
        yset = self.find(y)

        if xset == yset:
            return
        
        if self.rank[xset] < self.rank[yset]:
            self.parent[xset] = yset
        elif self.rank[xset] > self.rank[yset]:
            self.parent[yset] = xset
        else:
            self.parent[xset] = yset
            self.rank[yset] += 1  # Increase rank of yset representative

obj = DisSet(5)
obj.Union(0, 2)
obj.Union(4, 2)
obj.Union(3, 1)

if obj.find(4) == obj.find(0):
    print("Yes")
else:
    print("No")

if obj.find(1) == obj.find(0):
    print("Yes")
else:
    print("No")
