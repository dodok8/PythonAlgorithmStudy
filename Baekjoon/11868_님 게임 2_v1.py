# https://www.acmicpc.net/problem/11868
# 29164 KB 72ms
import sys
N = int(input())
p = list(map(int,sys.stdin.readline().split()))
a = p.pop()
for i in p:
    a = a^i
if a == 0:
    print('cubelover')
else:
    print('koosaga')