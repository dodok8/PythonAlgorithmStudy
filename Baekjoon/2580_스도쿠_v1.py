# https://www.acmicpc.net/problem/2580
# 일단 논리형 배열 잡는 게 제일 편해 보인다.
# 근데 비트 마스크 써도 크게 다르지 않을 듯
from sys import stdin

all_numbers = (2 << 9) - 1
sdoku = list()

for i in range(9):
    sdoku.append(list(map(int, stdin)))

for i in range(9):
    for j in range(9):
        if sdoku[i][j] == 0:
