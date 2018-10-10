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
from collections import defaultdict as defdict
from collections import deque

board = []
now_board_number = 0
for i in range(3):
    board.append(list(map(int, stdin.readline().split)))
    now_board_number = (board[i][0]*9**(i*3+0)
                    + board[i][1]*9**(i*3+1)
                    + board[i][2]*9**(i*3+2))
final_board = 42374116
visited = defdict(lambda: False)
visited[now_board_number] = True
distance = [0 for _ in range(362880)] #현재 거리에서 얼마나 멀리 떨어져 있는 지 측정

def BFS_final(start):
    global visited, final_board, distance
    queue = deque()
    queue.append(start)
    while queue:
        now = queue.popleft()
        connected_node = list()
        #TODO: 복원하는 과정을 짜야한다. 복원해서 그걸 숫자를 바꿔서 넣고 
        for i in connected_node:
            if not visited[i]:
                if i == final_board:
                    visited[i] = True
                    distance[i] = distance[now] + 1 
                    # 도착한거니깐 이 때까지 값 반환
                    return distance[i]
                else:
                    visited[i] = True
                    distance[i] = distance[now] + 1
                    queue.append(i) #다음 now 포인트가 될 테니 큐에 넣기
    #제대로 작동할지는 모르겠는데 어찌되었든 BFS 완성