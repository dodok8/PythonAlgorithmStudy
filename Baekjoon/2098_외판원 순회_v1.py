# https://www.acmicpc.net/problem/2098

MAX_INF = 100000000
import sys

n = int(sys.stdin.readline())
w = [[] for _ in range(n)]
dpList = [[None for __ in range(1<<n)] for _ in range(n)]
for j in range(1<<n):
    if j==0:
        dpList[0][1] = 0
    else :
        dpList[0][j] = MAX_INF
for i in range(n):
    for j in map(int, sys.stdin.readline().split()):
        if j != 0:
            w.append(j)
        else :
            w.append(MAX_INF)

def DP(u,a) :
    if dpList[u][a] is not None:
        return dpList[u][a]
    else :
        compareList = list()
        for i in range(n):
            if i != u & ((a >> i) & 1):
                compareList.append(DP(i,a)+w[i][u])
        dpList[u][a] = min(compareList)
        return dpList[u][a]

compareList = list()
for i in range(1,n):
    compareList.append(DP(i,(1<<n)-1)+w[i][0])    
print(min(compareList))