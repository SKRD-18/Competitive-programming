from collections import deque


def distance(adj, s, t):
    # s is the start node and t is the end node
    visited = [False] * len(adj)
    visited[s] = True
    fifo_queue = deque()
    fifo_queue.append((s, 0))  # (node, distance)
    while fifo_queue:
        v = fifo_queue.popleft()
        for neighbour in adj[v[0]]:
            if visited[neighbour] is False:
                visited[neighbour] = True
                fifo_queue.append((neighbour, v[1] + 1))
            if visited[t]:
                return v[1] + 1

    return -1


if __name__ == "__main__":
    input = """
    4 4
    1 2
    4 1
    2 3
    3 1
    2 4
    """

    input2 = """
    5 4
    5 2
    1 3
    3 4
    1 4
    3 5
    """

    data = list(map(int, input2.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0 : (2 * m) : 2], data[1 : (2 * m) : 2]))
    adj = [[] for _ in range(n)]
    for a, b in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
