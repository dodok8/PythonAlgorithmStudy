import random
import sys

n,m = map(int,sys.stdin.readline().split())

parentList = [i for i in range(n+1)]
heightList = [0 for _ in range(n+1)]

def findParent(a) :
    if parentList[a] == a :
        return a
    else :
        parentList[a] = findParent(parentList[a])
        return parentList[a]
def sumSet(a,b):
    A = findParent(a)
    B = findParent(b)
    if A == B:
        pass
    else : # 같은 집합에 있지 않을 때
        if heightList[A] == heightList[B] : #둘이 높이가 같은 경우
            if random.randint(0,2) == 1:
                parentList[B] = A
                heightList[A] += 1
            else:
                parentList[A] = B
                heightList[B] += 1
        elif heightList[A] > heightList[B]:
            parentList[B] = A
        else :
            parentList[A] = B

def findSet(a,b):
    A = findParent(a)
    B = findParent(b)
    if A == B:
        print('YES')
    else :
        print('NO')

for i in range(m):
    op,a,b = map(int,sys.stdin.readline().split())
    if op == 0: # 집합 더하기
        sumSet(a,b)
    else : #존재 확인
        findSet(a,b)
