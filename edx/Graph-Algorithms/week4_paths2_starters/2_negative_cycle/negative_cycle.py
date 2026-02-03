def negative_cycle(adj, cost):
    # 1. Initialize distance to Source = 0
    dist = [float("inf")] * len(adj)
    dist[0] = 0

    # 2. The Main Relaxation Loop
    for _ in range(len(adj) - 1):  # Repeat V-1 times
        # the below line iterates through every node exactly one time.
        for u in range(len(adj)):
            for v, w in zip(adj[u], cost[u]):  # w is the COST (c_ij), not the rate!
                if dist[u] + w < dist[v]:
                    # update dist[v] to replace it with a cheaper cost
                    dist[v] = dist[u] + w

    # 3. The Detection Loop
    for u in range(len(adj)):
        for v, w in zip(adj[u], cost[u]):  # w is the COST (c_ij), not the rate!
            if dist[u] + w < dist[v]:
                return 1

    return 0


if __name__ == "__main__":
    input = """
    4 4
    1 2 -5
    4 1 2
    2 3 2
    3 1 1
    """

    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(
        zip(zip(data[0 : (3 * m) : 3], data[1 : (3 * m) : 3]), data[2 : (3 * m) : 3])
    )
    data = data[3 * m :]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for (a, b), w in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    print(negative_cycle(adj, cost))
