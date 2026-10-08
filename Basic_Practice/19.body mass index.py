def body_mass(w,h):
    return round((w/h**2),2)
# 1 fit =30.48cm
# 1 fit = O.305 METER


HEIGHT=float(input("enter your height in fit"))
h=0.305*HEIGHT
print("your height in meter is:",h)
w=float(input("enter your weight in kg"))
print("your body weight is :",w)
bmi=body_mass(w,h)
print("bmi is :",bmi)
if(bmi<=18.5):
    print("your are under weight")
elif(18.5<bmi and bmi<=24.9):
    print("you are normal weight")
elif(25<bmi and bmi<=29.29):
    print("you are over weight")
else:
    print("you are obese")