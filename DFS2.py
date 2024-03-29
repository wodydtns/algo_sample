class Graph:
    def __init__(self):
        self.graph = {}  # dictionary to store graph

    def add_edge(self, u, v):
        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]

    def DFS(self, v):
        visited = set()
        stack = [v]

        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                print(vertex, end=" ")
                visited.add(vertex)
                stack.extend(reversed(self.graph.get(vertex, [])))


# Example usage
if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    print("Following is Depth First Traversal (starting from vertex 2)")
    g.DFS(2)
