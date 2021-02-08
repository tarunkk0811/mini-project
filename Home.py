import sqlite3
import re
import Register
import Training
import Recognition

conn = sqlite3.connect('users.db')
c = conn.cursor()
d = conn.cursor()
def login():
    email = input("Enter Your Email: ")
    password = input("Enter password: ")
    d.execute("select *from users where email=? and password=?",(email,password))
    c.execute("select *from users")
    rows = c.fetchall()#names
    userauth = d.fetchall()[0][2]

    for row in rows:
        names.append(row[2])
    names.insert(0, "None")

    user = Recognition.reconizeFace(names)
    if user == userauth:
        print("Welcome " + user + " !!!")
    else:
        print("Sorry! We are Unable to find Your Profile")




regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

names=[]
print("Welcome to Secure Authentication System")
print("1. Login \n2. Sign up\nEnter your choice")
while True:
    try:
        choice = int(input())
        if choice<1 or choice>2:
            raise Exception
        else:
            if choice == 2:
                name = input("Enter Your Name: ")
                email = ""
                while True:
                    email = input("Enter Your Email: ")
                    try:
                        if re.search(regex,email):
                            break
                        else:
                            raise Exception
                    except:
                        print("Invalid Email Please Try Again")
                password = input("Enter Password: ")
                query = "INSERT INTO users(Name,Email,Password) VALUES('"+name+"','"+email+"','"+password+"')"
                c.execute(query)
                conn.commit()
                print("Write success")
                Register.registerFace(c.lastrowid)
                print("Registration Success!!!")
                Training.Train()
                print("Successfully registered Your Face Thanks for registering!")
                login()
            else:
                login()

            break
    except:
        print("Sorry invalid input please try again")
        print("1. Login \n2. Sign up\nEnter your choice: ")