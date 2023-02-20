"""CREATING DATABSE AND ALL THE REQUIRED TABLES NEEDED TO RUN THE PROJECT
DATABASE NAME: Fashion_store
TABLES: customer, employees, product"""

import mysql.connector


def Create_Db():
    mydb=mysql.connector.connect(host="localhost",username="root",
                             password="1234")
    co=mydb.cursor()
    co.execute("CREATE DATABASE IF NOT EXISTS Fashion_store")
    co.close()
    mydb.close()


def Create_tb():
    mydb=mysql.connector.connect(host="localhost",username="root",
                             password="1234",
                            database="Fashion_store")
    co=mydb.cursor()
    co.execute('''CREATE TABLE IF NOT EXISTS customer(
               cust_id int primary key, cust_name varchar(20),
               last_name varchar(20),contact bigint,
               address varchar(30),booked_prod varchar(20))''')


    co.execute('''CREATE TABLE IF NOT EXISTS employees(
              emp_name varchar(20)
              , last_name varchar(20),
              contact bigint, address varchar(30))''')
    
    co.execute('''CREATE TABLE IF NOT EXISTS product(prod_no int,
                     prod_id varchar(10) primary key,
                     price int, stock int)''')
    co.close()
    mydb.close()
