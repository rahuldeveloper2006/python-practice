#now we find natuiral logarithenm of any number
#logarithem is a built in function in python
import math
def logarithem(num):
    number=math.log(num)
    print(f"the natural logarithem of {num} is ={number}")
num=float(input("enter your number"))
logarithem(num)