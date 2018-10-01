# https://www.acmicpc.net/problem/1182
# PyPy3 117876KB 336ms
# O(n*2^n)

from sys import stdin

n, goal_sum = map(int, stdin.readline().split())
num_list = list(map(int, stdin.readline().split()))
ways = 0

for i in range(1,1 << n):
    now_sum = 0
    for j in range(n):
        if (i >> j)%2 == 1:
            # 포함 된다는 의미
            now_sum += num_list[j]
    if now_sum == goal_sum:
        ways += 1

print(ways)
