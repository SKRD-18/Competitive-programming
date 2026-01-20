from collections import deque


def bipartite(adj):
    colours = [0] * len(adj)
    # 0: Unvisited, 1: Red, 2: Blue
    for node in range(len(adj)):
        # make sure we visit all nodes even if the graph is disconnected
        if colours[node] == 0:
            fifoQueue = deque([node])
            colours[node] = 1  # Colour the starting node Red

            # BFS Loop
            while fifoQueue:
                u = fifoQueue.popleft()
                for v in adj[u]:
                    if colours[v] == 0:  # If unvisited
                        colours[v] = colours[u] * -1
                        fifoQueue.append(v)
                    elif colours[v] == colours[u]:
                        return 0  # If the neighbour has the same colour, not

        return 1


if __name__ == "__main__":
    input = """
    4 4
    1 2
    4 1
    2 3
    3 1
    """

    input1 = """
    5 4
    5 2
    4 2
    3 4
    1 4
    """

    data = list(map(int, input1.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0 : (2 * m) : 2], data[1 : (2 * m) : 2]))
    adj = [[] for _ in range(n)]
    for a, b in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(bipartite(adj))
