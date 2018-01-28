import time;
test =False
userNum =0
factorial =1

print("\nWlcome to factorial program\n");
userNum = int(input("Please enter a non negative number: "))
if(userNum == 0 or userNum == 1):
         factorial =factorial;
         print("\n\nThe factorial of a number using the while loop is: ",factorial);
elif(userNum >1):
         factorial = userNum * (userNum-1)*(userNum-2)*(userNum-3) ;
         print("\n\nThe factorial of a number using the while loop is: ",factorial);
for i in range(0,userNum):
    if(userNum == 0 or userNum == 1):
        i =factorial;
           
    elif(userNum >1):
        i = userNum * (userNum-1)*(userNum-2)*(userNum-3) ;
        
    print("\n\nThe factorial of a number using the for loop is: ",i);
    print("\n\nBye!"); 
    break
      


while(userNum <0 and test == False and input !=int ):
    userNum = int(input("Please enter a non negative number: "))
    if(userNum == 0 or userNum == 1):
         factorial =factorial;
         print("\n\nThe factorial of a number using the while loop is: ",factorial);
    elif(userNum >1):
         factorial = userNum * (userNum-1)*(userNum-2)*(userNum-3) ;
         print("\n\nThe factorial of a number using the while loop is: ",factorial);
   
    for i in range(0,userNum):
        if(userNum == 0 or userNum == 1):
           factorial =factorial;
           
        elif(userNum >1):

           factorial = userNum * (userNum-1)*(userNum-2)*(userNum-3) ;
    print("\n\nThe factorial of a number using the for loop is: ",factorial);
            
    
    
    print("\n\nBye!");
          
    
    
                  
            
   
    
    

    
   



    
    
