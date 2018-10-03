'''
링크: https://www.acmicpc.net/problem/1676
런타임 에러: 5번
틀렸습니다: 1번
메모리 초과: 2번
PyPy3  117076KB  112ms
'''
from sys import stdin
n = int(stdin.readline())
squares = 5
num = 0
while squares < n:
    num = num + n//squares
    squares = squares*5
print(num)
