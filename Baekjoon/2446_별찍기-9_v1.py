'''
링크: https://www.acmicpc.net/problem/2446
런타임 에러:
틀렸습니다:
메모리 초과:
시간초과:
PyPy3  117592KB 104ms
'''
from sys import stdin

n = int(stdin.readline())
for i in range(n-1, -1, -1):
    print(' '*(n-1-i)+'*' * (i*2+1))
for i in range(1, n):
    print(' ' * (n-1-i) + '*' * (i*2+1))
