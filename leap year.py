def leapyear(year):
    leap = False
    #Логическое тело
    if year % 4 == 0:
        leap = True
        if year % 100 ==0 and year % 400!=0:
                leap = False
        elif year % 400:
                leap = True
    return leap
#ввод и вывод соответственно
year = int(input())
print(leapyear(year))
    

