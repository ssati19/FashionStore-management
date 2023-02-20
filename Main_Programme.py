import Database
import Functions

Database.Create_Db()
Database.Create_tb()


print("WELCOME!")
while True:
    print('''
Enter A if you're a Customer:
Enter B if you're a Employee:
Enter C if you're a Employer:
Enter E to exit''')
    choice=input("enter your choice: ")

    
    if choice=="A":
        print('''
        1. create a new account
        2. sign-in into existing account''')
        choice2=int(input("enter choice: "))
        if choice2==1:
            Functions.create_acc()     
        elif choice2==2:
            Functions.cust_login()      
        else:
                break
    elif choice=="B":
        Functions.emp_login()
    elif choice== "C":
        Functions.employer_login()    
    else:
        print("THANKS FOR VISITING")
        break
