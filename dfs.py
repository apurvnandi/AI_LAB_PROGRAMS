def dfs(adj, node, vis, ans):
    vis[node] = 1
    ans.append(node)

    for nei in adj[node]:
        if not vis[nei]:
            dfs(adj, nei, vis, ans)


# Main
n = 7
adj = [[] for _ in range(n)]

adj[1].append(2)
adj[1].append(4)

adj[2].append(1)
adj[2].append(3)

adj[3].append(2)
adj[3].append(4)
adj[3].append(5)

adj[4].append(1)
adj[4].append(3)
adj[4].append(5)

adj[5].append(3)
adj[5].append(4)
adj[5].append(6)

adj[6].append(5)

vis = [0] * n
ans = []

dfs(adj, 2, vis, ans)

print(*ans)