import sqlite3

conn = sqlite3.connect('1222_DB.sl3', 5)
cur = conn.cursor()
# CREATE
#cur.execute("CREATE TABLE student(id INT, name TEXT, age INT);")

# INSERT
# cur.execute("INSERT INTO student(id, name, age) VALUES (1,'Jack', 25)")
# cur.execute("INSERT INTO student(id, name, age) VALUES (2,'Bob', 15)")
# cur.execute("INSERT INTO student(id, name, age) VALUES (3,'Kevin', 12)")


# SELECT
cur.execute('SELECT * FROM student')
conn.commit()

res = cur.fetchall()
print(res)

conn.close()

# ALTER
# DROP




