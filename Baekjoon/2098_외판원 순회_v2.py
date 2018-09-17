# https://www.acmicpc.net/problem/2098

from math import inf
from sys import stdin

def DP(now : int, visited: int) -> int :
    global dpList, visitedAll,w
    if dpList[now][visited] is not None:
        pass
    else:
        #여기서 부터는 아직 방문 안한 거
        compareList = list()
        vistedExceptNow = visted & (~now)
        for i in range(vistedExceptNow):
            if (vistedExceptNow >> i) & 1:
                before = i
                compareList.append(DP(before,vistedExceptNow)+w[before][now])
        dpList[now][visited] = min(compareList)
    return dpList[now][visited]
n = int(stdin.readline())
w = list()
for _ in range(n):
    w.append([inf if int(i) == 0 else int(i) for i in stdin.readline().split()])
dpList = [[None for _ in range(1 << n)] for __ in range(n)]
visitedAll = (1 << n) - 1
compareList = list()
for i in range(1,n):
    compareList.append(DP(i,visitedAll)+w[i][1])
print(min(compareList))

