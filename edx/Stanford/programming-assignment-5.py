"""
Parsing: Reading the file and storing the graph.

The Algorithm: Implementing the loop to find shortest paths.
Reporting: Outputting specific distances.
"""

from typing import Any


def load_graph(filename):
    """
    Loads the graph from a text file into an adjacency list.
    Returns: A dictionary where keys are vertex IDs (int) and values
             are lists of tuples (neighbor_id, weight).
    """
    adj_list = {}

    try:
        with open(filename, "r") as f:
            for line in f:  # read line by line
                # 1. Split the line into parts (the vertex and the rest)
                parts = line.split()

                # 2. The first part is the current vertex
                vertex = int(parts[0])

                # 3. Initialize the list for this vertex in the dictionary
                adj_list[vertex] = []

                # 4. Loop through the remaining parts (neighbors)
                for neighbour in parts[1:]:
                    neighbour_id, weight = neighbour.split(",")
                    neighbour_id = int(neighbour_id)
                    weight = int(weight)
                    adj_list[vertex].append((neighbour_id, weight))
                #    For each part:
                #      a. Split by comma to get neighbor_id and weight
                #      b. Convert both to integers
                #      c. Append tuple (neighbor_id, weight) to adj_list[vertex]

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return None

    return adj_list


def djikstra(graph) -> dict[Any, Any]:
    X = []  # vertices processed so far
    V = list(graph.keys())
    A = {}  # computed shortest path distances
    for v in graph:
        A[v] = 1000000
    A[1] = 0

    while len(X) != len(V):
        # while total number of processed vertices doesn't total up to all the vertices
        # After picking the current_vertex (the one with the smallest distance), you need to look at its neighbors.
        # Create a list of unprocessed nodes

        # 1. Pick the unprocessed node with the smallest distance
        unprocessed_nodes = list(set(V) - set(X))
        min_key = min(
            unprocessed_nodes, key=lambda x: A[x]
        )  # the way we compare the vertices is by their A[key] = value

        # 2. MARK IT AS PROCESSED!
        X.append(min_key)

        for neighbour_tuple in graph[min_key]:
            neighbor_id = neighbour_tuple[0]
            edge_weight = neighbour_tuple[1]
            A[neighbor_id] = min(
                A[neighbor_id], A[min_key] + edge_weight
            )  # Djikstra's Greedy Criterion

    return A


graph = load_graph(
    "/Users/shiva/Documents/Competitive-programming/edx/Stanford/data/dijkstraData.txt"
)
if graph:
    # Print the first vertex to verify
    first_vertex = 1
    # print(f"Vertex {first_vertex}: {graph.get(first_vertex)}")

    print(djikstra(graph=graph))
