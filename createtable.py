import pymysql as connector
class DBHelper:
    def __init__(self):
        self.con = connector.connect(
            host="localhost",
            user="root",
            password="************",
         database="pythontest"
        )
        query="create table if not exists user(userID int primary key,username varchar(200),phonr varchar(12))"
        cur = self.con.cursor()
        cur.execute(query)
        print("created")

helper = DBHelper()
