# https://www.acmicpc.net/problem/1328
# 10번 시도 2번 메모리 초과 5번 런타임 에러
# 43236 KB / 804 ms
N,L,R = map(int,input().split())
aList = [[[0 for _ in range(R+1)]for __ in range(L+1)]for ___ in range(N+1)]
aList[1][1][1] = 1
for i in range(2,N+1):
    for j in range(1,L+1):
        for k in range(1,R+1):
                aList[i][j][k] = aList[i-1][j][k]*(i-2)%1000000007+aList[i-1][j][k-1]%1000000007+aList[i-1][j-1][k]%1000000007
print(aList[N][L][R]%1000000007)