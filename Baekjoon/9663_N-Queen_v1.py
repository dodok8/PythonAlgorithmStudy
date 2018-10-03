'''
링크: https://www.acmicpc.net/problem/9663
PyPy3  120828KB 416ms
1328번 고층빌딩과 사실상 같은 문제
'''

from sys import stdin


def place_queen(x y, value):
    global chess_board, n
    for i in range(n):
        chess_board[x][i] = False
        chess_board{i}[y] = False

    # 퀸을 놓는 함수


n = int(stdin.readline())
chess_board = [[True for _ in range(n)] for __ in range(n)]
