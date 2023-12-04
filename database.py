
import sqlite3

conn = sqlite3.connect('employee.db')

c = conn.cursor()
c.execute("""DROP TABLE IF EXISTS employees """)
c.execute("""          
    CREATE TABLE employees (
    UserID INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    Pay REAL NOT NULL,
    HoursWorked REAL 


)""")


c.execute("INSERT INTO employees VALUES (?,?,?,?)", (1234, "Sam", 14, 0))
conn.commit()

c.execute("SELECT * FROM employees")
print(c.fetchall())