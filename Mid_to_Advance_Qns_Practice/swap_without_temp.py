#1. wap that swaps two variables without using third variables .
"""
a = int(input("Enter value for a : "))
b = int(input("Enter value for b : "))
print(f"Before swap : a = {a} and b = {b}")
b = a+b
a = b - a
b = b - a
print(f"After swap : a = {a} and b = {b}")

"""



'''2. Given a list of numbers . classify each number as positive , negative , or zero and count
how many fall into each category.
'''

n = int(input("Enter len of list : "))
list_num = []
neg_count = []
pos_count = []
zero_count = []
print(f"Enter {n} numbers into list")
for i in range(n):
    list_num.append(int(input(f"Enter : ")))
for i in list_num:
    if i < 0:
        neg_count.append(i)
    elif i >0 :
        pos_count.append(i)
    else:
        zero_count.append(i)
print(f"the list contain {len(pos_count)} positive numbers i.e {pos_count}")
print(f"the list contain {len(neg_count)} Negative numbers i.e {neg_count}")
print(f"the list contain {len(zero_count)} Zeros i.e {zero_count}")


