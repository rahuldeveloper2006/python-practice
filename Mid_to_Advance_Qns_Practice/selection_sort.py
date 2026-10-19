# wap to sort the array in ascending order using selection sort
size = int(input("Enter size of the array : "))
arr = []
for i in range(size):
    arr.append(int(input("Enter element in array : ")))
#print the array
print(arr)
# now write logic to sort the array in asc order using selection sort
for i in range(size-1):
    lowest = i
    for j in range(i , size):
        if arr[lowest] > arr[j]:
            lowest = j

    #swap the array
    arr[i] = arr[lowest] + arr[i]
    arr[lowest] = arr[i] - arr[lowest]
    arr[i] = arr[i] - arr[lowest]

print(f"after from selection sort , the array is : {arr}")