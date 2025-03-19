import pymysql as connector

con = connector.connect(
    host="localhost",
    user="root",
    password="vermaswayam@225346",
    database="pythontest"
)
print(con)