class Calculator2:                         #2nd iteration
    def multiplication(value1,value2):     #multiplication function to multiply two numbers
        return value1*value2 
    def division(value1,value2):           #division function to multiply two numbers
        return value1//value2              #integer division
    
    

if __name__ == '__main__':
    while(True):                                         
        print("menu")
        print("1.multiplication")
        print("2.division")
        print("3.exit")
        print("choose a number(1,2,3)")
        try:
            choice = int(input())
        except Exception as err:
            print(err)
            continue    
        if choice==1:
            try:
                print("enter a number")
                number1 = int(input())
                print("enter a number")
                number2 = int(input())
                print('multiplication of {} and {} is {}'.format(number1,number2,Calculator2.multiplication(number1,number2)))
            except Exception as err:
                print(err)      
        elif choice==2:
            try:
                print("enter a number")
                number1 = int(input())
                print("enter a number")
                number2 = int(input())
                print('division of {} and {} is {}'.format(number1,number2,Calculator2.division(number1,number2)))
            except Exception as err:
                print(err)            
           
        elif choice==3:
           break
        else:
            pass        
                
            