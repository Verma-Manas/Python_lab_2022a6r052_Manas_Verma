'''num = int(input("Enter any integer : "))
if ( num > 10):
    print(num," is Greater than 10")
elif ( num == 10 ):
    print(num," is equal to 10")
else:
    print(num," is Smaller than 10")
print("\n\n")


#________________________________________________________________________________________



num_1 = int(input("Enter any integer : "))
if ( num % 2 == 0):
    print(num_1," is EVEN")
else:
    print(num_1," is ODD")
print("\n\n")


#________________________________________________________________________________________


'''
print("\n\n____________________________________________________________CALCULATOR______________________________________________________________\n\n")
while(1):
    print(" Enter '1' for Addition \n Enter '2' for Subtraction \n Enter '3' for Multiplication \n Enter '4' for Divide \n Enter '5' for Mod \n Enter '6' for Calculating average \n Enter '7' for Calculating percentage \n Enter '8' to exit \n Enter '9' for multiple inputs" )
    op = int(input(" Enter the Operator :"))
    if(op == 8):
        break
    if(op==6):
        sum_1 = 0
        total = int(input("Enter the total number of entries :"))       
        for i in range (1,total+1):
            nummm = int (input("Enter the number :"))
            sum_1 = sum_1 + nummm
        sum_1 = sum_1 / total
        print("Average : ", sum_1)
        
    elif(op==7):
        marks = int(input("Enter your Total marks : "))
        tot = int(input("Enter the Total marks that can be obtained :"))
        percent = (marks/tot) * 100
        print ("Percentage : ",percent)
        
    elif(op == 9):
        op = int(input("Enter the operator :"))
        b = int(input("Enter num 2 : "))
        if(op == 1):
            print("Addition : ",a+b)
            a  = a + b
        elif(op == 2):
            print("Subtraction : ",a-b)
            a  = a - b
        elif(op == 3):
            print("Muliplication : ",a*b)
            a  = a * b
        elif(op == 4):
            print("Quotient : ",a/b)
            a  = a / b
        elif(op == 5):
            print("Remainder : ",a%b)
            a  = a % b
        else:
            print("INVALID INPUT ")
        
    
        
    else:
        a = int(input("Enter num 1 : "))
        b = int(input("Enter num 2 : "))
        if(op == 1):
            print("Addition : ",a+b)
            a  = a + b
        elif(op == 2):
            print("Subtraction : ",a-b)
            a  = a - b
        elif(op == 3):
            print("Muliplication : ",a*b)
            a  = a * b
        elif(op == 4):
            print("Quotient : ",a/b)
            a  = a / b
        elif(op == 5):
            print("Remainder : ",a%b)
            a  = a % b
        else:
            print("INVALID INPUT ")
        
    print("\n\n\_____________________________________________________________THANKYOU_______________________________________________________________")


#________________________________________________________________________________________








