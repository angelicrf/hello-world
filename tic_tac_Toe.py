import random
print("Welcome to the Tic Tac Toe Game Simulator")

def board_structure ( myBoard ):
    print("+---+---+---+")
    print("|" , myBoard[0] , "|" , myBoard[1] , "|" , myBoard[2] , "|")
    print("+---+---+---+")
    print("|" , myBoard[3] , "|" , myBoard[4] , "|" , myBoard[5] , "|")
    print("+---+---+---+")
    print("|" , myBoard[6] , "|" , myBoard[7] , "|" , myBoard[8] , "|")
    print("+---+---+---+")




def winner_catche ( elm , pos_1 , pos_2 , pos_3 , myBoard ):
    if (myBoard[pos_1] == elm and myBoard[pos_2] == elm and myBoard[pos_3] == elm):
        return True
    return False


def check_spot ( elm , myBoard ):
    return (winner_catche ( elm , 0 , 3 , 6 , myBoard )
            or winner_catche ( elm , 1 , 4 , 7 , myBoard )
            or winner_catche ( elm , 2 , 5 , 8 , myBoard )
            or winner_catche ( elm , 6 , 7 , 8 , myBoard )
            or winner_catche ( elm , 0 , 4 , 8 , myBoard )
            or winner_catche ( elm , 2 , 4 , 6 , myBoard )
            or winner_catche ( elm , 0 , 1 , 2 , myBoard )
            or winner_catche ( elm , 3 , 4 , 5 , myBoard )
            or winner_catche ( elm , 6 , 7 , 8 , myBoard ))


def get_Input ( myBoard ):
    while True:
        board_structure ( myBoard )
        userAsk = int ( input ( "Please enter a position number: " ) )

        if (myBoard[userAsk] != "x" and myBoard[userAsk] != "o"):
            myBoard[userAsk] = "x"

        if (check_spot ( "x" , myBoard ) == True):
            print("Hey,You won")
            play_again = input ( 'would you like to play again? Y/N: ' )
            if play_again.upper () == 'Y':
                return True
            else:
                print("Bye")
                return False

        while True:
            computer = random.seed ()
            computer = random.randint ( 0 , 8 )

            if (myBoard[computer] != "x" and myBoard[computer] != "o"):
                myBoard[computer] = "o"
                if (check_spot ( "o" , myBoard ) == True):
                    print("computer won")

                    break
                break


        else:
            print("This position is filled")


def main ():
    myBoard = [
        0 , 1 , 2 ,
        3 , 4 , 5 ,
        6 , 7 , 8]
    play_again = get_Input ( myBoard )
    while play_again:
        myBoard = [0 , 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8]
        play_again = get_Input ( myBoard )


main ()