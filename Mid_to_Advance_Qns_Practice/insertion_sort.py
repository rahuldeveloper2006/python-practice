# wap to sort the array in ascending order using insertion sort
'''
size = int(input("Enter size of the array : "))
arr1 = []
for i in range(size):
    arr1.append(int(input("Enter elements in array : ")))

print(arr1)
i = 0
while(i<size-1):
    j = i
    while(j>=0):
        if(arr1[j]>arr1[j+1]):
            arr1[j],arr1[j+1] = arr1[j+1],arr1[j]
        else:
            break
        j-=1
    i+=1

print(arr1)
'''





# wap to sort the array in descending order using insertion sort


size = int(input("Enter size of the array : "))
arr1 = []
for i in range(size):
    arr1.append(int(input("Enter elements in array : ")))

print(arr1)
i = 0
while(i<size-1):
    j = i
    while(j>=0):
        if(arr1[j]<arr1[j+1]):
            arr1[j],arr1[j+1] = arr1[j+1],arr1[j]
        else:
            break
        j-=1
    i+=1

print(arr1)