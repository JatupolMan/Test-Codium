def leapyear(year):
    if  (year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0)):
        return  True
    else :
        return False
check = True
while(check):
    try:
        year = int(input(""))
        print("->",leapyear(year))
    except ValueError :
        check=False