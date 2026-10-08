#now we write a programe to print sum of arrey
# arrey=[]
# num1=int(input("enter number for fulfill arrey"))
# for i in range(num1):
#     num2=int(input("enter number"))
#     arrey.append(num2)
# #now we use reduction() function
# from functools import reduce
# sum_arrey=reduce(lambda x,y:x+y,arrey)
# print(f"sum of arreys  are ={sum_arrey}")
# #__________________________________________________________________________________
#now we write a programe to find a arrey is monotonic or not 
#its logic is=if elemrnts of arrey arranged in increasing or decreasing order then the arrey is monotonic
# if the arrey elements arranged multiple of increasing and decreasing that is called non monotonic arrey
lenarrey=int(input("enter the length of arrey"))
arrey=[]
for i in range(lenarrey):
    arr=int(input("enter arrey element"))
    arrey.append(arr)
print(arrey)
# print(arrey1)
temp1=arrey
temp2=arrey
print(temp1.sort())
print(temp1)
print(temp2.sort(reverse="true"))
print(temp2)
if(arrey==temp1):
    print(f"the arrey {arrey} is monotonic")
elif(arrey==temp2):
    print(f"the arrey  {arrey} is monotonic ")
else:
    print("the arrey is not monotonic")
             