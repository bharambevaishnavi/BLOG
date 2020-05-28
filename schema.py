import sqlite3  
  
con = sqlite3.connect("contacts.db")  
db=con.cursor()

#contact Data table to hold name , mail , message
db.execute("create table contact1 (name TEXT PRIMARY KEY NOT NULL, mail text NOT NULL,message text NOT NULL)")


con.close()  
