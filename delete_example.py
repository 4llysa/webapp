import sqlite3

connection=sqlite3.connect("library.db")
id=input("enter book to be deleted")
cursor=connection.execute("DELETE FROM Book WHERE ID=?", (id, ))
if cursor.rowcount == 0: 
    print("nothing deleted")

connection.commit()
connection.close()

