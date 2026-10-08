# # given a dictionary , now we find max and min value of dictionary and swap them....after swap update the dictionary and print it
# X={
#     "F":28, "C":15, "E":81, "M":19, "G":2
# }
# print("before update the dictionary is :",X)

# #  step-1 : now i convert from dictionary to list for find maximum and minimum value

# X_list=list(X.values())

# # step-2 : find max and min value

# max_index=X_list.index(max(X_list))
# min_index=X_list.index(min(X_list))

# # step-3 : now swap the max and min value

# X_list[max_index], X_list[min_index]=X_list[min_index],X_list[max_index]

# # step-4 : now we update dictionary
# keys=list(X.keys())
# update_X=dict(zip(keys,X_list))

# print("after update the dictionary is ", update_X)


X={
    "F":28, "C":15, "E":81, "M":19, "G":2
}
print("before update the dictionary is :",X)
max_key=max(X,key=X.get)
min_key=min(X,key=X.get)

X[max_key],X[min_key]=X[min_key],X[max_key]

print("after update the dictionary is :",X)