def mex(inList):
    if 0 not in inList:
        return 0
    elif 1 not in inList:
        return 1
    elif 2 not in inList:
        return 2
    elif 3 not in inList:
        return 3
    else :
        return 4

g = [[0 for _ in range(15)]for __ in range(15)]
g[2][2] = 4
g[0][2] = 1
g[2][0] = 1
g[0][1] = 2
g[0][1] = 2
g[1][2] = 2
g[2][1] = 1
for i in range(3,15):
    for j in range(3,15):
        g[i][j] = mex(list(g[i-2][y-1],g[i-2][j+1],g[i+1][j-2],g[i-1][j-2])
