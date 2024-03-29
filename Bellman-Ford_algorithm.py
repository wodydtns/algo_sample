class Graph:
    def __init__(self, vertices):
        self.V = vertices  # 노드의 수
        self.graph = []  # 가장자리 / 엣지를 저장하는 리스트

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def bellman_ford(self, src):
        # 거리 테이블을 초기화합니다.
        dist = [float("Inf")] * self.V
        dist[src] = 0

        # V-1 번 노드를 완화합니다.
        for _ in range(self.V - 1):
            for u, v, w in self.graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        # 음수 가중 순환을 확인합니다.
        for u, v, w in self.graph:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                print("그래프에 음수 가중치 순환이 있습니다.")
                return

        # 결과를 출력합니다.
        self.print_solution(dist)

    def print_solution(self, dist):
        print("노드까지의 거리")
        for i in range(self.V):
            print(f"{i}\t\t{dist[i]}")


# 예제 사용
if __name__ == "__main__":
    g = Graph(5)
    g.add_edge(0, 1, -1)
    g.add_edge(0, 2, 4)
    g.add_edge(1, 2, 3)
    g.add_edge(1, 3, 2)
    g.add_edge(1, 4, 2)
    g.add_edge(3, 2, 5)
    g.add_edge(3, 1, 1)
    g.add_edge(4, 3, -3)

    g.bellman_ford(0)
