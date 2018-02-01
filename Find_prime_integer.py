test= True;
userAsk =0
userContinue = "y"

while(userAsk <=0 or userAsk >5000 or userAsk ==1 and test == True or userAsk %2 ==0 or userContinue =="y".lower()):
    userAsk =int(input("Please enter an integer between 1 and 5000: "));
    Factor = userAsk/userAsk
    
    if(not userAsk <0 and not userAsk >5000):
        if(userAsk %2 ==0 or userAsk ==1):
            for i in range(1,userAsk+1 ):
                if (userAsk %i ==0):
                    test = True;
                    print(i, end=" ")
            print("\nThe number is NOT prime.");
        else:
            test= False;
            print("The number is a prime.");
            print("it has only 2 factors.");
            Factor = userAsk/userAsk
            print("Factors are: ",int(Factor),userAsk);
            userContinue=str(input("Do you want to continue (y/n): "));
            if(userContinue == "n".lower()):
                print("Bye");
    else:
        print("The number is invalid.");
            
        
    
    
