'''
링크: https://www.acmicpc.net/problem/1158, https://www.acmicpc.net/problem/11866
Python3 31752 KB 6452 ms
PyPy3 233772 KB 572 ms
TODO 스택 안쓰고 재귀로 짜는 중인데 막힘
'''

import sys


class Graph:
    def __init__(self, N, M):  # 정점의 개수 N 간선의 개수 M
        self.graph_list = [[]for _ in range(N+1)]
        self.visited = [False for _ in range(N+1)]
        for i in range(M):
            a, b = map(int, sys.stdin.readline().split())
            self.graph_list[a].append(b)
            self.graph_list[b].append(a)

    def clear(self):
        self.visited = [False for _ in range(N+1)]

    def DFS(self, start):
        self.visited[start] = True
        for i in range(len(self.graph_list[start])):
            start = self.graph_list[start][i]
            if self.visited[start] is False:
                self.DFS(start)


N, M, V = map(int, sys.stdin.readline().split())
g1 = Graph(N, M)
print(g1.visited)
# g1.BFS(V)
