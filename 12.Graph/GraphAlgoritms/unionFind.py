class UnionFind:
    def __init__(self, size):
        self.parent = []
        self.rank = []
        for i in range(size):
            self.parent.append(i)
            self.rank.append(1)

    def find(self, p):
        if self.parent[p] != p:
            self.parent[p] = self.find(self.parent[p])
        return self.parent[p]

    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP != rootQ:
            if self.rank[rootP] > self.rank[rootQ]:
                self.parent[rootQ] = rootP
            elif self.rank[rootP] < self.rank[rootQ]:
                self.parent[rootP] = rootQ
            else:
                self.parent[rootQ] = rootP
                self.rank[rootP] += 1

# Example usage
uf = UnionFind(5)
uf.union(0, 1)
uf.union(1, 2)
print("Union-Find Parent Array:", uf.parent)  # Output: [0, 0, 0, 3, 4]
print("Find(2):", uf.find(2))  # Output: 0
print("Find(3):", uf.find(3))  # Output: 3
