# https://www.acmicpc.net/problem/8895
# 29164 KB 1520 ms
count = int(input())
aList = [[[0 for _ in range(21)]for __ in range(21)]for ___ in range(21)]
aList[1][1][1] = 1
def dp(N,L,R):
    if aList[N][L][R] != 0:
        return aList[N][L][R]
    else :
        for i in range(2,N+1):
            for j in range(1,L+1):
                for k in range(1,R+1):
                        aList[i][j][k] = aList[i-1][j][k]*(i-2)+aList[i-1][j][k-1]+aList[i-1][j-1][k]
        return aList[N][L][R]
for _ in range(count):
    n,l,r = map(int,input().split())
    print(dp(n,l,r))