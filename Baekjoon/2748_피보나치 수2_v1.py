'''
링크: https://www.acmicpc.net/problem/2748
런타임 에러:
틀렸습니다:
메모리 초과:
시간초과:
Python3  KB  ms
PyPy3  117076KB 108ms
'''

from sys import stdin


class Fibo():
    def __init__(self, n):
        self.fibo_list = [-1 for i in range(n+1)]
        self.fibo_list[0] = 0
        self.fibo_list[1] = 1
        self.size = int(len(self.fibo_list))

    def get_value(self, *args):
        if args:
            n = args[0]
            if n > self.size:
                self.fibo_list.extend([-1 for i in range(n-self.size)])
                self.get_value(n)
            else:
                if self.fibo_list[n] == -1:
                    self.fibo_list[n] = (self.get_value(n-1)
                                         + self.get_value(n-2))
                return self.fibo_list[n]
        else:
            return self.get_value(len(self.fibo_list)-1)


fibo = Fibo(int(stdin.readline()))
print(fibo.get_value())
