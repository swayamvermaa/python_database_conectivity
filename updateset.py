import pymysql as connector
class DBHelper:
    def __init__(self):
        self.con = connector.connect(
            host="localhost",
            user="root",
            password="****************",
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

    def fetch_all(self):
        query = "select * from user"
        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
            # print(row)
            # for formating we use tuple or dictionary
            print("userID:",row[0])
            print("username:",row[1])
            print("phonr:", row[2])

    def delete_user(self, userId):
        query="delete from user where userID= {}".format(userId)
        print(query)
        c = self.con.cursor()
        c.execute(query)
        self.con.commit() # if we dont commit then it does not change permanently in database
        print("deleted")

    def update_user(self,userId,newname,newphone):
        query = "UPDATE user set username='{}', phonr= '{}' WHERE userID= {}".format(newname,newphone,userId)
        print(query)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("updated")

helper = DBHelper()
# helper.insert_user(2315, "swayam verma", "7060870613")
# helper.insert_user(6316, "sujal verma", "8171202988")
# helper.insert_user(4217, "dharmendera verma", "9897077591")
# helper.insert_user(9818, "archna verma", "7302227591")
# helper.fetch_all()
# helper.delete_user(6316)
helper.update_user(9818,"abhideep","8522202")
helper.fetch_all()
