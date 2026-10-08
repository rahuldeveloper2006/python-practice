panctuation='''<>"{ }()|/;:?.,#@!$%&~`'''
my_str=input("enter your string")
no_punct=""
for char in my_str:
    if char not in panctuation:
        no_punct=no_punct+char

print(no_punct)