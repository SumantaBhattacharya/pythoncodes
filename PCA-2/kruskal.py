# Kruskal's Minimum Spanning Tree (MST)Algorithm

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        if parent[i] != i:
            parent[i] = self.find(parent, parent[i])
        return parent[i]

    def union(self, parent, rank, x, y):
        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[x] > rank[y]:
            parent[y] = x
        else:
            parent[y] = x
            rank[x] += 1

    def KruskalMST(self):
        result = []  # This will store the resultant MST
        i = 0  # An index variable, used for sorted edges
        e = 0  # An index variable, used for result[]

        # Step 1: Sort all the edges in non-decreasing order of their weight
        self.graph = sorted(self.graph, key=lambda item: item[2])

        parent = []
        rank = []

        # Create V subsets with single elements
        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        # Number of edges to be taken is equal to V-1
        while e < self.V - 1:
            # Step 2: Pick the smallest edge and increment the index for next iteration
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            # If including this edge does not cause a cycle, include it in result
            # and increment the index of result for next edge
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)

        minimumCost = 0
        print("Edges in the constructed MST")
        for u, v, weight in result:
            minimumCost += weight
            print("%d -- %d == %d" % (u, v, weight))
        print("Minimum Spanning Tree", minimumCost)

# Driver code
if __name__ == '__main__':
    g = Graph(5)
    g.addEdge(0, 1, 1)
    g.addEdge(0, 2, 2)
    g.addEdge(0, 3, 3)
    g.addEdge(1, 2, 4)
    g.addEdge(1, 4, 5)
    g.addEdge(2, 3, 6)
    g.addEdge(3, 4, 7)
    
    g.KruskalMST()
