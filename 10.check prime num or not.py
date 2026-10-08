# num=int(input("enter your number for check prime or not"))
# count=0
# for i in range(1,num+1):
#     if(num%i==0):
#         count=count+1
# if(count<=2):
#     print(num,"is a prime number")
# else:
#     print(num,"is not a prime number")
#now we print all prime number in the interval
num1=int(input("enter starting number"))
num2=int(input("enter ending number"))
sum=0
i=1
list=[i for i in range(num1,num2+1)]
print(list)
i=1
j=0
while(i<=list[j]):
    if(list[j]%i==0):
        sum=sum+1
        if(sum>2):
            i=i+1
            j=j+1
        elif():
            print()

