import sqlite3 as sql

conn = sql.connect("cases_db.db")

conn.execute("CREATE TABLE cases (item_id TEXT, name TEXT, type TEXT, color TEXT, price TEXT)")

conn.close()

print("Table created successfully")