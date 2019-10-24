def pattern(n):
    for i in range(n):
        for j in range(n):
            if (i==j or j==(n-i-1)):
                print("*",end='')
            else:
                print(" ",end='')
        print("")
check = True
while(check):
    try:
        n = int(input("n="))
        pattern(n)
    except ValueError :
        check=False