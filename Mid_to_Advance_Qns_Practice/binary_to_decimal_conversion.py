#1. wap to convert binary to its decimal equivalent

""" 
num = int(input("Enter Binary number : "))
ans = 0
pow = 0
while(num>0):
    remind = num%10
    ans = ans + (remind * (2**pow))
    pow+=1
    num = num//10

print(f"its decimal equivalent is = {ans}")

 """



#2.Wap to add the digit of a number and give a single output
"""
num = int(input("enter a number : "))
ans = 0
while(num>9):
    ans = 0
    while(num>0):
        remind = num%10
        ans = ans + remind
        num = num // 10
    num = ans

print(f"After adding all digits of a number , then its single output is : {ans}")

"""


# 3. wap which print reverse of a number

num = int(input("Enter a number : "))
ans = 0
temp = num
while(num>0):
    remind = num % 10
    ans = ans * 10 + remind
    num = num // 10
print(f"Reverse of {temp} is {ans}")