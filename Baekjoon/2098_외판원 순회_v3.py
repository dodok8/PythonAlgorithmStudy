'''
링크: https://www.acmicpc.net/problem/2098
출력 값이 없는 이유 : none 과 int는 같은 리스트 있는 상태에서 min을 쓸 수 없다.
이전에 발생한 무한루프의 원인 : 비트 마스크를 잘못 이해함
시간초과: 1번(log(bitmask)정도 돌려야 하는 데 로그를 빼먹음)
PyPy3 161552KB 364ms
'''

from sys import stdin

n = int(stdin.readline())
start = 0
visited_all = (1 << n) - 1

w = [[] for _ in range(n)]
for i in range(n):
    for j in map(int, stdin.readline().split()):
        if j == 0:
            w[i].append(None)
        else:
            w[i].append(j)

dp_list = [[-1 for _ in range(1 << n)] for __ in range(n)]
for j in range(1 << n):
    if j == 1:
        dp_list[0][j] = 0
    else:
        dp_list[0][j] = None


def DP(now: int, visited: int) -> int:
    global dp_list
    if dp_list[now][visited] == -1:
        compare_list = list()
        visited_before = visited & (~(1 << now))
        for i in range(visited_before.bit_length()):
            if (visited_before >> i) & 1:
                before = i
            else:
                continue
            if DP(before, visited_before) is not None and w[before][now] is not None:
                compare_list.append(DP(before, visited_before)+w[before][now])
        if compare_list:
            dp_list[now][visited] = min(compare_list)
        else:
            dp_list[now][visited] = None
        return dp_list[now][visited]
    else:
        return dp_list[now][visited]


endpoint_list = list()
for last in range(1, n):
    if DP(last, visited_all) is not None and w[last][start] is not None:
        endpoint_list.append(DP(last, visited_all)+w[last][start])
print(min(endpoint_list))
