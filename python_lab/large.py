mydic = {'Alice' : 92,'Bob' : 85, 'Charlie' : 78, 'David' : 95,'Eve' : 88}
large = 0
for k, v in mydic.items():
    if v > large:
        large = v
        name = k
    else:
        continue
print(name,":",large)

a = 10
b = 20
c = 30
if a > b and a > c:
    print("a is largest")
elif b > a and b > c:
    print("b is largest")
elif c > b and c > a:
    print("c is largest")

