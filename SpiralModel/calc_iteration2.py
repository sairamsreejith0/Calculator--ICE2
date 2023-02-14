class Calculator2:
    def multiplication(value1,value2):
        return value1*value2 
    def division(value1,value2):
        return value1//value2
    
    

if __name__ == '__main__':
    while(True):
        print("menu")
        print("1.multiplication")
        print("2.division")
        print("3.exit")
        print("choose a number(1,2,3)")
        choice = int(input())
        if choice==1:
            print("enter a number")
            number1 = int(input())
            print("enter a number")
            number2 = int(input())
            print('multiplication of {} and {} is {}'.format(number1,number2,Calculator2.multiplication(number1,number2)))
        elif choice==2:
            print("enter a number")
            number1 = int(input())
            print("enter a number")
            number2 = int(input())
            if number2==0:
                print("undefined")
                continue            
            print('division of {} and {} is {}'.format(number1,number2,Calculator2.division(number1,number2)))
        elif choice==3:
           break
        else:
            pass        
                
            