#!C:/Python/Python37/python.exe
import cgi
import mysql.connector
print("Content-type:text/html\r\n\r\n")
print("<h1>CGI ISERTION</h1>")
data=cgi.FieldStorage()
name=data.getvalue('email')
password=data.getvalue('pass')
print(name)
print(password)

#connection with database
myconn=mysql.connector.connect(host="localhost",user ="root", passwd='1234',database="cgidatabase")
cur=myconn.cursor()

try:
    #sql query to execute
    cur.execute("insert into email values(%s,%s)",(name,password))
    myconn.commit()
    print("record inserted")
except:
        myconn.rollback()
myconn.close()
