import time
import unittest
from app_second import *
from unittest.mock import patch,MagicMock
from io import StringIO

# def testCreateUser():
#     sam = Employee("1234", "Sam", "Staff",True)
#     sam.clock_in()
#     time.sleep(1)
#     sam.clock_out()

Klass = Employee("1235", "Klass", "Staff",True)

class TestMethods(unittest.TestCase):
        
    def test_clockInclockOutTime(self):
        
        Klass.clock_in()
        time.sleep(3)
        Klass.clock_out()
        print(Klass.viewUserDetails()[0])

        self.assertEqual((Klass.viewUserDetails()[0]),3) #Test for clock_in and clock_out to make sure time is accurate

    def test_get_role(self):
        self.assertEqual(Klass.get_role(),"Staff")
        self.assertNotEqual(Klass.get_role(),"Lecturer")
    
    def test_checkEmployee(self):
        self.assertTrue(base_manager.checkEmployee("1235"))

    def test_get_employee_name_by_id(self):
        self.assertEqual(base_manager.get_employee_name_by_id("1235"),"Klass")
    
    def test_get_employee_by_id(self):
        self.assertEqual(base_manager.get_employee_by_id("1235"),Klass)
    
    def test_viewUserDetails(self):
        self.assertEqual(Klass.viewUserDetails(),(3,10))

        
        
        
   
    


if __name__ == '__main__':
    unittest.main()

# testCreateUser()
# clockInclockOutTimeTest()

    
