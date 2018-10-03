'''
https://www.acmicpc.net/problem/11868
Python3 29164 KB 72ms
PyPy3 
게임이론 문제
'''
from sys import stdin

N = int(input())
p = list(map(int, stdin.readline().split()))
a = p.pop()
for i in p:
    a = a ^ i
if a == 0:
    print('cubelover')
else:
    print('koosaga')
