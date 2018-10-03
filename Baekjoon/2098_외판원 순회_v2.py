'''
링크: https://www.acmicpc.net/problem/2098
비트 마스크를 잘못 적용함, 무한 루프 발생
'''
from math import inf
from sys import stdin


def DP(now, visited):
    global dpList, visitedAll, w, n
    if dpList[now][visited] != -1:
        print(now, visited, "dp")
        return dpList[now][visited]
    else:
        print(now, visited, "dp")
        # 여기서 부터는 아직 방문 안한 거
        tempVal = inf
        visitedExceptNow = visited & (~now)
        for before in range(n):
            if (before != now) and ((visited >> before) & 1):
                if w[before][now] is None:
                    continue
                else:
                    tempVal = min(tempVal, DP(
                        before, visited-(1 << now))+w[before][now])
        dpList[now][visited] = tempVal
        return dpList[now][visited]


n = int(stdin.readline())
w = [[] for _ in range(n)]
for i in range(n):
    for j in map(int, stdin.readline().split()):
        if j == 0:
            w[i].append(None)
        else:
            w[i].append(j)
dpList = [[-1 for _ in range(1 << n)] for __ in range(n)]
for j in range(1 << n):
    if j == 1:
        dpList[0][j] = 0
    else:
        dpList[0][j] = inf
visitedAll = (1 << n) - 1
print(DP(1, visitedAll)+w[1][0])
