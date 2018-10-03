# https://www.acmicpc.net/problem/10845
# 31752 KB 	796 ms
# PyPy3 126172 KB 704 ms
from sys import stdin
from collections import deque
q = deque()


def command(string):
    if string == 'front':
        if q:
            a = q.popleft()
            q.appendleft(a)
            print(a)
        else:
            print(-1)
    elif string == 'back':
        if q:
            a = q.pop()
            q.append(a)
            print(a)
        else:
            print(-1)
    elif string == 'empty':
        if q:
            print(0)
        else:
            print(1)
    elif string == 'size':
        print(len(q))
    elif string == 'pop':
        if q:
            print(q.popleft())
        else:
            print(-1)
    else:
        a = string.split()
        q.append(int(a[1]))


for _ in range(int(stdin.readline())):
    command(input())
