
import math
userDay= int(input("Enter the day : (1-31) "))
userMonth = int(input("Enter the month: "))
userYear =int(input("Enter a year between 1582 and 4902:" ))
while(userMonth ==1 or userMonth ==2):
          userYear -=1
          break
        
century = userYear /100
print("The century is: ",int (century))
yearAdjusted = userYear -(int(century) * 100)
print("The last two digits of the year is: ",yearAdjusted)
zellerMonth =0

if(userYear != 0 and (userYear >1582  and  userYear <4902)and (userDay >0 and userDay <=31)):
  print(userYear)
  if (userMonth == 1):
      print("January")
      zellerMonth =11
  elif(userMonth == 2):
      print("February")
      zellerMonth =12
  elif(userMonth == 3):
      print("March")
      zellerMonth =1
  elif(userMonth == 4):
      print("April")
      zellerMonth =2
  elif(userMonth == 5):
      print("May")
      zellerMonth =3
  elif(userMonth == 6):
      print("June")
      zellerMonth =4
  elif(userMonth == 7):
      print("July")
      zellerMonth =5
  elif(userMonth == 8):
      print("August")
      zellerMonth =6
  elif(userMonth == 9):
      print("September")
      zellerMonth =7
  elif(userMonth == 10):
      print("October")
      zellerMonth =8
  elif(userMonth == 11):
      print("October")
      zellerMonth =9
  elif(userMonth == 12):
      print("December")
      zellerMonth =10
      
  else:
      print("Invalid Month number.")
      


else:
  print("wrong input")
dayName = ((userDay+ math.floor((13 * zellerMonth - 1) / 5) + yearAdjusted + math.floor(yearAdjusted/ 4) + math.floor(century/4) - (2* int(century))) % 7 )
myDayName = []
myDayName.append(dayName+1)
print("The number of day in a week is: ",myDayName)
weekDays= ["Sunday","Saturday","Monday","Tuesday","Wednesday","Thursday","Friday"]

for  (x,y)in zip( myDayName,weekDays  ):
        print("The day of the month is: ",weekDays [x])
    
W = math.floor((13 * zellerMonth - 1) / 5)
X = math.floor(yearAdjusted/ 4)
Y = math.floor(century/4)
Z = (W + X + Y + userDay + yearAdjusted )- 2* int(century)
R = Z% 7 
print("a b c d = ",zellerMonth,userDay,yearAdjusted,int(century), end= " ")
print("\nw x y z r = ",W, X, Y, Z, R ,end= " ")


