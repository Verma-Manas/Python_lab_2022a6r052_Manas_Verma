
#___________________________FUNCTION CALLING___________________________________

a = 10
def change_value(a):
    a = 20
    print ("inside function value : ",a, "address :",id(a))
    return a

print ("before function:",a,"address :",id(a))
change_value(a)
print ("after function:",a,"address :",id(a),"\n")



#______________________FUNCTION CALLING USING LIST_____________________________

list_1 = [10,20,30,40,50]
def change_value_1(list_1):
    list_1[1] = 100
    print ("inside function value : ",list_1, "address :",id(list_1))
    return list_1

print ("before function:",list_1,"address :",id(a))
change_value_1(list_1)
print ("after function:",list_1,"address :",id(a))


#______________________________DEFAULT VALUE___________________________________

def fn(a,b=50):
    print("Value of a : ",a)
    print("Value of b : ",b)
