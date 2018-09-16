#https://www.acmicpc.net/problem/10828
# 런타임 에러 3번 골 때리는 건 내 컴에서는 재현이 안된다.
import sys
from collections import deque
q = deque()
def stack(string):
    a = list(string.split())
    if a[0] == 'push':
        q.append(int(a[1]))
    if a[0] == 'pop':
        if q :
            b = q.pop()
            print(b)
        else :
            print(-1)
    if a[0] == 'size':
        print(len(q))
    if a[0] == 'empty':
        if q :
            print(0)
        else:
            print(1)
    if a[0] == 'top':
        b = q.pop()
        q.append(b)
        print(b)
    return
for i in range(int(sys.stdin.readline())):
    stack(sys.stdin.readline())
