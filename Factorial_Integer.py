test =True
userNum =0
factorial =1
print("\n\nWelcome to factorial program\n\n")
userNum = int(input("Please enter a non negative number: "));
while True:
    while(userNum <0 and test == True):
        try:
           userNum = int(input("Please enter a non negative number: "));
        except Exception as e:
           userNum ==None;

    if(userNum == 0 or userNum == 1):
        factorial =factorial;
        print("\n\nThe factorial of a number using the while loop is: ",factorial);
        break
    while(userNum >1):
        count =1
        factorial = (factorial* userNum);
        userNum-=1
    print("\n\nThe factorial of a number using the while loop is: ",factorial );
    break
for i in range(1,userNum+1):
    if(userNum == 0 or userNum == 1):
       factorial =factorial;
           
    elif(userNum >1):
       
       factorial =factorial* i;
       
print("\n\nThe factorial of a number using the for loop is: ",factorial);
print("\n\nBye!");
    
          
    
    
                  
            
   
    
    

    
   



    
    
