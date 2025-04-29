class DisjointSet:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [0] * size
    
    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def union_by_rank(self, i, j):
        jrep = self.find(j)  # Corrected: j should be passed to find
        irep = self.find(i)  # Corrected: i should be passed to find

        if irep == jrep:
            return
        irank = self.rank[irep]
        jrank = self.rank[jrep]
        if irank < jrank:
            self.parent[irep] = jrep
        elif jrank < irank:
            self.parent[jrep] = irep
        else:
            self.parent[irep] = jrep
            self.rank[jrep] += 1

# Example usage
size = 5
ds = DisjointSet(size)
ds.union_by_rank(0, 1)
ds.union_by_rank(2, 3)
ds.union_by_rank(1, 3)

for i in range(size):
    print(f"Element {i} belongs to the set with representative {ds.find(i)}")

# ds = DisjointSet(size=5)
# ds.main()