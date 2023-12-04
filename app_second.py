from datetime import datetime

class Employee:
    _registry = []

    def __init__(self, emp_id, name, role):
        self.name = name
        self._id = emp_id
        self.role = role
        self.clock_in_time = None
        self.clock_out_time = None
        self._registry.append(self)

    def clock_in(self):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("Thanks",self.name, "\nClock in Time:", current_time)
        self.clock_in_time = current_time

    def clock_out(self):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("Thanks", self.name, "\nClock Out Time: ", current_time)
        self.clock_out_time = current_time

    def get_role(self):
        return self.role

    def get_clock_in_time(self):
        return self.clock_in_time

    def get_clock_out_time(self):
        return self.clock_out_time

class Manager(Employee):
    def __init__(self, emp_id, name):
        self.name = name
        self.employees = Employee._registry
        self._id = emp_id
        self.role="Manager"
        self.clock_in_time = None
        self.clock_out_time = None
        self._registry.append(self)

    def view_all_employees(self):
        for employee in self.employees:
            print("-" * 10)
            print("Name:", employee.name, "\nID:", employee._id,
                  "\nClock in Time:", employee.get_clock_in_time(),
                  "\nClock out Time:", employee.get_clock_out_time())
            print("-" * 10)

    def get_employee_name_by_id(self, emp_id):
        for employee in self.employees:
            if employee._id == emp_id:
                return employee.name
        return f"Employee with ID {emp_id} not found."
    def checkManager():

        return None
        
    def get_employee_by_id(self, emp_id):
        for employee in self.employees:
            if employee._id == emp_id:
                return employee
        return None

base_manager = Manager("0000","BaseManager")
bryan = Manager("4321","Bryan")


sam = Employee("1234", "Sam", "Staff")
# sam.clock_in()
# sam.clock_out()

bryan.view_all_employees()

def login():
    input_id = input("What is your Employee ID:")
    employee = base_manager.get_employee_by_id(input_id)
    


    if employee:
        if employee.role == "Manager":

            print("Welcome manager "+employee.name)

        else:
            clock_in_input = input("1 - Clock in\n2 - Clock out\n")

            if clock_in_input == "1":
                employee.clock_in()
            elif clock_in_input == "2":
                employee.clock_out()
            else:
                print("NOT AN OPTION")
    
        
    else:
        print(f"Employee with ID {input_id} not found.")


login()
