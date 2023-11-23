list_1 = [1,4,2,3,7,5,8,9]
'''x = int(input("Target :"))
count = 0
for i in range (len(list_1)):
    if x == list_1[i]:
        print("element found at index :",i)
        count = 1
        break
    if count != 1:
    print("Not found")'''



'''list_1.sort()
print(list_1)
y = int(input("Target :"))
for i in range (len(list_1)-1):
    mid = (len(list_1)) // 2
    if i <= mid :
        if mid == y :
            print ("found ",mid)
        else:
            list_1 = list_1[0:mid]

    elif i > mid:
        if mid == y :
            print ("found ",mid)
        else:
            list_1 = list_1[mid:len(list_1)-1]
    else:
        print("Not found ")
    i+=1'''


arr = [2,4,1,3,7,6,8,9,5]
arr = arr.sort
print( arr )
target = int(input("Target :"))
left, right = 0, len(arr) - 1

while left <= right:
    mid = (left + right) // 2 
    if arr[mid] == target:
        print("Element ",target," found at index ",mid)
        break  
    elif arr[mid] > target:
        right = mid - 1

    else:
        left = mid + 1
else:
    print("Element ",target," not found in the list.")
    
