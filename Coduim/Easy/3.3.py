def pattern(n):
    x=1
    for i in range(n):
       for j in range (n-i-1):
           print(" ",end='')
       print("*",end='')
       if i!=0:
            for k in range(x):
               print(" ", end='')
            print("*",end='')
            x+=2
       print("")
check = True
while(check):
    try:
        n = int(input("n="))
        pattern(n)
    except ValueError :
        check=False