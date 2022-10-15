import sqlite3 #a library just like flask
# \ this means continue reading
connection=sqlite3.connect("library.db") #name of the database file, will create if does not exist

try: 
   connection.execute("CREATE TABLE Book (ID INTEGER PRIMARY KEY, Title TEXT)")
except: 
    print("Table already created") 

while True: 
    id=input("Enter Book ID:")
    title=input("Enter Book title:")
    if id=="": 
        break
    try: 
        connection.execute(f"INSERT INTO Book(ID, Title) " +
                            "VALUES(?, ?)", (id, title)) #? acts as a place holder 
        connection.commit()
    except: 
        print("book already found")

def del0(bk_id): 
    connection.execute("DELETE FROM Book WHERE ID=?", (bk_id, ))
    print(f"book{bk_id} deleted")
    connection.commit()

del0("1")
connection.close()
