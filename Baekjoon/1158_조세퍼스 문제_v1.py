'''
링크: https://www.acmicpc.net/problem/1158, https://www.acmicpc.net/problem/11866
Python3 31752 KB 6452 ms
PyPy3 233772 KB 572 ms
큐를 사용해서 넣는 것이 원형으로 지워 나가면서 넣는 것과 캍은 구조이다.
'''

from sys import stdin
from collections import deque

q = deque()
N, M = map(int, stdin.readline().split())
for i in range(1, N + 1):
    q.append(i)
print("<", end="")
while len(q) > 1:
    for i in range(M):
        a = q.popleft()
        if i == M - 1:
            print(a, end=", ")
        else:
            q.append(a)
print(q.popleft(), end="")
print(">")
