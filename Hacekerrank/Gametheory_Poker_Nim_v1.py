#https://www.hackerrank.com/contests/5-days-of-game-theory/challenges/day-2-poker-nim
#k번 넣어 봤자 다시 돌려놓을 수 있으므로 그냥 님게임2과 같다
import sys

for _ in range(int(sys.stdin.readline())):
    n,k = map(int,sys.stdin.readline().split())
    p = list(map(int,sys.stdin.readline().split()))
    a = p.pop()
    for i in p:
        a = a^i
    if a == 0:
        print('Second')
    else:
        print('First')