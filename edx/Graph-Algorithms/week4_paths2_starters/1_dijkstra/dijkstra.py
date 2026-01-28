from queue import PriorityQueue


def distance(adj, cost, s, t):
    # start from s and find the least cost to node t
    pq = PriorityQueue()
    dist = [float("inf")] * len(adj)
    dist[s] = 0
    pq.put((0, s))  # (distance, node)

    while not pq.empty():
        d, u = pq.get()
        if d > dist[u]:
            continue

        for neighbour, weight in zip(adj[u], cost[u]):
            # RELAXATION: Is the new path better than the old one?
            new_dist = dist[u] + weight
            if new_dist < dist[neighbour]:
                dist[neighbour] = new_dist
                pq.put(
                    (new_dist, neighbour)
                )  # weight comes first for priority queue to
            # sort by weight
        if u == t:
            return dist[t]
    return -1


if __name__ == "__main__":
    input = """
    4 4
    1 2 1
    4 1 2
    2 3 2
    1 3 5
    1 3
    """
    input1 = """
    3 3
    1 2 7
    1 3 5
    2 3 2
    3 2
    """

    data = list(map(int, input1.split()))
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
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
