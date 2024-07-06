import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Hello@mscoder5",
    database="fir",
    # charset = 'utf8'
)

if mydb.is_connected():
    print("connected")
else:
    print("not connected")
