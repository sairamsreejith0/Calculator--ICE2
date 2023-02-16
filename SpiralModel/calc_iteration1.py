class Calculator1:                  #1st iteration
    def addition(value1,value2):    #addition function to add two numbers
        return value1+value2

    def subtraction(value1,value2):  #subtraction function to subtract two numbers
        return value1-value2 
    
if __name__ == '__main__':
    while(True):               
        print("menu")                #giving options to user to choose addition,subtraction,multiplication,division or exit
        print("1.addition")
        print("2.subtraction")               
        print("3.Exit")
        print("choose a number(1,2,3)")
        try:                         #try and except block is used for risk analysis by identifying exceptions and handling them
            choice = int(input())    #taking input from user
        except Exception as err:
            print(err)               #printing the exception
            continue
        if choice==1:                          #risk analysis needed to be done for each functionality separately
            try:
                print("enter a number")
                number1 = int(input())
                print("enter a number")
                number2 = int(input())
                print('addition of {} and {} is {}'.format(number1,number2,Calculator1.addition(number1,number2)))
            except Exception as err:
                print(err)
                
          
        elif choice==2:
            try:
                print("enter a number")
                number1 = int(input())
                print("enter a number")
                number2 = int(input())
                print('subtraction of {} and {} is {}'.format(number1,number2,Calculator1.subtraction(number1,number2)))
            except Exception as err:
                print(err)
                    
        elif choice==3:
            break
        else:
            pass        
                
            