'''
링크: https://www.acmicpc.net/problem/8895
PyPy3  120828KB 416ms
1328번 고층빌딩과 사실상 같은 문제
'''

count = int(input())
number_of_case = [[[0 for _ in range(21)]
                   for __ in range(21)]for ___ in range(21)]
number_of_case[1][1][1] = 1


def dp(N, L, R):
    global number_of_case
    if number_of_case[N][L][R] != 0:
        return number_of_case[N][L][R]
    else:
        for i in range(2, N+1):
            for j in range(1, L+1):
                for k in range(1, R+1):
                    number_of_case[i][j][k] = (number_of_case[i-1][j][k] * (i-2)
                                               + number_of_case[i-1][j][k-1]
                                               + number_of_case[i-1][j-1][k])
        return number_of_case[N][L][R]


for _ in range(count):
    n, l, r = map(int, input().split())
    print(dp(n, l, r))
