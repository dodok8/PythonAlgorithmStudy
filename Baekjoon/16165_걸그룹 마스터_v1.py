# https://www.acmicpc.net/problem/16165
from sys import stdin

N, M = map(int, stdin.readline().split())
girl_groups = dict()
for i in range(N):
    group_name = stdin.readline()
    girl_groups[group_name] = list()
    for i in range(int(stdin.readline())):
        girl_groups[group_name].append(stdin.readline())
for i in range(M):
    quiz = int(stdin.readline())
    if quiz == 1:
        # 그룹 멤버 출력
    else:
        # 어느 그룹인지 출력
        for i in girl_groups.keys():
            if ??? in girl_groups[i] :
                prrint(i)

