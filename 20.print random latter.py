# import random
# import string
# random_latter=random.choice(string.ascii_letters)
# print(random_latter)


#now we print random string in python
import random
string=("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
a=random.sample(string,3)
b="".join(a)
print("random string:",b)