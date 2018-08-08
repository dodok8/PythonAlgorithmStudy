#최적화를 포기해서 쉽게 생각해보자.
import random
import sys

parentList = [i for i in range(200000)]
heightList = [0 for _ in range(200000)]
numberList = [1 for _ in range(200000)]
nameDict = {}

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
        return numberList[A]
    else : # 같은 집합에 있지 않을 때
        if heightList[A] > heightList[B]:
            parentList[B] = A
            numberList[A] += numberList[B]
            numberList[B] = 1
            return numberList[A]
        else :
            parentList[A] = B
            numberList[B] += numberList[A]
            numberList[A] = 1
            return numberList[B]
def match2Dict(aList):
    for i in aList:
        if i not in nameDict :
            nameDict[i] = len(nameDict)
        else:
            pass
for _ in range(int(sys.stdin.readline())):
    for __ in range(int(sys.stdin.readline())):
        fstr = sys.stdin.readline().split()
        match2Dict(fstr)
        f1N = nameDict[fstr[0]]
        f2N = nameDict[fstr[1]]
        print(sumSet(f1N,f2N))
        fstr.clear()
    nameDict.clear()
    parentList = [i for i in range(200000)]
    heightList = [0 for _ in range(200000)]
    numberList = [1 for _ in range(200000)]