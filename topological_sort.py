from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)  # 노드의 인접 리스트를 저장하는 딕셔너리
        self.V = vertices  # 노드의 개수

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def topological_sort(self):
        # 모든 노드의 진입 차수를 0으로 초기화
        in_degree = [0] * self.V
        # 모든 노드의 진입 차수 계산
        for i in self.graph:
            for j in self.graph[i]:
                in_degree[j] += 1

        # 진입 차수가 0인 모든 노드를 큐에 삽입
        queue = []
        for i in range(self.V):
            if in_degree[i] == 0:
                queue.append(i)

        # 위상 정렬을 위한 카운트 변수
        cnt = 0
        # 위상 정렬의 결과를 저장할 리스트
        top_order = []

        while queue:
            u = queue.pop(0)  # 큐에서 원소를 꺼내어
            top_order.append(u)  # 결과 리스트에 추가

            # 꺼낸 노드에 인접한 모든 노드의 진입차수에서 1을 빼고
            # 진입 차수가 0이 된 노드를 큐에 추가
            for i in self.graph[u]:
                in_degree[i] -= 1
                if in_degree[i] == 0:
                    queue.append(i)

            cnt += 1

        # 모든 노드를 방문했는지 확인
        if cnt != self.V:
            print("Graph has a cycle. Topological sort not possible.")
        else:
            print(top_order)


# 예제 사용
if __name__ == "__main__":
    g = Graph(6)
    g.add_edge(5, 2)
    g.add_edge(5, 0)
    g.add_edge(4, 0)
    g.add_edge(4, 1)
    g.add_edge(2, 3)
    g.add_edge(3, 1)

    print("Topological Sort of the given graph:")
    g.topological_sort()
