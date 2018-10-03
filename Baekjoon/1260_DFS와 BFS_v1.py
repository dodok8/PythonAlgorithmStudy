'''
링크: https://www.acmicpc.net/problem/1260
PyPy3 119220 KB 220 ms
리스트로 큐와 스택을 대체 했으므로 좋은 풀이는 아니다. collection.deque을 쓰는 풀이를 짜야 한다.
'''
import sys


class Graph:
    def __init__(self, N, M):  # 정점의 개수 N 간선의 개수 M
        self.graph_list = [[]for _ in range(N+1)]
        for i in range(M):
            a, b = map(int, sys.stdin.readline().split())
            self.graph_list[a].append(b)
            self.graph_list[b].append(a)
        for i in range(1, N+1):
            self.graph_list[i].sort()

    def dfs(self, start):
        visited = []
        stack = [start]
        while stack:
            nowPoint = stack.pop()
            if nowPoint not in visited:
                visited.append(nowPoint)
                inList = list(set(self.graph_list[nowPoint])-set(visited))
                inList.sort(reverse=True)
                stack.extend(inList)
        return visited

    def bfs(self, start):
        visited = []
        queue = [start]
        while queue:
            nowPoint = queue.pop(0)
            if nowPoint not in visited:
                visited.append(nowPoint)
                inList = list(set(self.graph_list[nowPoint])-set(visited))
                inList.sort()
                queue.extend(inList)
        return visited


N, M, V = map(int, sys.stdin.readline().split())
g1 = Graph(N, M)
for i in g1.dfs(V):
    print(i, end=' ')
print()
for j in g1.bfs(V):
    print(j, end=' ')
