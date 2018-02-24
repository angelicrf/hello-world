
print("Welcome to the square-cube table generator")

userEnter = 0
userEnding =0
def square(userEnter):
    
    
    square = userEnter**2
    return square


def Cube(userEnter):
    
    num2 = userEnter
    cube = userEnter**3
    return cube
    

def main():
    userEnter =int(input("Please enter a number: "))
    userEnding =int(input("Please enter the ending number: "))

    print("-------","-------","-------")
    print()
    print("Number","Squared", "  Cubed")
    print("-------","-------","-------")
    print()

    for i in range(userEnter, userEnding+1):
        print(i ,square(i), Cube(i), sep = '      ')
main();


