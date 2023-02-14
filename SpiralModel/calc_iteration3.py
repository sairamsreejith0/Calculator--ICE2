class Calculator3:
    def addition(value1,value2):
        return value1+value2
    def subtraction(value1,value2):
        return value1-value2 
    def multiplication(value1,value2):
        return value1*value2 
    def division(value1,value2):
        return value1//value2
    

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
        choice = int(input())
        if choice==1:
            print("enter a number")
            number1 = int(input())
            print("enter a number")
            number2 = int(input())
            print('addition of {} and {} is {}'.format(number1,number2,Calculator3.addition(number1,number2)))
        elif choice==2:
            print("enter a number")
            number1 = int(input())
            print("enter a number")
            number2 = int(input())
            print('subtraction of {} and {} is {}'.format(number1,number2,Calculator3.subtraction(number1,number2)))
        elif choice==3:
            print("enter a number")
            number1 = int(input())
            print("enter a number")
            number2 = int(input())
            print('multiplication of {} and {} is {}'.format(number1,number2,Calculator3.multiplication(number1,number2)))
        elif choice==4:
            print("enter a number")
            number1 = int(input())
            print("enter a number")
            number2 = int(input())
            if number2==0:
                print("undefined")
                continue            
            print('division of {} and {} is {}'.format(number1,number2,Calculator3.division(number1,number2)))
        elif choice==5:
            break
        else:
            pass        
                
            