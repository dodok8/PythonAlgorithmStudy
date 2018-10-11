'''
링크: https://www.acmicpc.net/problem/1525
런타임 에러:
틀렸습니다:
메모리 초과:
시간초과:
Python3  KB  ms
PyPy3  KB  ms
'''
from sys import stdin
from collections import defaultdict, deque

board = list()
for i in range(3):
    board.extend(map(int, stdin.readline().split()))
temp_str = ''.join(str(i) for i in board)
now_board_number = int(temp_str,9)

def convert_9(n: int) -> str:
    T = "012345678"
    q, r = divmod(n, 9)
    if q == 0:
        return T[r]
    else:
        return convert_9(q) + T[r]


def get_connected_nodes(now: int):
    temp_board = list(convert_9(now))
    connected_list = list()
    swap_list = [1, -1, -3, 3]
    try:
        x = temp_board.index('0')
    except:
        x = 0
        temp_board.insert(0,'0')
    else:
        x = temp_board.index('0')
    for i in swap_list:
        if x+i < 0 or x+i >= 9:
            pass
        else:
            temp_board[x], temp_board[x+i] = temp_board[x+i], temp_board[x]
            temp_sum = ''.join(temp_board)
            connected_list.append(int(temp_sum, 9))
            temp_board[x], temp_board[x+i] = temp_board[x+i], temp_board[x]
    #for i in connected_list:
    #    print(convert_9(i))
    return connected_list


def BFS_final(start):
    visited = defaultdict(lambda: False)
    visited[start] = True
    final_board = 54480996
    distance = defaultdict(lambda: 0)
    queue = deque()
    queue.append(start)
    while queue:
        now = queue.popleft()
        if now == final_board: return distance[now]
        for i in get_connected_nodes(now):
            if not visited[i]:
                if i == final_board:
                    visited[i] = True
                    distance[i] = distance[now] + 1
                    return distance[i]
                else:
                    visited[i] = True
                    distance[i] = distance[now] + 1
                    queue.append(i)
    return -1

print(BFS_final(now_board_number))