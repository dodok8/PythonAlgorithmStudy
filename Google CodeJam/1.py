a_list = ["0","1","1","2","3","3","3","5","5","7"]
b_list = ["0","0","1","1","1","2","3","2","3","2"]
for _ in range(int(input())):
    N = input()
    a = ""
    b = ""
    for i in range(len(N)-1,-1,-1):
        a = a_list[int(N[i])] + a
        b = b_list[int(N[i])] + b
    print("Case #{0}: {1} {2}".format(_+1,a,int(b))