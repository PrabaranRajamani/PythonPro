import mysql.connector
from tabulate import tabulate

# Replace 'your_username', 'your_password', and 'your_database' with actual values
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Google_9443",
    database="practice"
)

def insert(NAME, CLASS, DOB, CITY):
    res = con.cursor()
    sql = "INSERT INTO users (NAME, CLASS, DOB, CITY) VALUES (%s, %s, %s, %s)"
    user = (NAME, CLASS, DOB, CITY)
    res.execute(sql, user)
    con.commit()
    print("Insert Data Success")
def select():
    res = con.cursor()
    sql = "SELECT ID, NAME , CLASS , DOB, CITY FROM users"
    res.execute(sql)
    result = res.fetchall()
    print(tabulate(result))

def update(NAME,CLASS,DOB,CITY,ID):
    res = con.cursor()
    sql = "INSERT INTO users (NAME = %s, CLASS = %s, DOB = %s, CITY =%s ) VALUES where ID = %s"
    user = (NAME, CLASS, DOB, CITY,ID)
    res.execute(sql, user)
    con.commit()
    print("Insert update Success")

def delete(ID):
    res = con.cursor()
    sql = "delete from users where ID = %s"
    user = (ID,)
    res.execute(sql, user)
    con.commit()
    print("Data delete Success")



while True :
    print("1.INSERT DATA")
    print("2.SELECT DATA")
    print("3.UPDATE DATA")
    print("4.Delete data")

    choice = int(input("Enter the choice: "))

    if choice == 1:
        NAME = input("Enter the name: ")
        CLASS = input("Enter the class: ")
        DOB = input("Enter the DOB: ")
        CITY = input("Enter the CITY: ")
        insert(NAME, CLASS, DOB, CITY)

    elif choice == 2:
        select()
    elif choice == 3:
        ID = input("Enter the ID: ")
        NAME = input("Enter the NAME: ")
        CLASS = input("Enter the class: ")
        DOB = input("Enter the DOB: ")
        CITY = input("Enter the CITY: ")
        update(NAME, CLASS, DOB, CITY, ID)
    elif choice == 4:
        ID = input("Enter the ID:")
        delete(ID)