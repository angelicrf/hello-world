test =True
starting_odometer =0
new_odometer =0
counter =0
fuel_count=0
average =0
sum=0
user_continue ="y"

print("\n\n****Welcome to the Average MPG Calculator****\n\n");
starting_odometer = int(input("Please enter the starting odometer in miles: "));
while True:
    while(starting_odometer <0 and test == True and user_continue =="y".lower()):
        starting_odometer = int(input("\nPlease enter a valid starting odometer per miles: "));

    counter = counter +1;
    new_odometer = int(input("\nPlease enter the new odometer in miles for leg # "+str(counter)+": "));
    while(new_odometer<starting_odometer and test == True and user_continue =="y".lower() ):
                
                
                if(new_odometer> starting_odometer):
                    counter = counter +1;
                    new_odometer = int(input("\nPlease enter the new odometer in miles for leg # "+str(counter)+": "));
                else:
                    counter =counter;
                    new_odometer = int(input("\nPlease enter the new odometer in miles for leg # "+str(counter)+": "));
                
                
                
    fuel_count = fuel_count +1;
    userFuel =float(input("\nPlease enter the feul consumed on leg # "+str(fuel_count)+": "));
    average= (new_odometer - starting_odometer)/ userFuel;
    sum =(sum+average);
                
                
    print("\nThe amount of fuel per mile is: ",average);
    user_continue = str(input("\nWould you like to continue(Y/N) ? "));
    if (user_continue == "n".lower()):
              print("\n\nThe total of the logs to complete this journey was: ",counter);
              
              print("The final average MPG for the entire journey was: ",round(sum,2));
              print("\nBye");
    
              break
