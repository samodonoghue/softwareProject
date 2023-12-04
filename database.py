
import sqlite3

conn = sqlite3.connect('employee.db')

c = conn.cursor()
c.execute("""DROP TABLE IF EXISTS employees """)
c.execute("""CREATE TABLE employees (
    first text,
    last text,
    pay integer

)""")


c.execute("INSERT INTO employees VALUES (?,?,?)", ("Sam", "ODonoghue", 14))
conn.commit()

c.execute("SELECT * FROM employees")
print(c.fetchall())