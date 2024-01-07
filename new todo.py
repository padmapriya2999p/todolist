
import sqlite3


conn=sqlite3.connect("details.db")
cur = conn.cursor()
#cur.execute("DROP TABLE task;")
cur.execute("CREATE TABLE IF NOT EXISTS task(task TEXT);")
cur.execute("INSERT INTO task VALUES('oi');")
#cur.execute("INSERT INTO task VALUES('"+task+"');")
conn.commit()
conn.close()
       