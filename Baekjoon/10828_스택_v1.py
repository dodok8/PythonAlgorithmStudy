'''
링크: https://www.acmicpc.net/problem/10828
PyPy3  121516KB 216ms
파이썬에서 큐와 스택은 colltions.deque()을 사용하자.
'''
import sys
from collections import deque
q = deque()


def stack(string):
    global q
    input_list = list(string.split())
    if input_list[0] == 'push':
        q.append(input_list[1])
    if input_list[0] == 'pop':
        if q:
            b = q.pop()
            print(b)
        else:
            print(-1)
    if input_list[0] == 'size':
        print(len(q))
    if input_list[0] == 'empty':
        if q:
            print(0)
        else:
            print(1)
    if input_list[0] == 'top':
        if q:
            b = q.pop()
            q.append(b)
            print(b)
        else:
            print(-1)
    return


for i in range(int(sys.stdin.readline())):
    stack(sys.stdin.readline())
