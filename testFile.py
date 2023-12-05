import time
from app_second import *

def testCreateUser():
    sam = Employee("1234", "Sam", "Staff",True)
    sam.clock_in()
    time.sleep(1)
    sam.clock_out()

def testCreateUser2():
    Klass = Employee("1235", "Klass", "Staff",True)
    Klass.clock_in()
    time.sleep(1)
    Klass.clock_out()




testCreateUser()
testCreateUser2()
    