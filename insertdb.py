import pymysql as connector
class DBHelper:
    def __init__(self):
        self.con = connector.connect(
            host="localhost",
            user="root",
            password="***************",
         database="pythontest"
        )
        query="create table if not exists user(userID int primary key,username varchar(200),phonr varchar(12))"
        cur = self.con.cursor()
        cur.execute(query)
        print("created")
    
    def insert_user(self, userid, username, phone):
        query="insert into user(userID,username,phonr) values({},'{}','{}')".format(userid, username, phone)
        print(query)
        cur = self.con.cursor() # cursor meanse to run the query of data base
        cur.execute(query)
        self.con.commit() #commit meanse physically change to data base and it  always run with con.
        print("user save to db")

helper = DBHelper()
# helper.insert_user(2315, "swayam verma", "7060870613")
helper.insert_user(6316, "sujal verma", "8171202988")
helper.insert_user(4217, "dharmendera verma", "9897077591")
helper.insert_user(9818, "archna verma", "7302227591")
