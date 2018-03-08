
show =[['Wooden staff','brown',30.0],
       ['wizard hat','black',1.5],
       ['cloth shoes','blue',5.3]]

new_list=[]

def Menu():
    menu =['show','grab','edit','drop','exit']
    
    describe =['show all the items','Grab an item','Edit an item','Drop an item','exit']
    for i in range(len(menu)):
        print('\n',i+1,menu[i],'-----' ,describe[i])
    return menu

def Show(n):

    for i in range(len(n)):
        print("   ")
        for j in range(len(n[0])):

                 print(i+1," " , n[i][j] , end ='')

        print()

def adding_element(n,nl):
    total_items = len(n)
    print("The total numbers of items are: ",total_items)
    total_weight = n[0][2] + n[1][2] + n[2][2]
    print("The current weight of items is: ",total_weight)


    if (total_items >3):
        print("You can't carry anymore items. Drop something first")
    #          Drop(n)

    else:
        askUser = str ( input ( "Name: " ) )
        askColor = str ( input ( "Color: " ) )
        askWeight = float ( input ( "Weight: " ) )
        test_total = askWeight + total_weight
        #     # current_weight =testWeight
        print("the test weight is: " , test_total, "The limit is 100")
        if (test_total < 100):
            nl = []
            nl.append ( askUser )
            nl.append ( askColor )
            nl.append ( askWeight )

            n.append ( nl )

            total_weight = 0
            for i in n:
                for j in nl:
                    nl=n

            print(n)

            total_weight = n[0][2] + n[1][2] + n[2][2]
            print(test_total)
        else:
            print("Weight limit of 100 lbs will be exceeded with this item."+
                  "Please drop something first")
            Drop_item(n)


def Edit(n):
    userWant = int ( input ( "Enter the number of  item: " ) )

    if (userWant ==1):
        x = n[0].pop(userWant-1)
        print("The item you want to edit is: ", x)
        userUpdated = str(input("Updated name: "))
        u= n[0].insert(0,userUpdated)
        for elm in n:
            print(elm)
    elif(userWant ==2):
        x = n[1].pop (userWant-1)
        print("The item you want to edit is: " , x)
        userUpdated = str ( input ( "Updated name: " ) )
        u = n[1].insert ( 0 , userUpdated )
        for elm in n:
            print(elm)
    elif(userWant ==3):
        x = n[2].pop (userWant-1)
        print("The item you want to edit is: " , x)
        userUpdated = str ( input ( "Updated name: " ) )
        u = n[2].insert ( 0 , userUpdated )
        for elm in n:
            print(n)
    else:
        print("The number is wrong,try again!!")


def Drop_item(n):
    print("The grabbed items before dropping contains: " , n)
    userDrop = str(input("Do you want drop by number or by color(number/color)?: "))
    if (userDrop == "number"):
        askNumber =int(input("Enter the number: "))
        # delete_item =askNumber +1
        del n[:askNumber]
        print(n)

    elif(userDrop =="color"):
        askColor =str(input("Enter the color: "))

        for value in n[:]:
            if value[1]  == askColor:
                n.remove ( value )
                print(n)
            elif value[1] != askColor:
                n=n

        print("Sorry,the color doesn't exist")
        # for col in n:
        #     if askColor in col:
        #
        #         n.remove(col)
        # print(n)



    else:
        print("Wrong entry.Try again!!!")

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
            Drop_item ( show )
        elif(userChoice =='grab'):
            adding_element ( show , new_list )
        elif(userChoice =='exit'):
            print("Bye")
            break
        else:
            print("Invalid entry")


main()
