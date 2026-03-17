from collections import deque

def bfs(adj, src):
    vis = [0] * len(adj)
    q = deque([src])
    vis[src] = 1
    ans = []

    while q:
        node = q.popleft()
        ans.append(node)

        for nei in adj[node]:
            if not vis[nei]:
                vis[nei] = 1
                q.append(nei)

    return ans


adj = [[],
       [2,4],
       [1,3],
       [2,4,5],
       [1,3,5],
       [3,4,6],
       [5]]

print(bfs(adj, 2))
 