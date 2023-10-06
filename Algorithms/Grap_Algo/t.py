from collections import defaultdict

class Solution:
    def __init__(self):
        self.stack = []
        self.vis = []

    def dfs(self,node,adj):
        self.vis[node] = True
        for i in adj[node]:
            if not self.vis[i]:
                self.dfs(i,adj)
        self.stack.append(node)
    
    def dfs_reverse(self,node,adjT):
        self.vis[node] = True
        for i in adjT[node]:
            if not self.vis[i]:
                self.dfs_reverse(i,adjT)

    def kosaraju(self,V,adj):
        self.vis = [False] * V

        for i in range(V):
            if not self.vis[i]:
                self.dfs(i,adj)

        adjT = defaultdict(list)
        for i in range(V):
            self.vis[i] = False
            for it in adj[i]:
                adjT[it].append(i)
        
        scc = 0
        while self.stack:
            node = self.stack.pop()
            if not self.vis[node]:
                scc+=1
                self.dfs_reverse(node,adjT)
        return scc
    

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
print(adj)
ans = obj.kosaraju(n, adj)
print(f"The number of strongly connected components is: {ans}")