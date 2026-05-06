from tabulate import tabulate

class employeeManager():

    def __init__(self):
        self.employees={101: {'name': 'Satya', 'age': 27, 'department': 'HR', 'salary': 50000}}
        
    def employeeExist(self,emp_id):
        return emp_id in self.employees
    
    def postiveInteger(self,value):
        return isinstance(value, int) and value > 0
    
    def acceptValidNumber(self,prompt):
         value=input(prompt)
         while True:
              try:
                    value=int(value)
                    if self.postiveInteger(value):
                        return value
              except ValueError:
                   value=input("Invalid input. "+prompt)

                   
    def acceptValidAge(self):
        age=self.acceptValidNumber("Enter age (between 1 and 120) : ")
        while  0>age>120:
            age=self.acceptValidNumber("Invalid age. Enter age (between 1 and 120) : ")
            print(age)

        return age
           
    def add_employee(self,emp_id,name,age,department,salary):
        if not self.employeeExist(emp_id):
            self.employees[emp_id]={"name":name,
                                    "age":age,
                                    "department":department,
                                    "salary":salary}
            print(f"Employee {name} with id {emp_id} added successfully")
        else :
            print("Employee already exists")
        
    def view_employees(self):
        if self.employees:
            table=[[emp_id]+list(info.values()) for emp_id,info in self.employees.items()]
            print(tabulate(table, headers=["ID", "Name", "Age", "Department", "Salary"], tablefmt="grid"))
        else:
            print("No employees available")

    def search_employees(self,emp_id):
        if self.employeeExist(emp_id):
            table=[[emp_id]+list(self.employees[emp_id].values())]
            print(tabulate(table, headers=["ID", "Name", "Age", "Department", "Salary"], tablefmt="grid"))
        else:
            print("No Employee Found")

    def remove_employee(self,emp_id):
        if self.employeeExist(emp_id):
            del self.employees[emp_id]
            print(f"Employee with id {emp_id} removed successfully")
        else:
            print("No Employee Found")
    
    def update_employee(self,emp_id,name=None,age=None,department=None,salary=None):
        if self.employeeExist(emp_id):
            if name:
                self.employees[emp_id]['name']=name
            if age:
                self.employees[emp_id]['age']=age
            if department:
                self.employees[emp_id]['department']=department
            if salary:
                self.employees[emp_id]['salary']=salary
            print(f"\nEmployee with id {emp_id} updated successfully")
        else:
            print("No Employee Found")

    def add_Handler(self):

        emp_id=self.acceptValidNumber("Enter employee id : ")

        while self.employeeExist(emp_id):
                    emp_id=self.acceptValidNumber("Employee_id alreay Exist.Enter new id : ")
                    
        name=input("Enter name : ")
        age=self.acceptValidAge()
        dept=input("Enter department : ")
        salary=self.acceptValidNumber("Enter salary : ")

        while not self.postiveInteger(salary):
                    salary=self.acceptValidNumber("Enter positive integer for salary : ")

        self.add_employee(emp_id,name,age,dept,salary)  
    
    def view_Handler(self):
        self.view_employees()
        
    def remove_Handler(self):
        emp_id=self.acceptValidNumber("Enter employee id : ")
        self.remove_employee(emp_id)
         
    def search_Handler(self):
        emp_id=self.acceptValidNumber("Enter employee id : ")
        self.search_employees(emp_id)

    def update_Handler(self):
        emp_id=self.acceptValidNumber("Enter employee id : ")
        if self.employeeExist(emp_id):
            self.search_employees(emp_id)
            while True:
                            name=input("Enter new name (leave blank to keep current) : ")
                            age_input=input("Enter new age (leave blank to keep current) : ")
                            dept=input("Enter new department (leave blank to keep current) : ")
                            salary_input=input("Enter new salary (leave blank to keep current) : ")
                            try:
                                age=int(age_input) if age_input else None
                                salary=int(salary_input) if salary_input else None
                                break
                            except ValueError:
                                print("Invalid inputs. Please enter valid values.")

            self.update_employee(emp_id,name,age,dept,salary)
                        
        else:
                    print("No Employee Found")

    def main_menu(self):
        print("-"*40)
        print("-"*40)
        option = input("1. Add Employee\n" \
        "2. View All Employees\n" \
        "3. Search for Employees\n" \
        "4. Remove Employee\n" \
        "5. Update Employee\n" \
        "6. Exit \n---------------------\n---------------------\n")
        try:
            option=int(option)
        except ValueError:
            print("Invalid input. Please enter a valid option.")
        return option
 
    def main(self):

        while True:

            option=self.main_menu()
            options={
                1:self.add_Handler,
                2:self.view_Handler,
                3:self.search_Handler,
                4:self.remove_Handler,
                5:self.update_Handler
            }

            if option in options:
                options[option]()
            
            elif option == 6:
                print("Exiting Employee Management System. Thank You!")
                break
            else:
                print("Invalid Option")
    
if __name__ =="__main__":
    HR=employeeManager()
    HR.main()

