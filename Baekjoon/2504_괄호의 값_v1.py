'''
링크: https://www.acmicpc.net/problem/2504
런타임 에러:
틀렸습니다:
메모리 초과:
시간초과:
Python3  KB  ms
PyPy3  KB  ms
스택을 이용한 문제로 열린 괄호 - 열린괄호, 열린 괄호 - 닫힌 괄호, 숫자 - 닫힌 괄호 등으로 케이스를 나눠서 풀면 된다.
'''
from sys import stdin
from collections import deque

in_string = list(stdin.readable().rstrip())
bracket_stack = deque()
idx = 0
bracket_stack.append(in_string[idx])
while bracket_stack :
    if idx == len(in_string):
        break
    elif:
        idx += 1
    else:
        pass
print(bracket_stack.pop())