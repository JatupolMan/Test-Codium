def pattern(n):
   for i in range(n):
       for j in range(i+1):
           print("*",end='')
       print("")
check = True
while(check):
    try:
        n = int(input("n="))
        pattern(n)
    except ValueError :
        check=False