#now we convert desimal to binary, hexadesimal and octal
#it is already define in python
#bin() , hex() and oct() all are built in function only for python not other programe
desimal=int(input("enter a desimal number"))
print("here desimal number is :",desimal)
binary=bin(desimal)
print("after binary conversion:",binary)
print("after octal conversion :",oct(desimal))
print("after hexadesimal conversion :",hex(desimal))