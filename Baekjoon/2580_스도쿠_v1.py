'''
링크: https://www.acmicpc.net/problem/2580
런타임 에러:
틀렸습니다:
메모리 초과:
시간초과:
PyPy3  
논리형 배열을 쓰는 게 편하긴 할듯
TODO: 구현 완성
'''

from sys import stdin

all_numbers = (2 << 9) - 1
sdoku = list()

for i in range(9):
    sdoku.append(list(map(int, stdin)))

for i in range(9):
    for j in range(9):
        if sdoku[i][j] == 0:
