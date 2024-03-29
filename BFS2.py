class Graph:
    def __init__(self):
        self.graph = {}  # dictionary to store graph as an adjacency list

    def add_edge(self, u, v):
        # Assuming a directed graph; if undirected, add v to u and u to v
        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]

    def BFS(self, start):
        visited = set()  # Set to keep track of visited nodes
        queue = [start]  # Initialize a queue with the start vertex

        while queue:
            vertex = queue.pop(
                0
            )  # Dequeue a vertex from the queue (inefficient with a list)
            if vertex not in visited:
                print(vertex, end=" ")
                visited.add(vertex)

                # Enqueue all adjacent vertices that have not been visited
                for neighbour in self.graph.get(vertex, []):
                    if neighbour not in visited:
                        queue.append(neighbour)


# Example usage
if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    print("Following is Breadth First Traversal (starting from vertex 2):")
    g.BFS(2)
