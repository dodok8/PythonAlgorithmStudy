'''
링크: https://www.acmicpc.net/problem/1717
PyPy3  227656KB  952ms
'''

import random
import sys

n, m = map(int, sys.stdin.readline().split())

parent_list = [i for i in range(n+1)]
height_list = [0 for _ in range(n+1)]


def find_parent(a):
    global parent_list
    if parent_list[a] == a:
        return a
    else:
        parent_list[a] = find_parent(parent_list[a])
        return parent_list[a]


def sum_set(a, b):
    A = find_parent(a)
    B = find_parent(b)
    if A == B:
        pass
    else:  # 같은 집합에 있지 않을 때
        if height_list[A] == height_list[B]:  # 둘이 높이가 같은 경우
            if random.randint(0, 2) == 1:
                parent_list[B] = A
                height_list[A] += 1
            else:
                parent_list[A] = B
                height_list[B] += 1
        elif height_list[A] > height_list[B]:
            parent_list[B] = A
        else:
            parent_list[A] = B


def find_set(a, b):
    A = find_parent(a)
    B = find_parent(b)
    if A == B:
        print('YES')
    else:
        print('NO')


for i in range(m):
    op, a, b = map(int, sys.stdin.readline().split())
    if op == 0:  # 집합 더하기
        sum_set(a, b)
    else:  # 존재 확인
        find_set(a, b)
