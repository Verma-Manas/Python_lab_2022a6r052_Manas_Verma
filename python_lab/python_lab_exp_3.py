a = "Welcome to Python programming"
print (a)
while True:
    print("\n\nChoose the operation to perform \n1.Count the number of alphabets in the given string.\n2.To extract characters in the given string.\n3.Check if the string is alphanumeric or not.\n4.To extract by word input\n5.Exit")
    choice = int(input("Enter the choice 1/2/3/4 :"))

    if choice == 1:
        count = 0
        for i in a:
            if i.isalpha:
                count = count + 1
        print (count)
        
    elif choice == 2:
        print("\n1. Welcome\n2.to\n3.Python\n4.programming")
        extract = int(input("Choose the word to extract. 1/2/3/4/5 "))
        if(extract == 1):
            print(a[0:7])
        elif(extract == 2):
            print(a[8:11])
        elif(extract == 3):
            print(a[13:19])
        elif(extract == 4):
            print(a[21:32])
        else:
            print("Invalid input")
    elif choice == 3:
        if a.isalnum():
            print("Yes")
        else:
            print("No")

    elif choice == 5:
        break

    elif choice == 4:
        extract = str(input("Enter the extraction word:"))
        if(extract == 'Welcome'):
            print(a[0:7])
        elif(extract == 'to'):
            print(a[8:10])
        elif(extract == 'Python'):
            print(a[11:17])
        elif(extract == 'programming'):
            print(a[21:32])
        else:
            print("Invalid input")
    else:
        print("Invalid input")
        

#__________________DICTIONARY_____________________

        
d = {'key1': 1, 'key2': 2, 'key3': 3}
for k in d:
    print(k)
print(list(d))
print(type(list(d)))
while(1):
    print('*******DICTIONARY ITERATION********')
    print('1.Through Dictionary keys()')
    print('2.Through Dictionary values()')
    print('3.Through Dictionary items()')
    print('4.Exit')
    c=int(input('Enter Your Choice'))
    if(c==1):
        for k in d.keys():
            print(k)
        print(d.keys())
        print(type(d.keys()))
        print(list(d.keys()))
        print(type(list(d.keys())))
    elif(c==2):
        for v in d.values():
            print(v)
        print(d.values())
        print(type(d.values()))
    elif(c==3):
        for k, v in d.items():
            print('Keys=',k, 'Values=',v)
        print(d.items())
        print(type(d.items()))
    elif(c==4):
        break









        
