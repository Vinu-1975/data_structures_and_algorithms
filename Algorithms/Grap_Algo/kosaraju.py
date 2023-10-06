from collections import defaultdict

class Solution:
    def __init__(self):
        self.stack = []
        self.vis = []

    def dfs(self, node, adj):
        self.vis[node] = True
        for it in adj[node]:
            if not self.vis[it]:
                self.dfs(it, adj)
        self.stack.append(node)

    def reverse_dfs(self, node, adjT):
        self.vis[node] = True
        for it in adjT[node]:
            if not self.vis[it]:
                self.reverse_dfs(it, adjT)

    def kosaraju(self, V, adj):
        self.vis = [False] * V

        for i in range(V):
            if not self.vis[i]:
                self.dfs(i, adj)

        adjT = defaultdict(list)
        for i in range(V):
            self.vis[i] = False
            for it in adj[i]:
                adjT[it].append(i)

        scc = 0
        while self.stack:
            node = self.stack.pop()
            if not self.vis[node]:
                scc += 1
                self.reverse_dfs(node, adjT)

        return scc

# Driver Code
n = 5
edges = [
    (1, 0), (0, 2),
    (2, 1), (0, 3),
    (3, 4)
]

adj = defaultdict(list)
for edge in edges:
    adj[edge[0]].append(edge[1])

obj = Solution()
ans = obj.kosaraju(n, adj)
print(f"The number of strongly connected components is: {ans}")