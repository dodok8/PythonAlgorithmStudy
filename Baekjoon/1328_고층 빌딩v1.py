# 방법 자체가 잘못 된 듯
import sys
sys.setrecursionlimit(100000)
combiList = [[0 for _ in range(100)] for __ in range(100)]
def combi(n,r):
    if n == r or r == 0:
        combiList[n][r] = 1
    if combiList[n][r] == 0:
        combiList[n][r] = (n-r+1)/r*combi(n,r-1)
    return combiList[n][r]

N,L,R = map(int,input().split())
aList = [[[0 for _ in range(R+1)]for __ in range(L+1)]for ___ in range(N+1)]

def A(n,l,r):
    if aList[n][l][r] != 0:
        pass
    else :
        if l==n or n==r :
            aList[n][l][r] = 1
        else:
            sum = 0
            for i in range(l,n-r+2):
                sum =sum + combi(n-1,i-1)*A(i,l,1)*A(n-i+1,1,r)%1000000007
            aList[n][l][r] = sum
    return aList[n][l][r]

print(int(A(N,L,R)%1000000007))
