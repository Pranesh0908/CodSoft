a="yes"
while a=="yes":
    num1=int(input("Enter the number 1:"))
    num2=int(input("Enter the number 2:"))
    
    print("Enter 1 to Add")
    print("Enter 2 to Subtract")
    print("Enter 3 to Multiply")
    print("Enter 4 to Divide")
    option=int(input("Enter the option:"))
    
    if(option==1):
        print("The sum is:",num1+num2)

    elif(option==2):
        print("The difference is:",num1-num2)

    elif(option==3):
        print("The product is:",num1*num2)

    elif(option==4):
        print("The Quotient is:",num1/num2)

    else:
        print("The option in invalid")
    a=input("Do you want to continue? (yes or no):")
