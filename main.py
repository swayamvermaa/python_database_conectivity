import pymysql as connector

con = connector.connect(
    host="localhost",
    user="root",
    password="************",
    database="pythontest"
)
print(con)
