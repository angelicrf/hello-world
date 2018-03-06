show =['Wooden staff','wizard hat','cloth shoes']
itemWeight =[30.0,1.5,5.3]
ItemColor =["brown","black","blue"]
# current_weight = 0


def Menu():
    menu =['show','grab','edit','drop','exit']
    
    describe =['show all the items','Grab an item','Edit an item','Drop an item','exit']
    for i in range(len(menu)):
        print('\n',i+1,menu[i],'-----' ,describe[i])
    return menu

def Show(n):
    
    for i in range(len(n)): 
        print("\n",i+1, n[i],'-----',ItemColor[i],'-----',itemWeight[i])

 
def Grab(n,c,w):
    total_item = len(show)
    print("The total items are:" ,total_item)
    total_weight = sum ( itemWeight )

    if (total_item >3):
         print("You can't carry anymore items. Drop something first")
         Drop(n,c,w)
         # Grab(n,c,w)

    # while (not total_item >3 and not total_weight >100):
        
    askUser =str(input("Name: "))
    askColor =str(input("Color: "))
    askWeight =float(input("Weight: "))
    testWeight  = askWeight +sum(itemWeight)
    # current_weight =testWeight
    print("the test weight is: ",testWeight,"The limit is 100")

    if (testWeight <100):

        show.append(askUser)
        itemWeight.append(askWeight)
        ItemColor.append(askColor)

    else:
        print("Weight limit of 100 lbs will be exceeded with this item."+
              "Please drop something first")
        Drop(n,c,w)
        # Grab(n,c,w)

# def get_weight():
#     return  current_weight
#

def Edit(n):
    userWant =int(input("Enter the number of  item: "))
    x = n.pop(userWant-1)
    print("The item you want to delete is: ", x)
    userUpdated = str(input("Updated name: "))
    u= n.append(userUpdated)
    print(n)
    

def Drop(n,c,w):

    print("The grabbed items before dropping contains: ",show)
    userDrop = str(input("Do you want drop by number or by color(number/color)?: "))
    testWeight = sum ( itemWeight)
    if(userDrop =="number"):
        # while (not len(show) >3):
        askNum =int(input("Enter an index number: "))
        if(ItemColor[askNum]):
            position_show =(n[askNum])
            print("The deleted item is: ",position_show)
            show[:] = (value for value in show if value != position_show)
            # deleted_show =n.pop(askNum)
            print("The current items are: ",show)
        else:
            print("Wrong entry. No item can be deleted. ")

        if (ItemColor[askNum]):

            position_weight =(w[askNum])
            # deleted_weight =w.pop(askNum)
            itemWeight[:] = (value for value in itemWeight if value != position_weight)
            print("The current items weight are : ",itemWeight)
        else:
            print("Wrong entry.No weight can be deleted. ")

        if (ItemColor[askNum]):

            position_color = (c[askNum])
            # deleted_color =c.pop(askNum)
            ItemColor[:] = (value for value in ItemColor if value != position_color)
            print("the current items color are: " , ItemColor)
            print("The total weight is: ",testWeight)

        else:
            print("Wrong entry.No color can be deleted. ")

                
    elif(userDrop =="color"):
        print("current itms colors are: ", ItemColor)
        # while (not len(show) >3):
        askColor =str(input("Color: "))

        if (askColor in ItemColor):
            for j in n:
                find_inex = c.index ( askColor )
                # print("the find_index is",find_inex)
                position_item = n[find_inex]
                # print ( "The position_item is : " , position_item )
                show[:] = (value for value in show if value !=position_item )
            print ( "The current items are : " , show )


        else:
            print ( "item does not exists in Items." )


        if (askColor in ItemColor):
            find_inex = c.index(askColor)
            # print("the find_index is",find_inex)
            for k in w:
                position_weight = w[find_inex]

                itemWeight[:] = (value for value in itemWeight if value !=position_weight )
            print("The current items weight are : ",itemWeight)
            print("The total weight is: " , testWeight)
        else:
             print ( "item does not exists in Items weight." )

                
         
        if (askColor in ItemColor ):
            # ItemColor.remove(askColor)
            ItemColor[:] = (value for value in ItemColor if value != askColor)
            print("The colors after deleting: ",ItemColor)
        elif(askColor not in ItemColor ):
            print("No color of ",askColor, "found. No items were dropped." )

        
    else:
        print("Invalid choice.should be either number or color.\n")

    
    
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
            Drop(show,ItemColor,itemWeight)            
        elif(userChoice =='grab'):
            Grab(show,ItemColor,itemWeight)
        elif(userChoice =='exit'):
            print("Bye")
            break
        else:
            print("Invalid entry")
   

main()
