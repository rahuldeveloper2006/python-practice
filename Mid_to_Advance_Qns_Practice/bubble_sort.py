# wap to sort the array in ascending order using bubble sort
size = int(input("Enter size of the array : "))
arr1 = []
for i in range(size):
    arr1.append(int(input("Enter element in array : ")))
print(arr1)
i=size-1
while(i > 0):
    j = 0
    swapped = False
    while(j < i):
        if(arr1[j]>arr1[j+1]):
            arr1[j] = arr1[j]+arr1[j+1]
            arr1[j+1] = arr1[j]-arr1[j+1]
            arr1[j] = arr1[j]-arr1[j+1]
            swapped = True
        j+=1
    if not swapped:
        break
    i-=1

print(f"after sorted in ascending order, the array is {arr1}")



'''its best time complexity is O(n)
worst and average tme complexity is O(n**2)'''

