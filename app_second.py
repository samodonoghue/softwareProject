from datetime import datetime
from database import *


class Employee:
    _registry = []

    def __init__(self, emp_id, name, role,manual=False,pay=10):
        self.name = name
        self._id = emp_id
        self.role = role
        self.clocked_in = False
        self.clock_in_time = None
        self.clocktime = None 
        # additional clocktime and clockedtime not necessary
        self.clock_out_time = None
        self.clockedtime = None
        self._registry.append(self)
        
        if manual:
            c.execute("SELECT HoursWorked FROM employees WHERE UserID=?",(emp_id,))
            employeeID_check = currentHours=c.fetchone()
            if employeeID_check:
                print("-"*10)
                print("EMPLOYEE ID IS TAKEN")
                print("-"*10)
            else:
                c.execute("INSERT INTO employees VALUES (?,?,?,?)",(self._id,self.name,pay,0))

    def clock_in(self):
        if self.clocked_in == False:
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print("Thanks",self.name, "\nClock in Time:", current_time)
            self.clock_in_time = current_time
            self.clocktime=now.timestamp()
            self.clocked_in = True

        else:
            print("You're already Clocked in")

    def clock_out(self):
        if self.clocked_in == True:
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print("Thanks", self.name, "\nClock Out Time: ", current_time)
            self.clock_out_time = current_time
            self.clockedtime = now.timestamp()
            self.clocked_in = False
            c.execute("SELECT HoursWorked FROM employees WHERE UserID=?",(self._id,))
            currentHours=float(c.fetchone()[0])

            addedHours=((float(self.clockedtime)-(self.clocktime)))/60            
            newHours = currentHours+addedHours
           
            editUserHours(self._id,(newHours))
            
        else:
            print("You were not Clocked in")

    def get_role(self):
        return self.role

    def get_clock_in_time(self):
        return self.clock_in_time

    def get_clock_out_time(self):
        return self.clock_out_time
    
    def viewUserDetails(self):
        c.execute("SELECT HoursWorked FROM employees WHERE UserID=?",(self._id,))
        currentHours=c.fetchone()[0]
    
        c.execute("SELECT Pay FROM employees WHERE UserID=?",(self._id,))
        pay=c.fetchone()[0]

        return currentHours,pay

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

    def checkEmployee(self,emp_id):
        employee = base_manager.get_employee_by_id(emp_id)
        if employee:
            return True
        else:
                print("-"*10)
                print("Employee not found - Please try again")
                print("-"*10)


    def get_employee_name_by_id(self, emp_id):
        for employee in self.employees:
            if employee._id == emp_id:
                return employee.name
        return f"Employee with ID {emp_id} not found."
         
    def get_employee_by_id(self, emp_id):
        for employee in self.employees:
            if employee._id == emp_id:
                return employee
        return None
    
    def editPay(self):
        try:
            print("Edit User Pay Selected")
            employeeID=input("Input EmployeeID:")
            
            if base_manager.checkEmployee(employeeID):
                newPay=input("Input new pay:")
                editUserPay(int(employeeID),float(newPay))
            
        except ValueError:
            print("-"*10)
            print("there was an error - Please try again")
            print("-"*10)
    
    
    def editHours(self):
        print("Edit User Hours Selected")
        employeeID=input("Input EmployeeID:")
        try:
            if base_manager.checkEmployee(employeeID):
                newHours=input("Input added hours:")
                c.execute("SELECT HoursWorked FROM employees WHERE UserID=?",(employeeID,))
                
                currentHours=c.fetchone()[0]
                
                newHours=float(newHours)+float(currentHours)
                editUserHours(employeeID,float(newHours))
        except ValueError:
            print("-"*10)
            print("there was an error - Please try again")
            print("-"*10)

        
        
    def insertNewUser(self):
        print("Insert new user selected")
        employeeID=input("input new employee ID:")
        c.execute("SELECT HoursWorked FROM employees WHERE UserID=?",(employeeID,))
        employeeID_check = currentHours=c.fetchone()

        if employeeID_check:
            print("-"*10)
            print("EMPLOYEE ID IS TAKEN")
            print("-"*10)
        else:
            name=input("input employee name:")
            pay=input("Input employees pay:")
            globals()[name] = Employee(employeeID,name,"Staff")
            c.execute("INSERT INTO employees VALUES (?,?,?,?)",(employeeID,name,pay,0))

    


base_manager = Manager("0000","BaseManager")
bryan = Manager("4321","Bryan")


sam = Employee("1234", "Sam", "Staff")
sam.clock_in()
sam.clock_out()

bryan.view_all_employees()

def login():
    input_id = input("What is your Employee ID:")
    employee = base_manager.get_employee_by_id(input_id)
    


    if employee:
        if employee.role == "Manager":
            print("-" * 10)
            print("Welcome manager "+employee.name)
            print("-" * 10)
            manager_input = input("1-Edit User Pay\n2-Edit User Hours\n3-Insert New User\n4-View employee details\nOr press X to exit\n")
            print("-" * 10)
            if manager_input =="1":
                employee.editPay()
                c.execute("SELECT * FROM employees")
                print(c.fetchall())
            elif manager_input=="2":
                employee.editHours()
                c.execute("SELECT * FROM employees")
                print(c.fetchall())
            elif manager_input=="3":
                employee.insertNewUser()
                c.execute("SELECT * FROM employees")
                print(c.fetchall())
            elif manager_input=="4":
                employee.view_all_employees()
            elif manager_input=="X":
                login()

            else:
                print("NOT AN OPTION")
            

        else:
            print("-" * 10)
            print("Welcome "+employee.name)
            print("-" * 10)
            employee_input = input("1 - Clock in or out\n2 - View pay and hours\n")
            if employee_input == "1":
                clock_in_input = input("1 - Clock in\n2 - Clock out\n")

                if clock_in_input == "1":
                    employee.clock_in()
                elif clock_in_input == "2":
                    employee.clock_out()
                else:
                    print("NOT AN OPTION")
            elif employee_input == "2":
                currentHours,pay=employee.viewUserDetails()
                earned=pay*currentHours
                print(employee.name+"\nHours worked:"+str(currentHours)+"\nPay:"+str(pay)+"\nEarned:"+str(earned))
                
            else:
                print("NOT AN OPTION")
    
    
        
    else:
        print(f"Employee with ID {input_id} not found.")
    Exit=input("Press X to exit or any key to continue:").capitalize()
    if (Exit=="X"):
        exit()

    login()

if __name__ == '__main__':

    login()
