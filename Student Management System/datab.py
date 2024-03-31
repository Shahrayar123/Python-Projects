from sqlite3 import *

con = None
try:
	con = connect("datab.db")
	cursor = con.cursor()
	sql = "create table student(rno int primary key,name text,marks int)"
	cursor.execute(sql)
except Exception as e:
	print("Issue",e)
finally:
	if con is not None:
		con.close()
		print("Closed")