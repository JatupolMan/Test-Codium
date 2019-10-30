import os
import redis
r = redis.Redis(port=6379)
p1list,p2list,p3list,p4list,p5list,p6list,primelist,leapyearlist=[],[],[],[],[],[],[],[]
def FizzBuzz():#1
   for i in range(1,101):
       if i%3==0:
           print("Fizz ",end='')
       elif i%5==0:
           print("Buzz ",end='')
       else:
           print(str(i)+" ", end='')
       if i %20==0:
           print("")

def leapyear(year):#2
    if  (year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0)):
        print(True)
    else :
        print(False)
def pattern_1(n):#3.1
    if n>0:
       for i in range(n):
           for j in range(i+1):
               print("*",end='')
           print("")
def pattern_2(n):#3.2
   for i in range(n):
       for j in range (n-i-1):
           print(" ",end='')
       for k in range(i+1):
           print("*",end='')
       print("")
def pattern_3(n):#3.3
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
def pattern_4(n):
    for i in range(n):
        for j in range(n):
            if (i==j or j==(n-i-1)):
                print("*",end='')
            else:
                print(" ",end='')
        print("")
def pattern_5(n):
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
def pattern_6(n):
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
def elsefinally():
    os.system('cls')
    string='ข้อแตกต่างจาก finally กับ else'
    print(string)
    string='1.finally ถึงแม้จะว่าคำสั่งนั้นจะเข้า try หรือ cash สุดท้ายแล้ว คำสั่งนั้นก็จะเข้าฟังชั่น finally เสมอ'
    print(string)
    string='2.finally เป็นขั้นตอนสุดท้ายสำหรับการจัดการความผิดพลาดของโปรแกรม';
    print(string)
    string='3. else จะเข้าก็ต่อเมื่อไม่เข้า if ถ้าเกิดเข้า if ไป แล้วก็จะไม่เข้า else ในกรณีใดกรณีหนึ่ง'
    print(string)
    input()
def primenumber(n):#4
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
    print()
def ManuPattern():
    os.system('cls')
    print("1.> Pattern 1")
    print("2.> Pattern 2")
    print("3.> Pattern 3")
    print("4.> Pattern 4")
    print("5.> Pattern 5")
    print("6.> Pattern 6")
    print("7.> Manu")
    pattern = input("Select Pattern : ")
    if int(pattern)==1:
        while True:
            n = input("Input n : ")
            if n == ' ':
                ManuPattern()
            else:
                pattern_1(int(n))
                p1list.append(int(n))
                r.set('Pattern 1', str(p1list))
    elif int(pattern)==2:
        while True:
            n = input("Input n : ")
            if n == ' ':
                ManuPattern()
            else:
                pattern_2(int(n))
                p2list.append(int(n))
                r.set('Pattern 2', str(p2list))
    elif int(pattern) == 3:
        while True:
            n= input("Input n : ")
            if n==' 'or n=='':
                ManuPattern()
            else:
                pattern_3(int(n))
                p3list.append(int(n))
                r.set('Pattern 3', str(p3list))
    elif int(pattern) == 4:
        while True:
            n= input("Input n : ")
            if n==' 'or n=='':
                ManuPattern()
            else:
                pattern_4(int(n))
                p4list.append(int(n))
                r.set('Pattern 4', str(p4list))
    elif int(pattern) == 5:
        while True:
            n= input("Input n : ")
            if n==' 'or n=='':
                ManuPattern()
            else:
                pattern_5(int(n))
                p5list.append(int(n))
                r.set('Pattern 5', str(p5list))
    elif int(pattern) == 6:
        while True:
            n= input("Input n : ")
            if n==' 'or n=='':
                ManuPattern()
            else:
                pattern_6(int(n))
                p6list.append(int(n))
                r.set('Pattern 6', str(p6list))
    elif int(pattern)==7:
        MainManu()
    ManuPattern()
def tolist(tolist):
   return [int (i) for i in str(tolist)[3:-2].split(',')]

listtask = ['Leap year', 'Pattern 1', 'Pattern 2', 'Pattern 3', 'Pattern 4', 'Pattern 5', 'Pattern 6', "Prime Number"]
def MainManu():
    check = True
    while(check):
        try:
            os.system('cls')
            print("****Hello World****")
            print("1.> Fizz & Buzz ")
            print("2.> Pattern")
            print("3.> Leap year")
            print("4.> Prime numbers")
            print("5.> Show all task")
            print("6.> Delete task")
            print("7.> Different else and finally")
            print("8.> Close program")
            print("Please select manu")
            manu = input("Input : ")
            if int(manu) == 1:
                FizzBuzz()
                input()
            elif int(manu) == 2:
                ManuPattern()
            elif int(manu) == 3:
                while True:
                    year = input("Year : ")
                    if year == ' ':
                        MainManu()
                    else:
                        leapyear(int(year))
                        leapyearlist.append(int(year))
                        r.set('Leap year',str(leapyearlist))
            elif int(manu) == 4:
                while True:
                    n = input("Input n : ")
                    if n == ' ':
                        MainManu()
                    else:
                        primenumber(int(n))
                        primelist.append(int(n))
                        r.set('Prime Number',str(primelist))
            elif int(manu) == 5:
                print("Show All Task ")
                for i in listtask:
                    print(i)
                    if r.get(i)!=None:
                        for j in tolist(r.get(i)):
                            print("N : "+str(j))
                            if i =='Leap year':
                                leapyear(j)
                            elif i=='Pattern 1':
                                pattern_1(j)
                            elif i=='Pattern 2':
                                pattern_2(j)
                            elif i=='Pattern 3':
                                pattern_3(j)
                            elif i=='Pattern 4':
                                pattern_4(j)
                            elif i=='Pattern 5':
                                pattern_5(j)
                            elif i=='Pattern 6':
                                pattern_6(j)
                            elif i== 'Prime Number':
                                primenumber(j)
                    else:
                        print("No have task")
                    print()
                input()
            elif int(manu) == 6:
                try:
                    while True:
                        os.system('cls')
                        print("*** Delete Data ***")
                        for id,va in enumerate(listtask):
                            print(str(id+1)+'.>',va)
                        print("9.> Manu")
                        print("Please Input choose to delete")
                        n = input("Input list : ")
                        if n.isdigit():
                            if int(n)<=8 :
                                if r.get(listtask[int(n)-1])!=None:
                                    mlist=tolist(r.get(listtask[int(n)-1]))
                                    print(mlist)
                                    index = input("Delete by index : ")
                                    if int(index)<=len(mlist):
                                        mlist.pop(int(index))
                                        if len(mlist)==0:
                                            r.delete(listtask[int(n) - 1])
                                        else:
                                            r.set(listtask[int(n) - 1],str(mlist))
                                        print(mlist)
                                    else:
                                        print("Index out of range")
                                else:
                                    print("No have data")
                            elif(int(n)==9):
                                MainManu()
                            else :
                                print("Input invalid")
                        else:
                            print("Input invalid")
                        input()
                except ValueError as ex:
                    print(ex)
            elif int(manu)==7:
                elsefinally()
            elif int(manu) == 8:
                check=False
        except ValueError as e:
            print(e)
MainManu()