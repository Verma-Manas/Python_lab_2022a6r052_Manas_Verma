string = "malayalam"
string2=[]
st=[]
print(string)
for i in range(len(string)-1,-1,-1) :
                string2.append(string[i])
print(string2)
for i in range(0,len(string)) :
                st.append(string[i])
print(st)
if st==string2:
    print("yes")
else:
    print("no")


#program2
print("\n\n\n")
a = (input("Enter string1:"))
b = (input("Enter string1:"))

count = 0
for i in range(0,len(a)) :
    for j in range(0,len(a)) :
        if a[i] == b[j]:
            count+=1
if count==len(a):
    print("YES")
else:
    print("NO")

#program2.2
sorted(a)
sorted(b)
if a==b:
    print("YES")
efelse:
    print("NO")
