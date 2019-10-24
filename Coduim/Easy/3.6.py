def pattern(n):
   x=1
   for i in range(n):
      for a in range(n-i-1):
          print("A",end='');
      for e in range(x):
          if (i == i+e or e == x-1):
              print("+", end='')
          else:
              print("E", end='')
      for b in range(n-i-1):
          print("B",end='')
      x+=2
      print("")
   x -= 2
   for i in range(n):
       for a in range(i):
           print("C", end='');
       if i>0:
           for e in range(x):
               if (i == i + e or e == x - 1):
                   print("+", end='')
               else:
                   print("E", end='')
       for b in range(i):
           print("D", end='')
       if i > 0:
           print("")
       x -= 2
check = True
while(check):
    try:
        n = int(input("n="))
        pattern(n)
    except ValueError :
        check=False