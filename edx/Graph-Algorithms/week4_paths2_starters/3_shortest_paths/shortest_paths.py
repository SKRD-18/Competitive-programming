from queue import LifoQueue


def shortet_paths(adj, cost, s, distance, reachable, shortest):
    # s stands for source node
    # 1. Initialize distance to Source = 0
    # s is reachable from itself
    distance[s] = 0
    reachable[s] = 1

    # 2. The Main Relaxation Loop
    for _ in range(len(adj) - 1):  # Repeat every node V-1 times
        # the below line iterates through every node exactly one time.
        for u in range(len(adj)):
            for v, w in zip(adj[u], cost[u]):
                if distance[u] != 10**19 and distance[u] + w < distance[v]:
                    # update dist[v] to replace it with a cheaper cost
                    distance[v] = distance[u] + w
                    reachable[v] = 1

    Lifo = LifoQueue()

    # 3. "Collecting Patient Zero" - the Vth iteration
    for u in range(len(adj)):
        for v, w in zip(adj[u], cost[u]):
            if distance[u] != 10**19 and distance[u] + w < distance[v]:
                # it means v is part of a negative cycle or reachable from a
                # negative cycle
                if shortest[v] == 1:
                    shortest[v] = 0
                    Lifo.put(v)

    # The Pandemic spread: DFS
    while Lifo.empty() is False:
        curr = Lifo.get()  # Pop the first element
        for neighbor in adj[curr]:
            if shortest[neighbor] == 1:  # If not yet infected
                shortest[neighbor] = 0  # Mark as infected
                Lifo.put(neighbor)  # Continue the spread

    for _ in range(len(adj)):  # for ex: n = 10, it prints from 0 to 9
        if distance[_] == 10**19:
            reachable[_] = 0


if __name__ == "__main__":
    input = """
    6 7
    1 2 10
    2 3 5
    1 3 100
    3 5 7
    5 4 10
    4 3 -18
    6 1 -1
    1
    """

    input1 = """
    5 4
    1 2 1
    4 1 2
    2 3 2
    3 1 -5
    4
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

    s = data[0]
    s -= 1
    distance = [10**19] * n
    reachable = [0] * n
    shortest = [1] * n
    shortet_paths(adj, cost, s, distance, reachable, shortest)

    for x in range(n):
        if reachable[x] == 0:
            print("*")
        elif shortest[x] == 0:
            print("-")
        else:
            print(distance[x])
