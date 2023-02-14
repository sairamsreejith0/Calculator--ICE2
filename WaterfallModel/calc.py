class Calculator:
    def addition(value1,value2):
        return value1+value2

    def subtraction(value1,value2):
        return value1-value2 

    def multiplication(value1,value2):
        return value1*value2 

if __name__ == '__main__':
    while(True):
        print("menu")
        print("1.addition")
        print("2.subtraction")
        print("3.multiplication")
        print("4.Exit")
        print("choose a number(1,2,3 or 4)")
        choice = int(input())
        if choice==1:
            print("enter a number")
            number1 = int(input())
            print("enter a number")
            number2 = int(input())
            print('addition of {} and {} is {}'.format(number1,number2,Calculator.addition(number1,number2)))
        elif choice==2:
            print("enter a number")
            number1 = int(input())
            print("enter a number")
            number2 = int(input())
            print('subtraction of {} and {} is {}'.format(number1,number2,Calculator.subtraction(number1,number2)))
        elif choice==3:
            print("enter a number")
            number1 = int(input())
            print("enter a number")
            number2 = int(input())
            print('multiplication of {} and {} is {}'.format(number1,number2,Calculator.multiplication(number1,number2)))
        elif choice==4:
            break
        else:
            pass        
                
            