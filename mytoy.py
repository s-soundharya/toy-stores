import mysql.connector
# Establishing connection
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root"
)

print(mydb)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS toystore")
mycursor.execute("USE toystore")

mycursor.execute("""
CREATE TABLE IF NOT EXISTS toys (
    id INT AUTO_INCREMENT PRIMARY KEY,
    toyname VARCHAR(255),
    type VARCHAR(255),
    price DECIMAL(10, 2),
    stock INT,
    available BOOLEAN,
    total DECIMAL(10, 2)
)
""")

def insert_toy():
    toyname = input("Enter toy name: ")
    type_ = input("Enter toy type: ")
    price = float(input("Enter toy price: "))
    stock = int(input("Enter toy stock: "))
    available = input("Is the toy available (yes/no)? ").lower() == 'yes'
    total = price * stock
    sql_insert = "INSERT INTO toys (toyname, type, price, stock, available, total) VALUES (%s, %s, %s, %s, %s, %s)"
    values_insert = (toyname, type_, price, stock, available, total)
    mycursor.execute(sql_insert, values_insert)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.\n-----------------------------------------------------------")

def update_toy():
    toy_id = int(input("Enter the toy ID to update: "))
    new_price = float(input("Enter the new price: "))
    sql_update = "UPDATE toys SET price = %s WHERE id = %s"
    values_update = (new_price, toy_id)
    mycursor.execute(sql_update, values_update)
    mydb.commit()
    print("Record updated.\n-----------------------------------------------------------")
    # Update total after price update
    mycursor.execute("UPDATE toys SET total = price * stock WHERE id = %s", (toy_id,))
    mydb.commit()

def delete_toy():
    toy_id = int(input("Enter the toy ID to delete: "))
    sql_delete = "DELETE FROM toys WHERE id = %s"
    mycursor.execute(sql_delete, (toy_id,))
    mydb.commit()
    print("Record deleted.\n-----------------------------------------------------------")

def display_toys():
    mycursor.execute("SELECT * FROM toys")
    myresult = mycursor.fetchall()
    print("Data in toys table:")
    for x in myresult:
        print(x)

while True:
    print("\nMenu:")
    print("1. Insert Toy")
    print("2. Update Toy Price")
    print("3. Delete Toy")
    print("4. Display Toys")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        insert_toy()
    elif choice == '2':
        update_toy()
    elif choice == '3':
        delete_toy()
    elif choice == '4':
        display_toys()
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please try again.")

mydb.close()

	
