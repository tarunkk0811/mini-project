import sqlite3
conn = sqlite3.connect('users.db')
c = conn.cursor()
c.execute("Create table users(id integer AUTO INCREMENT,name text,email text primary key,password text)")
#c.execute("drop table users")
#c.execute("select *from users")
conn.commit()
print("Success")