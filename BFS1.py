from collections import deque


def bfs(graph, start_node):
    visited = set()  # A set to keep track of visited nodes.
    queue = deque([start_node])  # A queue to manage the nodes to be visited.

    while queue:
        node = queue.popleft()  # Dequeue a vertex from the queue.
        if node not in visited:
            visited.add(node)  # Mark the node as visited.
            print(node, end=" ")  # Print the visited node.

            # Add all unvisited neighbors to the queue.
            for neighbour in graph[node]:
                if neighbour not in visited:
                    queue.append(neighbour)


# Example usage
if __name__ == "__main__":
    # Creating a graph as an adjacency list
    # Graph format: {node: [neighbor nodes]}
    graph = {0: [1, 2], 1: [2], 2: [0, 3], 3: [3]}

    print("Breadth First Traversal starting from vertex 2:")
    bfs(graph, 2)
