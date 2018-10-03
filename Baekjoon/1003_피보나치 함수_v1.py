'''
링크 : https://www.acmicpc.net/problem/1003
PyPy3 117592KB 108ms
'''

from sys import stdin


class FbList:
    def __init__(self, n):
        self.fibo_list = [-1 for i in range(n + 1)]
        self.fibo_list[0] = 0
        self.fibo_list[1] = 1
        self.size = int(len(self.fibo_list))

    def get_value(self, *args):
        if args:
            n = args[0]
            if n == -1:
                return 1
            else:
                if self.fibo_list[n] == -1:
                    self.fibo_list[n] = self.get_value(n - 1)
                    + self.get_value(n - 2)
                return self.fibo_list[n]
        else:
            return self.get_value(len(self.fibo_list) - 1)


t = int(stdin.readline())
fibo = FbList(40)
for _ in range(t):
    n = int(stdin.readline())
    print(fibo.get_value(n - 1), fibo.get_value(n))
