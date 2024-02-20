from pymysql import Connection

con = Connection(
    host="localhost",
    port=3306,
    user="root",
    password="admin123",
    database="my_db_01"
)

cursor = con.cursor()