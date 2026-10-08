#the cube sum of 1st nth natural number
n=int(input("enter your number"))
count=0
if(n<=0):
    print("please enter positive value")
else:
    for i in range(1,n+1):
        mul=i**3
        count=count+mul
    print("the cube sum of ",n,"natural number is :",count)