#https://www.acmicpc.net/problem/2748
# PyPy3 117076KB 108ms
from sys import stdin
class FbList:
    def __init__(self, n):
        self.fbList = [-1 for i in range(n+1)]
        self.fbList[0] = 0
        self.fbList[1] = 1
        self.size = int(len(self.fbList))
    def getValue(self, *args):
        if args:
            n = args[0]
            if n > self.size:
                self.fbList.extend([-1 for i in range(n-self.size)])
                self.get(n)
            else :
                if self.fbList[n] == -1:
                    self.fbList[n] = self.getValue(n-1) + self.getValue(n-2)
                return self.fbList[n]
        else:
            return self.getValue(len(self.fbList)-1)
fibo = FbList(int(stdin.readline()))
print(fibo.getValue())
