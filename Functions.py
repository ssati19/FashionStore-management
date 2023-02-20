import mysql.connector

mydb=mysql.connector.connect(host="localhost",username="root",password="1234",
                             database="Fashion_store")

co=mydb.cursor()


#To check existing customer or create new account
a=[]
co.execute("select cust_id from customer")
result=co.fetchall()
for i in result:
    a.append(i[0])
    
def create_acc():
    id=int(input("Enter ID: "))
    if id in a:
        print("This id already exists")

    else:
        print("Hello sir/madam, kindly fill all the details")
        name=input("enter your first name: ")
        last=input("enter your last name: ")
        con=input("enetr your contact no.: ")
        add=input("enter you address: ")
        order=input("enter your booked product: ")
        
        
        query="""insert into customer values({},'{}','{}',
        {},'{}','{}')""".format(id,name,last,con,add,order)
        co.execute(query)
        mydb.commit()
        print("details added successfully")


#Function for customer login
def cust_login():
    id=int(input("please enter your id"))
    
    if id in a:
        while True:
            print(''' What do you want:
                    1. Enter 1 to view your Order details
                    2. Enter 2 to update order details
                    3. ENter 3 to cancel Booked products
                    4. Exit
                            ''')
            choice=int(input("enter your choice: "))
            
            if choice==1:
                query="""select booked_prod from
                    customer where cust_id ={}""".format(id)
                co.execute(query)
                result=co.fetchone()
                print(result)
                    
            elif choice==2:
                n=input("enter the product you want to update: ")
                query="""update customer set booked_prod='{}'
                    where cust_id={}""".format(n,id)
                co.execute(query)
                mydb.commit()
                print("updated successfully")

            elif choice==3:
                query="delete from customer where cust_id={}".format(id)
                co.execute(query)
                mydb.commit()
                print("deleted successfully")
            else:
                break
    else:
        print("Please enter a valid ID")

#product function
def prod():
    query="select * from product"
    co.execute(query)
    result=co.fetchall()
    for i in result:
        print(i)



#To add product function
def add_prod():
    n=int(input("how many product details you want to enter: "))
    for i in range(n):
        a=int(input("enter product no.: "))
        b=input("enter product id: ")
        c=int(input("enter product price: "))
        d=int(input("enter product stock: "))
        query='''insert into product values
        ({},'{}',{},{})'''.format(a,b,c,d)
        co.execute(query)
        mydb.commit()
    print("product added")

    
#Delete a product function
def del_prod():
    m=input("Enter id of product to be deleted")
    query="delete from product where prod_id='{}'".format(m)
    co.execute(query)
    mydb.commit()
    print("deleted successfully")



#Employee Login Function
def emp_login():
    
    query="select emp_id from employees"
    co.execute(query)
    result=co.fetchall()
    e=[]
    for i in result:
        e.append(i[0])
    n=int(input("enter your employee login id"))
    if n in e:
        while True:
            print('''
                     1. add a new product
                     2. delete a prdouct
                     3. exit
                     ''')
            choice=int(input("enter your choice: "))
            if choice==1:
                add_prod()
            if choice==2:
                del_prod()
            else:
                break
    else:
        print("not a valid choice")

#Add employee function.
def add_emp():
    a=int(input("enteremployee id: "))
    b=input("enter employee name: ")
    c=input("enter employee last name: ")
    d=int(input("enter employee phone no.: "))
    e=input("enter employee address: ")
    query='''insert into employees values
    ({},'{}','{}',{},'{}')'''.format(a,b,c,d,e)
    co.execute(query)
    mydb.commit()
    print("employee added successfully")



#Employer Login           
def employer_login():
    while True:
        print('''
1. view all product
2. add a new employee
3. Exit''')
        choice=int(input("enter your choice: "))
        if choice ==1:
            prod()       
        elif choice==2:
            add_emp()    
        else:
            break
