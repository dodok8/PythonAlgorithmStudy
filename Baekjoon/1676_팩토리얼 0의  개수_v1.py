# https://www.acmicpc.net/problem/1676
# 1번 틀림
# PyPy 117076KB 112ms
from sys import stdin
n = int(stdin.readline())
squares = 5
num0 = 0
while squares < n:
    num0 = num0 + n//squares
    squares = squares*5
print(num0)
