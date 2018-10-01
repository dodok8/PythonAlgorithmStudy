# https://www.acmicpc.net/problem/1182
from sys import stdin

n, goal_sum = map(int, stdin.readline().split())
num_list = list(map(int, stdin.readline().split()))
now_sum = 0
ways = 0

for i in range(1,1 << n):
    for j in range(n):
        if (i >> j)%2 == 1:
            # 포함 된다는 의미
            now_sum += num_list[j]]
    if now_sum == goal_sum:
        ways += 1


