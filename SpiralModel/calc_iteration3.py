class Calculator3:                          #final iteration -previous iteration functionalities are integrated and made this final iteration
    def addition(value1,value2):
        return value1+value2
    def subtraction(value1,value2):
        return value1-value2 
    def multiplication(value1,value2):
        return value1*value2 
    def division(value1,value2):             
        return value1/value2                        #modification in division function to get floating point answers
    

if __name__ == '__main__':
    while(True):
        print("FINAL PHASE")
        print("menu")
        print("1.addition")
        print("2.subtraction")
        print("3.multiplication")
        print("4.division")
        print("5.exit")
        print("choose a number(1,2,3,4 or 5)")
        try:
            choice = int(input())
        except Exception as err:
            print(err)    
        if choice==1:
            try:
                print("enter a number")
                number1 = int(input())
                print("enter a number")
                number2 = int(input())
                print('addition of {} and {} is {}'.format(number1,number2,Calculator3.addition(number1,number2)))
            except Exception as err:
                print(err)    
        elif choice==2:
            try:
                print("enter a number")
                number1 = int(input())
                print("enter a number")
                number2 = int(input())
                print('subtraction of {} and {} is {}'.format(number1,number2,Calculator3.subtraction(number1,number2)))
            except Exception as err:
                print(err)
        elif choice==3:
            try:
                print("enter a number")
                number1 = int(input())
                print("enter a number")
                number2 = int(input())
                print('multiplication of {} and {} is {}'.format(number1,number2,Calculator3.multiplication(number1,number2)))
            except Exception as err:
                print(err)        
        elif choice==4:
            try:
                print("enter a number")
                number1 = int(input())
                print("enter a number")
                number2 = int(input())
                print('division of {} and {} is {}'.format(number1,number2,Calculator3.division(number1,number2)))
            except Exception as err:
                print(err)          
        elif choice==5:
            break
        else:
            pass        
                
            