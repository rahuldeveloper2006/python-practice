'''the logic of palindrum number IS=
REVERSE ORDER OF A NUMBER=THAT NUMBER
EX=121 its reverse order is same i.e 121 so here 121 is called palindrum number.'''
n=int(input("enter your number"))
rev=0
temp=n
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
print(rev)
if(temp==rev):
    print(temp,"palindrum number")
else:
    print(temp,"not palindrom number")