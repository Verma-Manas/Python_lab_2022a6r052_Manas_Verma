c = int(input("Enter temperature in celcius : "))
print (c,"°C is equals to ",(c*9/5)+32,"°F)
f = int(input("Enter temperature in Farenheit : "))
print (f,"°F is equals to ",(f-32)*(5/9),"°C")

row = int(input("Enter num:"))
for i in range(1,row+1):
    for j in range(i):
        print("# ",end="")
    print("\n")

