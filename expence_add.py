# now we write a programe to add,view,and calculate total expense
def expense_add():
    print("enter your all expense")
    while("true"):
        category=input("enter your expense category")
        amount=float(input("enter its amount"))
        string=f"{category}={amount}\n"
        with open("store.txt","a") as f:
            f.write(string)
        doubt=input("are you want to add next expence")
        if(doubt=='no'):
            break
def expence_show():
    print("your all expence are printed bellow")
    with open("store.txt","r") as f:
        print(f.read())

def exit_app():
    print("thanks for using me \n good by \n enjoy your life")
while('true'):
    choice=int(input("enter 1 for add expence \n enter 2 for show all expence \n enter 3 for exit the app"))
    if(choice==1):
        expense_add()
    elif(choice==2):
       expence_show()
    elif(choice==3):
       exit_app()
       break
    else:
       raise ValueError("please enter choice between 1 and 3")