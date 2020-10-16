year = input("Введите год: ")
number = int(year)
number=False
if number % 4 == 0:
   number=True
   if number % 100 == 0 and number % 400 != 0:
      number=False
   elif number % 400 == 0:
      number=True
if number = True:
   print("это високосный год")
if number = False:
   print("это не високосный год")
       
      
   
