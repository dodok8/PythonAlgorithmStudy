#스택 안쓰고 재귀로 짜는 중인데 막힘
import sys

class Graph:
    def __init__(self,N,M): #정점의 개수 N 간선의 개수 M
        self.gList = [[]for _ in range(N+1)]
        for i in range(M):
            a,b = map(int,sys.stdin.readline().split())
            self.gList[a].append(b)
            self.gList[b].append(a)
        self.visited = [False for _ in range(N+1)]
    def clear(self):
        self.visited = [False for _ in range(N+1)]
    def DFS(self, start):
        visited[start] = True
        for i in range(len(self.gList[start])):
            start = self.gList[start][i] 
            if self.visted[start] == False :
                self.DFS(start)
N,M,V = map(int,sys.stdin.readline().split())
g1 = Graph(N,M)
print(g1.visited)
#g1.BFS(V)