#https://www.acmicpc.net/problem/9656
#Python 29164KB 72ms
import sys
N = int(sys.stdin.readline())
if N%4 == 0 or N%4 ==2 :
    print('CY')
else :
    print('SK')