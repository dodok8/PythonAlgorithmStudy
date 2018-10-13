'''
https://www.acmicpc.net/problem/16165
출력 형식 오류: 1번
런타임 에러: 1번
틀렸습니다: 1번
PyPy3 117592KB 108ms
'''
N, M = map(int, input().split())
girl_groups = dict()
for i in range(N):
    group_name = input()
    girl_groups[group_name] = list()
    for i in range(int(input())):
        girl_groups[group_name].append(input())
    girl_groups[group_name].sort()
for i in range(M):
    in_name = input()
    quiz = int(input())
    if quiz == 1:
        for i in girl_groups.keys():
            if in_name in girl_groups[i]:
                print(i)
                continue
        # 어디 소속인지 출력
    else:
        for i in girl_groups[in_name]:
            print(i)
