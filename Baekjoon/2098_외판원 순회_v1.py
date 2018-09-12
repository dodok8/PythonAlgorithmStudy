# https://www.acmicpc.net/problem/2098

import sys

n = int(sys.stdin.readline())
w = list()
cost = 0
for _ in range(n):
    w.append(list(map(int(),sys.stdin.readline().split())))

print(cost)