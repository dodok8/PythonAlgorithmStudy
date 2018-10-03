'''
링크: https://www.acmicpc.net/problem/4195
PyPy3  211328KB 788ms
Disjoint set의 구현이기는 한데 가장 큰 장점인 최적화를 포기했다.
TODO: 최적화 넣어서 다시 구현
'''

import random
import sys

parent_list = [i for i in range(200000)]
height_list = [0 for _ in range(200000)]
number_list = [1 for _ in range(200000)]
name_dict = {}


def find_parent(a):
    global parent_list
    if parent_list[a] == a:
        return a
    else:
        parent_list[a] = find_parent(parent_list[a])
        return parent_list[a]


def sum_set(a, b):
    global parent_list, number_list
    A = find_parent(a)
    B = find_parent(b)
    if A == B:
        return number_list[A]
    else:  # 같은 집합에 있지 않을 때
        if height_list[A] > height_list[B]:
            parent_list[B] = A
            number_list[A] += number_list[B]
            number_list[B] = 1
            return number_list[A]
        else:
            parent_list[A] = B
            number_list[B] += number_list[A]
            number_list[A] = 1
            return number_list[B]


def match_to_dict(in_list):
    for i in in_list:
        if i not in name_dict:
            name_dict[i] = len(name_dict)
        else:
            pass


for _ in range(int(sys.stdin.readline())):
    for __ in range(int(sys.stdin.readline())):
        fstr = sys.stdin.readline().split()
        match_to_dict(fstr)
        f1N = name_dict[fstr[0]]
        f2N = name_dict[fstr[1]]
        print(sum_set(f1N, f2N))
        fstr.clear()
    name_dict.clear()
    parent_list = [i for i in range(200000)]
    height_list = [0 for _ in range(200000)]
    number_list = [1 for _ in range(200000)]
