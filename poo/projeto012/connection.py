import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="mypass",
  database="nation"
)
#print(mydb)
