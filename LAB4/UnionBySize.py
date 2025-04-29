# union by size
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.Size = [1] * n

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def unionBySize(self, i ,j):
        irep = self.find(i)
        jrep = self.find(j)
        if irep == jrep:
            return
        isize = self.Size[irep]
        jsize = self.Size[jrep]

        if isize < jsize:
            self.parent[irep] = jrep
            self.Size[jrep] += self.Size[irep]
        else:
            self.parent[jrep] = irep
            self.Size[irep] += self.Size[jrep]

n = 5
unionFind = UnionFind(n)

unionFind.unionBySize(0,1)
unionFind.unionBySize(2,3)
unionFind.unionBySize(0,4)

for i in range(n):
    print("Element {}: Representative = {}".format(i, unionFind.find(i)))
