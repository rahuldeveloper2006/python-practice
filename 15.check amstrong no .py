# num=int(input("enter your number"))
# num_str=str(num)
# num_digit=len(num_str)
# temp_num=num
# zero=0
# while(num>0):
#     reminder=num%10
#     zero=zero+reminder**num_digit
#     num=num//10
# if(zero==temp_num):
#     print(temp_num," is an amstrong number")
# else:
#     print(temp_num,"is not an amstrong number ")

#now we write a programe to print amstrong number in the interval
num1=int(input("enter your starting number"))
num2=int(input("enter your ending number"))
print("amstrong numbers are")
for i in range(num1,num2+1):
    str_i=str(i)
    temp_i=i
    i_digit=len(str_i)
    ans=0
    while(i>0):
        reminder=i%10
        ans=ans+reminder**i_digit
        i=i//10
    if(temp_i==ans):
            print(temp_i)
            