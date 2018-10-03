'''
링크: https://www.acmicpc.net/problem/11179
PyPy3  117076KB 104ms
'''
from sys import stdin

input_list = bin(int(stdin.readline()))
reversed = input_list[0:2] + ''.join(reversed(input_list[2:]))
print(int(reversed, 2))
