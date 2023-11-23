a=5
b=6
print(a<=b)
print(a<b)
print(b>=a)
print(b>a)
print(a!=b)
print(a+1==b)
print("a =",a,"b =",b)


#program 2
print("\n\n")
a='manas'
b=1
if a and b:
    print("True")
if a or b:
    print("True")
if not b:
    print("False")
else:
    print("True")

#program 3
print("\n\n")
i=0
list1 = []
dic={'manas':[101,20,30,40],'nandini':[102,20,30,40],'aru':[103,20,30,40],'mns':[104,20,30,40],'sanam':[105,20,30,40]}
print(list1)
for k,v in dic.items():
        print("Name :",k,"\nMarks :",v,"\n")
name = str(input("Enter the name:"))
for k,v in dic.items():
    if name == k:
        print("Name :",k,"\nMarks :",v,"\n")


#program 4

