ms = [[2,7,6],
      [9,5,1],
      [4,3,8]]
sum=0
x=0
y=0
print("---------------------------------------------------------")
for i in ms:
    if ms[x][0]+ms[x][1]+ms[x][2]==15:
        print("YEAHHHH")
        sum+=1
    else:
        print("NOOOOOOOOHHH")
    x+=1
print("---------------------------------------------------------")
for i in ms:
    if ms[0][y]+ms[1][y]+ms[2][y]==15:
        print("YEAHHHH")
        sum+=1
    else:
        print("NOOOOOOOOHHH")
    y+=1
print("---------------------------------------------------------")
if sum==6:
    print("MAGIC SQUARE")
else:
    print("NOT A MAGIC SQUARE")
print("---------------------------------------------------------")

