# class Customers:
#     # Create a static variable and store a dictionary
#     order_detail = {
#         1: {
#             "name": "R",
#             "Customer_id": "123@gmail.com",
#             "Purchasing_amount": 23451,
#             "item": "Hand Drill",
#         },
#         2: {
#             "name": "P",
#             "Customer_id": "456@gmail.com",
#             "Purchasing_amount": 555677,
#             "Item": "Welding machine",
#         },
#         3: {
#             "name": "J",
#             "Customer_id": "789@gmail.com",
#             "Purchasing_amount": 899,
#             "Item": "Sandpaper",
#         },
#         4: {
#             "name": "A",
#             "Customer_id": "389@gmail.com",
#             "Purchasing_amount": 48658,
#             "Item": "Machine Tools",
#         },
#     }

#     def __init__(self, name, order_id):
#         self.name = name
#         self.order_id = order_id

#     def customer_detail(self):
#         print(f"Customer name:{self.name}")
#         print(f"order_id:{self.order_id}")


# name = input("Enter your name:")
# order_id = int(input("Enter you order_id:"))
# C1 = Customers(name, order_id)
# x = C1.customer_detail()
# C2 = Customers.order_detail
# if (
#     order_id in C2
# ):  # CHECK IF order_id is in the given dictionary & if found then iterate over the items and print the items in dictionary
#     C2[order_id].items()
#     for i, v in C2[order_id].items():
#         print(i, ":", v)

# else:
#     print("ERROR:ID NOT FOUND")


import mysql.connector


database = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="0483@8340403952@0509",
    database="ruchisnewdatabase",
)

mycursor = database.cursor()
# CREATE TABLES
""" Customer_details = "CREATE TABLE IF NOT EXISTS CustomerDetail (Name VARCHAR(255),customerID VARCHAR(255) PRIMARY KEY NOT NULL );"
Order_Details = "CREATE TABLE IF NOT EXISTS OrderDetail (OrderID int AUTO_INCREMENT PRIMARY KEY NOT NULL, customer_ID VARCHAR(255) NOT NULL);"
Item_Details = "CREATE TABLE IF NOT EXISTS ItemDetail(Order_ID int AUTO_INCREMENT PRIMARY KEY NOT NULL,Item VARCHAR(200),Amount int);"
"""
"""
mycursor.execute(Customer_details)
mycursor.execute(Order_Details)
mycursor.execute(Item_Details)"""
# ADD FOREIGN KEY CONSTRAINTS
"""mycursor.execute("ALTER TABLE OrderDetail  ADD CONSTRAINT FK_customerID FOREIGN KEY (customer_ID) REFERENCES CustomerDetail (customerID);")
mycursor.execute("ALTER TABLE ItemDetail ADD CONSTRAINT FK_OrderID FOREIGN KEY (Order_ID) REFERENCES OrderDetail (OrderID);)
"""


def Take_orders(x):
    if x == 1:
        name = input("Enter your name: ")
        customer_id = input("Enter your customer_id(mail-id) :")
        item_purchased = input("Enter the Item name: ")
        amount = int(input("Enter the price of item: "))
        # Insert data into CustomerDetail table
        mycursor.execute(
            """
            INSERT IGNORE INTO CustomerDetail ( customerID , Name)
            VALUES (%s,%s)
            """,
            (customer_id, name),
        )
        # Insert data into OrderDetail table
        mycursor.execute(
            """
            INSERT IGNORE INTO OrderDetail (customer_ID)
            VALUES (%s)
            """,
            (customer_id,),
        )
        # Insert data into ItemDetail table
        mycursor.execute(
            """
            INSERT IGNORE INTO ItemDetail (Item,Amount)
            VALUES(%s,%s) 
            """,
            (item_purchased, amount),
        )

        database.commit()
        print("Order processed successfully")

    elif x == 2:
        customer_id = input("Enter your customer_id(mail-id) :")

        mycursor.execute(
            "SELECT * FROM (SELECT O.OrderID, I.Item,I.Amount from OrderDetail O JOIN ItemDetail I ON I.Order_ID = O.OrderID) WHERE customerID =%s",
            (customer_id,),
        )

        rows = mycursor.fetchall()
        for y in rows:
            print(y)
    elif x == 0:
        print("You have exited the page")
        database.close()


x = 3
while x != 0:
    print("Select an option: ")
    print("1. Take Orders")
    print("2. Print Order")
    print("0.Exit")
    x = int(input("Enter an option: "))
    Take_orders(x)
if database:
    database.close()
    print("\n The Mysql connection is closed.")
