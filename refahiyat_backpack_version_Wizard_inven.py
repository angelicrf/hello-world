show =['Wooden staff','wizard hat','cloth shoes']
backPack=[]

def Menu():
    menu =['show','grab','edit','drop','exit']
    describe =['show all the items','Grab an item','Edit an item','Drop an item','exit']
    for i in range(len(menu)):
        print('\n',i+1,menu[i],'-----' ,describe[i])
    return menu

def Show(n):
    for i in range(len(n)): 
        print("\n",i+1, n[i])

 
def Grab(n):
    
    askUser =str(input("Name: "))

    assert (not len(backPack) >1)
    while (askUser in n and not len(backPack) >1):
           position =(n.index(askUser))

           print("The user Ask position : ", position)
           deleted =n.pop(position)
           print("The array contains: ",deleted)
    
           Added =backPack.append(deleted)
           print("Inside you backPack is: ",backPack)
           if(len(backPack) >1):
              print("You're not be able to take more items unless you drop something.")
              Drop()  
           return backPack
    
def Edit(n):
    userWant =int(input("Enter the number of  item: "))
    x = n.pop(userWant-1)
    print("The item you want to delete is: ", x)
    userUpdated = str(input("Updated name: "))
    u= n.append(userUpdated)
    print(n)
    

def Drop():

    userDrop = int(input("Enter the index of backpack to drop: "))
    searched = backPack[userDrop]
    print("Indexof items in backpack is:",searched )
    
    droped = backPack.pop(userDrop)
    
    print("The index dropped: ",droped)
    print("The items in your backpack is:",backPack)
    
def main():
    Menu()
    while True:
        userChoice = str(input("Command: "))
        if (userChoice == 'menu'):             
            Menu()             
        elif (userChoice == 'show'):           
            Show(show)            
        elif(userChoice == 'edit'):            
            Edit(show)             
        elif(userChoice =='drop'): 
            Drop()            
        elif(userChoice =='grab'and not len(backPack) >1):
            Grab(show)
        elif(userChoice =='exit'):
            print("Bye")
            break
        else:
            print("Invalid entry")
   

main()
