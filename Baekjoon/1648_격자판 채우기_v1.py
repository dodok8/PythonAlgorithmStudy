# https://www.acmicpc.net/problem/1648

from sys import stdin

n, m = map(int,stdin.readline().split())
dpList = [[-1 for _ in range(15)] for __ in range(1<<15)]

def solve(x,y,p,q):       
    if y == m:
        return solve(x+1,0,q,0)
    if x == n:
        if p == 0:
            return 1
        else:
            return 0
    if y == 0 and q == 0 :
        print("dpList의 크기는" + str(len(dpList)))
        if dpList[x][p] > 0:
            return dpList[x][p] 
    if (p >> y) & 1 :
        dpList[x][p] = solve(x,y+1,p,q)
    elif ((p >> (y + 1)) & 1) or (y + 1 < m): 
        dpList[x][p] = solve(x,y+1,p,q+(1<<y))
    else:
        dpList[x][p] = (solve(x,y+1,p,q+(1<<y))+solve(x,y+2,p,q))
    return dpList[x][p]

print(solve(0,0,0,0)%9901)