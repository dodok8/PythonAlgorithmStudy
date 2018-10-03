# https://www.acmicpc.net/problem/10828
# PyPy3 121516KB 216ms
import sys
from collections import deque
q = deque()


def stack(string):
    a = list(string.split())
    if a[0] == 'push':
        q.append(a[1])
    if a[0] == 'pop':
        if q:
            b = q.pop()
            print(b)
        else:
            print(-1)
    if a[0] == 'size':
        print(len(q))
    if a[0] == 'empty':
        if q:
            print(0)
        else:
            print(1)
    if a[0] == 'top':
        if q:
            b = q.pop()
            q.append(b)
            print(b)
        else:
            print(-1)
    return


for i in range(int(sys.stdin.readline())):
    stack(sys.stdin.readline())
