# https://www.acmicpc.net/problem/2098

from math import inf
from sys import stdin,setrecursionlimit

setrecursionlimit(10**9)

def DP(now, visited):
    global dpList, visitedAll,w
    if now == 0:
        #시작 점 초기화
        if visited == 1:
            dpList[now][visited] = 0
        #시작한 상황인데 이미 방문한 곳이 1이상인 이상한 경우 제외
        else :
            dpList[now][visited] = inf
    if dpList[now][visited] != None:
        pass
    else:
        #여기서 부터는 아직 방문 안한 거
        tempVal = inf
        visitedExceptNow = visited & (~now)
        for i in range(n):
            if (visitedExceptNow >> i) & 1:
                before = i
                tempVal = min(tempVal, DP(before,visitedExceptNow)+w[before][now])
        dpList[now][visited] = tempVal
    return dpList[now][visited]

n = int(stdin.readline())
w = list()
for _ in range(n):
    w.append([inf if int(i) == 0 else int(i) for i in stdin.readline().split()])
dpList = [[None for _ in range(1 << n)] for __ in range(n)]
visitedAll = (1 << n) - 1
aList = list()
for i in range(1,n):
    aList.append(DP(i,visitedAll)+w[i][0])
print(min(aList))