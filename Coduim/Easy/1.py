def FizzBuzz():
   for i in range(1,101):
       if i%3==0:
           print("Fizz ",end='')
       elif i%5==0:
           print("Buzz ",end='')
       else:
           print(str(i)+" ", end='')
       if i %20==0:
           print("")
FizzBuzz()