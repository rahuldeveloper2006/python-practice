#now we write a programe to find factorial of a number by using recursion 
#logic of factorial is => factorial of n= n*factorial(n-1)
def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
       return n*factorial(n-1)
 #now we call the function for operation the specified task
factorial(3)
print(factorial(3))