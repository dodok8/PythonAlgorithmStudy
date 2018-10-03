'''
링크: https://www.acmicpc.net/problem/9655
PyPy3  117076KB 124ms
기초적인 님문제
'''
import sys
N = int(sys.stdin.readline())
if N % 4 == 0 or N % 4 == 2:
    print('CY')
else:
    print('SK')
