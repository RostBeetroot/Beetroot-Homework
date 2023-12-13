def floyd_warshall(graph):
    # Number of vertices in the graph
    V = len(graph)

    # Initialize the distance matrix with the input graph
    dist = [[float('inf')] * V for _ in range(V)]
    for i in range(V):
        for j in range(V):
            if i == j:
                dist[i][j] = 0
            elif graph[i][j] != 0:
                dist[i][j] = graph[i][j]

    # Update the distance matrix using Floyd-Warshall algorithm
    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist


# Example usage:
graph = [
    [0, 2, 0, 1, 0],
    [0, 0, 0, 3, 0],
    [0, 0, 0, 0, 4],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

result = floyd_warshall(graph)

# Output the shortest paths
for i in range(len(result)):
    for j in range(len(result[i])):
        print(f"Shortest path from vertex {i} to {j}: {result[i][j]}")
