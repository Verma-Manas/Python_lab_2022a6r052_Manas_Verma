odd=[]
eve=[]
i=1
while(i<=40):

    if(i%2==0 and i<=20):
        if(i==2):
            print("EVEN NUMS :")
        print(i)

    if(i%2!=0 and i>=20):
        if(i==21):
            print("\nODD NUMS :")
        print(i-20)
    i+=1
