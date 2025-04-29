# Prim's Algorithm for Minimum Spanning Tree 
# (MST). 

import sys

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    def printMST(self, parent):
        print("Edge \tWeight")
        for i in range(1, self.V):
            print(f"{parent[i]} - {i} \t{self.graph[i][parent[i]]}")

    def minKey(self, key, mstSet):
        min_val = sys.maxsize
        min_index = -1

        for v in range(self.V):
            if key[v] < min_val and not mstSet[v]:
                min_val = key[v]
                min_index = v

        return min_index

    def primMST(self):
        key = [sys.maxsize] * self.V
        parent = [None] * self.V
        key[0] = 0
        mstSet = [False] * self.V
        parent[0] = -1

        for cout in range(self.V):
            u = self.minKey(key, mstSet)
            mstSet[u] = True

            for v in range(self.V):
                if self.graph[u][v] > 0 and not mstSet[v] and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        self.printMST(parent)

# Driver code
if __name__ == "__main__":
    g = Graph(5)
    g.graph = [
        [0, 2, 0, 6, 0],
        [2, 0, 3, 8, 5],
        [0, 3, 0, 0, 7],
        [6, 8, 0, 0, 9],
        [0, 5, 7, 9, 0]
    ]

    g.primMST()

'''Explanation:
Graph Initialization: The Graph class is initialized with the number of vertices and an adjacency matrix representing the graph.
printMST Method: This method prints the edges of the MST and their corresponding weights.
minKey Method: This helper method finds the vertex with the minimum key value from the set of vertices not yet included in the MST.
primMST Method: This method constructs the MST using Prim's algorithm. It maintains an array of key values used to pick the minimum weight edge and a boolean array to represent the set of vertices included in the MST. It updates the key values and parent indices to build the MST.
Driver Code: Initializes the graph with a given adjacency matrix and calls the primMST method to find and print the MST.
'''