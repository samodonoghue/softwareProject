import sys
from datetime import datetime
import time
class Employee:

    _registry = []
    def __init__(self,id,name, role):
        self.name = name
        self._id = id
        self._registry.append(self)
        self.role = role
        return
    

    def clock_in(self):
        self.now = datetime.now()
        current_time = self.now.strftime("%H:%M:%S")
        print(" clock in time:  " + current_time)
        self.clock_in_time =current_time
        return
    
    def clock_out(self):
        self.now = datetime.now()
        current_time = self.now.strftime("%H:%M:%S")
        self.clock_out_time = current_time
        return
    
    def get_role(self):
        return self.role

    def get_clock_in_time(self):
        return self.clock_in_time

    def get_clock_out_time(self):
        return self.clock_out_time
    
sam = Employee("06819" ,"Sam","Staff")

sam.clock_in()
# time.sleep(10)
sam.clock_out()

for employees in Employee._registry:
    print(employees.name)


print(sam.get_role())
print(sam.get_clock_in_time())
print(sam.get_clock_out_time())


class Manager():
    def __init__(self, name):
        self.name = name
        self.employees = Employee._registry

    def view_all_employees(self):
        for employee in Employee._registry:
            print("-"*10)
            print("Name: ",employee.name,"\nID:", employee._id,"\nClock in Time: ", employee.get_clock_in_time())
            print("-"*10)
    def get_employee_name_by_id(self, emp_id):
        emp = self.employees.get(emp_id)
        if emp:
            return emp.emp_name
        else:
            return f"Employee with ID {emp_id} not found."

base_manager = Manager("BaseManager")
bryan = Manager("Bryan")

bryan.view_all_employees()


def login():
    input_id = input("What is your Employee ID:")
    print("Employee name - ",base_manager.get_employee_name_by_id(input_id))

login()



