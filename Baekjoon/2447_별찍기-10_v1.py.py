'''
링크: https://www.acmicpc.net/problem/2447
런타임 에러:
틀렸습니다:
메모리 초과:
시간초과:
Python3  KB  ms
PyPy3  KB  ms
'''
def sponge(x: int, y: int, n):
    global stars
    for i in range(x + n//3,x + 2*(n//3)-1, 1):
        for i in range(y + n//3,y + 2*(n//3)+1, 1):
            stars[i][j] = ' '
    if x != 3:
        for i in range(0,,n//3):
            for j in range(0, ,n//3):
                sponge(x + i,y + i n//3)
    else:
        pass

from sys import stdin
n = int(stdin.readline())
stars = [['*' for _ in range(n)]for __ in range(n)]
sponge(0,o,n)
for i in range(n):
    for j in range(m):
        print(sponge[i][j], end='')
    print()