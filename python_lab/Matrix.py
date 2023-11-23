List_1 = [[1,2,3,4],
          [5,6,7,8],
          [9,10,11,12],
          [13,14,15,16]]
print("program_1")
count = 0
for m in List_1:
    for n in m:
        count=count+n
        print(n,end=" ")
    print()
print("sum =",count)
print("\n\n")


print("program_2")
count1=0
count2=0
for m in List_1:
    for n in m:
        if(n%2==0):
            count1+=1
            count2+=n
print("Num of even nums =",count1,"\nTheir sum =",count2)
print("\n\n")


print("program_3")
count3 = 0
for m in List_1[1]:
    count+=m
print("sum of row 2 =",count3)
print("\n\n")


print("program_4")
count4 = 0
for m in List_1:
    for n,e in enumerate(m):
        if(n%2==0):
            count4+=e
print("sum of even index elements =",count4)
print("\n\n")


print("program_5")
count6 = 0
for m in List_1:
        count6+=m[3]
print("sum =",count6)
print("\n\n")



count5 = 0
print("program_6")
for m in List_1:
    for n,e in enumerate(m):
        if(List_1[n]==m):
            count5+=e
print("sum of diagonal elements =",count5)
print("\n\n")



count7 = 0
print("program_7")
for m in range(0,len(List_1)):
    for n in range(0,len(List_1[m])):
        if(n+m==3):
            print()
            count7+=List_1[m][n]
print("sum of diagonal elements =",count7)
print("\n\n")



print("program_8")
x = int(input("ENTER row number to be reversed :"))

if(x==1):
            List_1[0].reverse()
            print(List_1[0])
elif(x==2):
            List_1[1].reverse()
            print(List_1[1])
elif(x==3):
            List_1[2].reverse()
            print(List_1[2])
elif(x==4):
            List_1[3].reverse()
            print(List_1[3])

