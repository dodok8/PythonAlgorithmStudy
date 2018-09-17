#https://www.acmicpc.net/problem/2748

from sys import stdin
class FbList:
    def __init__(self, n):
        self.fbList = [-1 for i in range(n+1)]
        self.fbList[0] = 0
        self.fbList[1] = 1
        self.size = len(self.fbList)
    def getValue(self,n):
        if n > self.size:
            self.fbList.extend([-1 for i in range(n-self.size)])
            self.get(n)
        else :
            if self.fbList[n] == -1:
                self.fbList[n] = self.fbList[n-1] + self.fbList[n-2]
            return self.fbList[n]
    def getValue(self):
        return self.fbList[len(fbList-1)]
fibo = FbList(int(stdin.readline()))
fibo.getValue()
