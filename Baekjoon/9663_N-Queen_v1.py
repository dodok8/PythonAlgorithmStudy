# https://www.acmicpc.net/problem/9663

from sys import stdin


def update(x: int y: int, value: bool) -> None:
    global chess_board, n
    for i in range(n):
        chess_board[x][i] = False
        chess_board{i}[y] = False

    # 퀸을 놓는 함수


n = int(stdin.readline())
chess_board = [[True for _ in range(n)] for __ in range(n)]
