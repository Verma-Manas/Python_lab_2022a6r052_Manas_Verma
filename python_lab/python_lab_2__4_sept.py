#using functions:

#abs()
print(abs(-10)) 

#len
print(len("WELCOME TO MIET"))

#min()
print(min([10,20,1,200]))

#round
print(round(3.14556))

#isalnum
print("CSE, 3rd sem".isalnum())
print("123abc".isalnum())

#type
print(type(10))
print(type("AI AND ML"))

#all

list1 = [True,True,True]
list2 = [True,False,False]
print(all(list1))
print(all(list2))

#any
list3 = [False,False,False]
list4 = [True,False,False]
print(all(list3))
print(all(list4))

#ascii
print(ascii("Kot,\nBhalwal!"))

#ord
print(ord("a"))
print(ord(" "))
print(ord(","))
print(ord("*"))

#bin
print(bin(10))
print(bin(15))

#bool
print(bool(0))
print(bool(42))
print(bool([]))
print(bool([1,2]))

#byte array
byte_array = bytearray([65,66,67])
print(byte_array)
byte_array[0] = 88
print(byte_array)

#bytes
byte_string = bytes([68,69,70])
print(byte_string)

#callable
def my_function():
    return 42
print(callable(my_function))
print(callable(42))




