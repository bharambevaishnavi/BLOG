from flask import Flask, render_template
from flask import *
import sqlite3 


app = Flask(__name__)

@app.route("/")
def hello():
    return render_template ("index.html")

@app.route("/projects")
def projects():   
    return render_template ("projects.html")

@app.route("/activities")
def activities():
    return render_template ("activities.html")

@app.route("/blog", methods=['GET', 'POST'])
def blog():
    print(request.form)
    name1='dummy'
    mail1='dummyuser@gmail.com'
    message1="East and West, This Blog is the Best"
    if request.method == 'POST':
        name = request.form['cName']
        mail = request.form['cMail']
        message = request.form['cMessage']
        db=sqlite3.connect("contacts.db")
        db.execute('Insert into contact values (? ,?, ?)',(name,mail,message))
    return render_template ("blog.html")

@app.route("/category")
def category():
    return render_template ("category.html")

@app.route("/contact")
def contact():
    return render_template ("page-contact.html")



if __name__ == "__main__":
    app.run(debug=True)
