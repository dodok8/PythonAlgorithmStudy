# https://www.acmicpc.net/problem/2042

from sys import stdin

n, m, k = map(int,stdin.readline().split())
# n은 숫자의 개수, m은 수의 변경 개수, l는 구간합 개수
N = n.bit_length()
treeList = [0  for i in range((1 << (N+1)))]

def update(location, diff):
    global treeList, n
    x = treeList[location]
    treeList[location] += diff
#    print(treeList)
    if location > 1:
        update(location//2, diff)

def sum(l,r):
    global treeList, n
    if l == r:
        return treeList[l]
    res = sum((l+1)//2,(r-1)//2)
    if l%2 == 1:
        res += treeList[l]
    if r%2 == 0:
        res += treeList[r]
    return res

for i in range(n):
    update((1 << N) + i,int(stdin.readline()))

for i in range(n):
    a,b,c = map(int,stdin.readline().split())
    if a == 1:
        #숫자 바꾸기
        update((1 << N) + b - 1,c - treeList[(1 << N) + b - 1])
    else :
        print(sum((1 << N) + b - 1, (1 << N) + c - 1))