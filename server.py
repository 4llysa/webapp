from flask import Flask 
from flask import render_template 
from flask import request 

app=Flask(__name__)

@app.route("/")
def root():
    return render_template("form1.html")
    
app.run()
