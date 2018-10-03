'''
링크: https://www.acmicpc.net/problem/1328
틀렸습니다: 3번
10번 시도 2번 메모리 초과 5번 런타임 에러
PyPy3 KB / 804 ms
'''
import sys

N, L, R = map(int, sys.stdin.readline().split())
dp = [[[0 for _ in range(R + 1)]for __ in range(L + 1)]
      for ___ in range(N + 1)]
dp[1][1][1] = 1
for i in range(2, N + 1):
    for j in range(1, L + 1):
        for k in range(1, R + 1):
            dp[i][j][k] = (dp[i-1][j][k]*(i-2) % 1000000007
                           + dp[i-1][j][k-1] % 1000000007
                           + dp[i-1][j-1][k] % 1000000007)
print(dp[N][L][R] % 1000000007)
