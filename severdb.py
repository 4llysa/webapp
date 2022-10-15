import sqlite3
print("hello")
from flask import Flask #flask is a library that contains the class Flask
from flask import render_template  #this is a function
from flask import request ##request is an object (object≠class, object has already been created by another class)
from flask import redirect ##redirect function (302)
app=Flask(__name__) #anything that has 2 underscores have already been predefined

@app.route("/") #default method is get
def root(): 
    try: 
        connection=sqlite3.connect("catalogue.db")
        connection.execute("CREATE TABLE Products (Name TEXT PRIMARY KEY, Price TEXT, Description TEXT, Image TEXT)")
    except: 
        print("Table already created") 

    connection=sqlite3.connect("catalogue.db")
    print("hello2")
    connection.row_factory=sqlite3.Row
    cur=connection.execute("SELECT * FROM Products")
    rows=cur.fetchall() #returns list of dictionary objects
    connection.close()
    print(rows)
    return render_template("products1.html",products=rows)
    #jinja template tool/engine 

@app.route("/form") #DECORATOR. one line before function signature, this is a python syntax: to do something before the function is invoked
def home(): 
    #return "<h1>Hello World<h1>"
    return render_template("webform.html") 

@app.route("/submit",methods=["POST"])
def submit():
    file_name=""
    if "image" in request.files: #stored in request.files dictionary, looking for dictionary key image  
        file_obj=request.files["image"] #contains the actual content of the file (bitmap image)
        file_name=file_obj.filename #filename is an atr from flask
        file_obj.save(f"static/images/{file_name}")
        print("hello")
    connection=sqlite3.connect("catalogue.db")
    connection.execute("INSERT INTO Products(Name, Price, Description, Image) VALUES (?,?,?,?)",(request.form['product'],request.form['description'],request.form['price'],file_name))
    connection.commit()
    connection.close()
    return redirect("/")
    #f"{request.form['product']}+{request.form['description']}+{request.form['price']}"
    #request.form creates a python dictionary object 

@app.route("/edit/<product>")
def edit_product(product):
    try:
        con= sqlite3.connect("catalogue.db")
        con.row_factory=sqlite3.Row
        cur = con.execute("SELECT * FROM Products WHERE Name=?", (product,))
        row=cur.fetchone()
        con.close()
        print(row)
    except Exception as e:
        print(str(e))
    return render_template("product_edit.html",data=row)

@app.route("/update/<product>",methods=["POST"])
def update_product(product):
    file_name=""
    print("request files", request.files)
    if "image" in request.files: 
        file_obj=request.files["image"]
        file_name=file_obj.filename
        try:
            file_obj.save(f"static/images/{file_name}")
        except: 
            pass
    #connect to data base
    connection=sqlite3.connect("catalogue.db")
    connection.row_factory=sqlite3.Row
    if request.form["submit"]=="update" and file_name=="":
        cur=connection.execute("UPDATE Products SET Name=?, Description=?, Price=? WHERE Name=?",
        (request.form['name'],request.form['description'],request.form['price'],product))
        print(cur)
    elif request.form["submit"] =="update" and file_name!= "": 
        cur=connection.execute("UPDATE Products SET Name=?, Description=?, Price=?, Image=? WHERE Name=?",
        (request.form['name'],request.form['description'],request.form['price'],file_name,product))
    elif request.form["submit"]=="delete":
        cur=connection.execute("DELETE FROM Products where NAME=?",(product, ))
        #if not, then update name, desc and price. 
    connection.commit()
    connection.close()
    return redirect("/")
app.run() ## infinite loop