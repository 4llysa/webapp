import sqlite3

connection=sqlite3.connect("library.db")
cursor=connection.execute("SELECT ID, Title FROM Book ")

#cursor will be an iterable
for row in cursor:
    print(row[0],row[1]) 
    #row is a tuple

connection.row_factory=sqlite3.Row #instead of returning a tuple, it will return a python dictionary object  
cursor=connection.execute("SELECT ID, Title FROM Book ")
#cursor will be an iterable
for row in cursor:
    print(f"{row['Title']}{row['ID']}") 
    #row is a dict

connection.close()

