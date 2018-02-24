import random

user_contin ="b"
user_num =0
numbers_dice =[]
col_total =0


def welcome():
    print("Welcome to Dice Rolling Simulator")

def getuser():
    user_num = int(input("Please neter the number of tries you want to run: "))
    return user_num

def user_continue():
    
    user_contin= str(input("Continue? (y/n): "))
    if (user_contin =="n"):
        print("Bye")
    elif(not user_contin =="y"):
        print("the entry in invalid.")
    return user_contin

def calculate(user_num,user_contin):
    user_num =False
    
    while (not user_num or user_contin =="y"):
        
        user_num = getuser()
        if(user_num <0):
            user_num = getuser()
            
        numbers_dice.append(user_num)
        print("\nRoll","Count","Percentage", end ='  ')
        
        for i in range (1,13):
            dice_Round = random.randint(1,user_num)
            percentage = dice_Round /100
            col_total=sum(numbers_dice)
            
            print ("\n",i,dice_Round,percentage, sep='  ' )
            
        print("\n the total is: ",col_total)
        del numbers_dice[ 0:len(numbers_dice) ]
        user_contin = user_continue()
        
        
def main():
    
    welcome()
    calculate(user_num,user_contin)
    
main()
