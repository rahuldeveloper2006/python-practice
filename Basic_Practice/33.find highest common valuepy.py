#the logic of highest common value is the value which completely divisible without balace reminder
#now we try an example
#now we create a function
def hcv(num1,num2):
    if num1>num2:
        smaller=num2    
    else:
        smaller=num1
    for i in range(1,smaller+1):
        if(num1%i==0 and num2%i==0):
            hcf=i
    return hcf
num1=int(input("enter your 1st number"))
num2=int(input("enter your 2nd number"))
result=hcv(num1,num2)
print("the highest common factor of is :",result)
