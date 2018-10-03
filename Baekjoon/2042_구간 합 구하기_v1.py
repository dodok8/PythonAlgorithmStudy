# https://www.acmicpc.net/problem/2042
# 런타임 에러 1번 틀림 1번
from sys import stdin

n, m, k = map(int, stdin.readline().split())
# n은 숫자의 개수, m은 수의 변경 개수, l는 구간합 개수
N = n.bit_length()
treeList = [0 for i in range((1 << (N+1)))]


def update(location, diff):
    global treeList, n
    x = treeList[location]
    treeList[location] += diff
#    print(treeList)
    if location > 1:
        update(location//2, diff)


def sum(l, r):
    left = min(l, r)
    right = max(r, l)
    global treeList, n
    if left == right:
        return treeList[left]
    res = sum((left+1)//2, (right-1)//2)
    if left % 2 == 1:
        res += treeList[left]
    if right % 2 == 0:
        res += treeList[right]
    return res


for i in range(n):
    update((1 << N) + i, int(stdin.readline()))

for i in range(m+k):
    a, b, c = map(int, stdin.readline().split())
    if a == 1:
        # 숫자 바꾸기
        update((1 << N) + b - 1, c - treeList[(1 << N) + b - 1])
    else:
        print(sum((1 << N) + b - 1, (1 << N) + c - 1))
