import sqlite3

def connectDB(filename):
    return sqlite3.connect(filename)

conn = connectDB("librarycubed/blockchain.db")

c = conn.cursor()
try:
    c.execute("""CREATE TABLE blockchain(
    chain text
    )""")
except sqlite3.OperationalError:
    pass

c.execute("INSERT INTO blockchain VALUES ('this is chain')")
c.execute("SELECT * FROM blockchain")
print(c.fetchall())
conn.commit()
conn.close()
