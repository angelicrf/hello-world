import random

def printWelcome():

    print("****Welcome to Rock/paper/Scissors game****")
    print("Rules of the game")
    print("\t You and the computer will each pick rock, paper or scissors.\n\t"+
      "The winner will be decided using following policy: \n\t"+
      "Rock wins over Scissors but looses to Paper. \n\t"+
      "Scissors wins over paper but loses to Rock. \n\t"+
      "Paper wins over Rock but loses to Scissors.\n\n\t"+
      "Let the game begin!!\n\n")


def pickRPS():
    objectName = ["scissors","rock","paper"]
    comp_Play = objectName[random.randint(0,2)]
    return comp_Play



def getUserPick():
    human =str(input("Please choose scissors, rock or paper or quit to exit:"))
    return human

def playOneRound(human):
    
    human = False            
    count_round =0
    count_human =0
    count_comp =0
    count_tie =0
    count_comp =0
    comp_Play = pickRPS()
    
    
    while human == False:
    ##    human =str(input("Please choose scissors, rock or paper or quit to exit: "))
          human = getUserPick()
          if (human == comp_Play):
                print("There is a tie")
                
                count_round +=1
                count_tie +=1
          elif(human == "rock"):
                if(comp_Play == "paper"):
                    print("You lose",comp_Play,"Take over", human)
                    count_round +=1
                    count_human +=1
                    count_comp +=1
                else:
                    print("Tou won",human,"destroes",comp_Play)
                    count_round +=1
                    count_human +=1
                    count_comp +=1
          elif(human == "scissors"):
                if(comp_Play == "rock"):
                    print("You lose", comp_Play,"destroyes",human)
                    count_round +=1
                    count_human +=1
                    count_comp +=1
                else:
                    print("You won", human, "cut the",comp_Play)
                    count_round +=1
                    count_human +=1
                    count_comp +=1
          elif(human == "paper"):
                if(comp_Play == "scissors"):
                    print("You lose", comp_Play, "cut the", human)
                    count_round +=1
                    count_human +=1
                    count_comp +=1
                else:
                    print("You won", human, "Take over", comp_Play)
                    count_round +=1
                    count_human +=1
                    count_comp +=1

          elif(human == "quit"):
                
                print("\nNumber of rounds: ",count_round)
                print("Numbers of times you won: ",count_human)
                print("Number of times computer won: ",count_comp)
                print("Number of ties: ",count_tie)
                print("Bye")
                break
          else:
                print("You entered a wrong value.")
          human = False
          ## comp_Play = objectName[random.randint(0,2)]
        

def main():
        printWelcome()
        playOneRound(False)
main()
