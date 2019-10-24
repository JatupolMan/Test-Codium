def pattern(n):
    for i in range(1,n+1,2):
        for j in range(i,n,2):
            print(" ",end='')
        for k in range(i):
            print("*",end='')
        print("")
    for i in range(1, n,2):
        for j in range(0,i,2):
            print(" ", end='')
        if n%2!=0:
            for k in range(i,n-1):
                print("*", end='')
        else:
            for k in range(i,n):
                print("*", end='')
        print("")
check = True
while(check):
    try:
        n = int(input("n="))
        pattern(n)
    except ValueError :
        check=False