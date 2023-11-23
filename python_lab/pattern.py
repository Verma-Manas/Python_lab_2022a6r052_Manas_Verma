for i in range (0,7):
    for j in range (0,7):
        if i+j==i or i+j==j or i==6 or j==6:
            print(1,"  ",end="")
        elif i+j==i+1 or i+j==j+1 or i==5 or j==5:
            print(2,"  ",end="")
        elif i+j==i+2 or i+j==j+2 or i==4 or j==4:
            print(3,"  ",end="")
        elif i+j==i+3 or i+j==j+3 or i==3 or j==3:
            print(4,"  ",end="")
    print("\n")
