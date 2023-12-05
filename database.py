
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



conn.commit()
def insertUser(employeeID,name,pay,hoursWorked=0):
    c.execute("INSERT INTO employees VALUES (?,?,?,?)", (employeeID, name, pay, hoursWorked))



def editUserPay(employeeID,newPay):
    c.execute("UPDATE employees  SET Pay = ? WHERE UserID =?",(newPay,employeeID))
    

def editUserHours(employeeID,newHours):
    c.execute("UPDATE employees  SET hoursWorked = ? WHERE UserID =?",(newHours,employeeID))
    
# c.execute("INSERT INTO employees VALUES (?,?,?,?)",(1234,"Sam",14,0))
# editUserPay(1234,15)
# editUserHours(1234,2.5)


# c.execute("SELECT * FROM employees")
# print(c.fetchall())