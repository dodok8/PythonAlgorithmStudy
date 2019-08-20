l_dict = {"E":"S","S":"E"}
for test_count in range(int(input())):
    dim = int(input())
    N = input()
    a= ""
    for i in N:
        a = a + l_dict[i]
    print("Case #{0}: {1}".format(test_count+1,a))