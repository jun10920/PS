class UnionFind:
    def __init__(self, size):
        self.root = list(range(size))
        self.rank = [1] * size
    
    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1
    def connected(self, x, y):
        return self.find(x) == self.find(y)

def solution(n, costs):
    
    costs.sort(key = lambda x : x[2])
    uf = UnionFind(n)
    answer = 0
    edges_used = 0
    
    for u, v, cost in costs:
        if not uf.connected(u, v):
            uf.union(u, v)
            answer += cost
            edges_used += 1
            if edges_used == n - 1:
                break
    return answer