'''
링크: https://www.acmicpc.net/problem/10845
Python3 31752KB 796 ms
PyPy3  126172 KB 704 ms
파이썬에서 큐와 스택은 colltions.deque()을 사용하자.
'''

from sys import stdin
from collections import deque
q = deque()


def command(string):
    global q
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
