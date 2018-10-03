'''
https://www.acmicpc.net/problem/1182
PyPy3 117936 KB 292 ms
비트마스크를 이용해 모든 부분 집합에 대해서 다 더하게 시키는 경우, O(n*2^n)가 걸린다.
'''

from sys import stdin

n, goal_sum = map(int, stdin.readline().split())
num_list = list(map(int, stdin.readline().split()))
ways = 0

for i in range(1, 1 << n):
    now_sum = 0
    for j in range(i.bit_length()):
        if (i >> j) % 2 == 1:
            # 포함 된다는 의미
            now_sum += num_list[j]
    if now_sum == goal_sum:
        ways += 1

print(ways)
