#now we find duplicate charecter in a string
# str1=input("enter your about")
# list1=list(str1)
# list3=[]
# for index,i in enumerate(list1):
#     list2=list1.count(list1[index])
#     if(list2>1):
#         list3.append(list1[index])
# set1=set(list3)
# print("the duplicate latters in a string are written bellow")
# print(set1)

#and other method to find duplicate latter in a string
# def find_duplicate(string):
#     #create an empty dictionary to store charecter count
#     char_count={}
#     #initialize a list to store duplicate charecter
#     duplicate=[]
#     # iterate each charecter in the input string
#     for i in string:
#         #if the charecter already in a dictionary , i8ncrements its
#         if i in char_count:
#             char_count[i]+=1
#         else:
#             char_count[i]=1
#     for i,count in char_count.items():
#         if count>1:
#             duplicate.append(i)
#     return duplicate
# string=input("enter a string")
# duplicate_chars=find_duplicate(string)
# print("duplicate charecters are:",duplicate_chars)
