# https://www.acmicpc.net/problem/2098
# none 과 int는 같은 리스트 있는 상태에서 min을 쓸 수 없다.
from sys import stdin

n = int(stdin.readline())
start = 0
visitedAll = (1 << n) - 1

w = [[] for _ in range(n)]
for i in range(n):
    for j in map(int,stdin.readline().split()):
        if j == 0:
            w[i].append(None)
        else :
            w[i].append(j)

dpList = [[ -1 for _ in range(1 << n)] for __ in range(n)]
for j in range(1 << n):
    if j == 1:
        dpList[0][j] = 0
    else :
        dpList[0][j] = None

def DP(now: int, visited: int) -> int:
    global dpList
    if dpList[now][visited] == -1:
        compareList = list()
        visitedBefore = visited & (~(1 << now))
        for i in range(n):
            if (visitedBefore >> i) & 1:
                before = i
            else:
                continue
            if DP(before, visitedBefore) is not None and w[before][now] is not None:
                compareList.append(DP(before, visitedBefore)+w[before][now])
        if compareList:
            dpList[now][visited] = min(compareList)
        else:
            dpList[now][visited] = None
        return dpList[now][visited]
    else:
        return dpList[now][visited]

endPointList = list()
for last in range(1,n) :
    if DP(last, visitedAll) is not None and w[last][start] is not None:
        endPointList.append(DP(last, visitedAll)+w[last][start])
print(min(endPointList))