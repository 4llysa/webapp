print("hello")
from flask import Flask #flask is a library that contains the class Flask
from flask import render_template  #this is a function
from flask import request ##request is an object (object≠class, object has already been created by another class)
from flask import redirect ##redirect function (302)
app=Flask(__name__) #anything that has 2 underscores have already been predefined

@app.route("/")
def root(): 
    f=open("products.txt","r")
    products_list=[line.strip().split(",") for line in f]
    return render_template("products1.html",products=products_list)
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
    f=open("products.txt","a")
    f.write(f"{request.form['product']},{request.form['description']},{request.form['price']},{file_name} \n") 
    f.close()
    return redirect("/")
    #f"{request.form['product']}+{request.form['description']}+{request.form['price']}"
    #request.form creates a python dictionary object 
app.run() ## infinite loop