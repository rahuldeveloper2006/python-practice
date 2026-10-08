#now we write a programe to find factorial of a number and also find the number of '0' digit in result of factorial
num=int(input("enter a number for find its factorial"))
#now we find the factorial of given number
temp=num
ans=1
while(temp>0):
    ans=ans*temp
    temp=temp-1
    count=0
print(f"the factorial of {num} is {ans}")
#now we find number of 0 digit in result
lis=[int(d) for d in str(ans)]
for i,value in enumerate(lis):
    if(lis[i]==0):
        count=count+1
print("the number of 0 digit is :",count)