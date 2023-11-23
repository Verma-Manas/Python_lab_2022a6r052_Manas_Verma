def add(a,b):
    return ("Sum:",a+b)
def sub(a,b):
    return ("Sub:",a-b)
def mult(a,b):
    return ("Mult:",a*b)
def div(a,b):
    return ("Div",a/b)
def rem(a,b):
    return ("Rem",a%b)
a=int(input("Enter num 1:"))
b=int(input("Enter num 2:"))
choice=input("Enter you choice \n1 for add\n2 for subtract\n3 for multiply\n4 for divide\n5 for mod")
res=str(res)
if choice==1:
    res=add(a,b)
if choice==2:
    res=sub(a,b)
if choice==3:
    res=mult(a,b)
if choice==4:
    res=div(a,b)
if choice==5:
    res=rem(a,b)
print(res)
