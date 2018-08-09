# https://www.acmicpc.net/problem/10845
from sys import stdin
from collections import deque
q = deque()
def command(string):
    if string == 'front':
        if q:
            a = q.popleft()
            q.appendleft(a)
            return a
        else:
            return -1
    elif string == 'back':
        if q:
            a = q.pop()
            q.append(a)
            return a
        else :
            return -1
    elif string == 'empty':
        if q:
            return 0
        else :
            return 1
    elif string == 'size':
        return len(q)
    elif string == 'pop':
        if q:
            return q.popleft()
        else:
            return -1
    else:
        a,b = string.split()
        q.append(int(b))
for _ in range(int(stdin.readline())):
    command(stdin.readline())