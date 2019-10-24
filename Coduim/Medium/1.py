def primenumber(n):
    print("-> ",end='')
    mlist = []
    for i in range(2,n+1).__reversed__():
        check = True
        for j in range(2,i).__reversed__():
            if i%j==0 :
                check=False
                break
        if check :
            mlist.append(i)
    mlist.sort()
    print(*mlist)

check = True
while(check):
    try:
        n = int(input(""))
        primenumber(n)
        print('')
    except ValueError :
        check=False