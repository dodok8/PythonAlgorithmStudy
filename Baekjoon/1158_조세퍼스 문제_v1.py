#https://www.acmicpc.net/submit/1158/8735288
#31752 KB 6452 ms
from sys import stdin
from collections import deque

q = deque()
N,M = map(int,stdin.readline().split())
for i in range(1,N+1):
    q.append(i)
print("<",end="")
while len(q) > 1:
    for i in range(M):
        a = q.popleft()
        if i == M-1 :
            print(a,end=", ")
        else :
            q.append(a)
print(q.popleft(), end="")
print(">")
