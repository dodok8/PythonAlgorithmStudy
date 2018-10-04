'''
링크: https://www.acmicpc.net/problem/9663
PyPy3  
'''

from sys import stdin


def place_queen(x: int, y: int, value: bool):
    global chess_board, n
    for i in range(n):
        chess_board[x][i] = False
        chess_board{i}[y] = False
    i = x - 1
    j = y - 1
    while(x >= 0 and y >= 0):
        chess_board[i][j] = False
        i -= 1
        j -= 1
    i = x + 1
    j = y + 1
    while(k < n and l < n):
        chess_board[i][j] = False
        i += 1
        j += 1
    i = x - 1
    j = y + 1
    while(x >= 0 and y < n):
        chess_board[i][j] = False
        i -= 1
        j += 1
    i = x + 1
    j = y - 1
    while(x < n and y >= 0):
        chess_board[i][j] = False
        i += 1
        j -= 1
    i = x + 1
    j = y - 1


n = int(stdin.readline())
chess_board = [[True for _ in range(n)] for __ in range(n)]
last_x = 0
last_y = 0
count = 0

