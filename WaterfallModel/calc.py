class Calculator:
    def addition(value1,value2):  #addition function to add two numbers
        return value1+value2

    def subtraction(value1,value2): #subtraction function to subtract two numbers
        return value1-value2 

    def multiplication(value1,value2): #multiplication function to multiply two numbers
        return value1*value2 

if __name__ == '__main__':
    while(True):                        #continuously prompts menu to user until exit
        print("menu")                   #giving options to user to choose addition,subtraction,multiplication,division or exit
        print("1.addition")
        print("2.subtraction")
        print("3.multiplication")
        print("4.Exit")
        print("choose a number(1,2,3 or 4)")
        choice = int(input())                #taking input from user
        if choice==1:                        #if the user gives 1 as input perform addition
            print("enter a number")
            number1 = int(input())           #reading 1st number 
            print("enter a number")
            number2 = int(input())           #reading 2nd number
            print('addition of {} and {} is {}'.format(number1,number2,Calculator.addition(number1,number2))) #calling addition function by passing number1 and number2
        elif choice==2:                      #if the user gives 2 as input perform subtraction
            print("enter a number")
            number1 = int(input())           #reading 1st number
            print("enter a number")       
            number2 = int(input())           #reading 2nd number
            print('subtraction of {} and {} is {}'.format(number1,number2,Calculator.subtraction(number1,number2)))  #calling subtraction function by passing number1 and number2
        elif choice==3:                      #if the user gives 3 as input perform multiplication
            print("enter a number")
            number1 = int(input())           #reading 1st number
            print("enter a number")
            number2 = int(input())           #reading 2nd number
            print('multiplication of {} and {} is {}'.format(number1,number2,Calculator.multiplication(number1,number2))) #calling multiplication function by passing number1 and number2
        elif choice==4:                      #if the user gives 4 as input then exit 
            break
        else:                                #if the user gives any other input other than 1,2,3,4 then ignore
            pass        
                
            