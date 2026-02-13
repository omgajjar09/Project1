
class employee:
    def __init__(self,name,age,employee_id,salary):
        self.name=name
        self.age=age
        self.employee_id=employee_id
        self.salary=salary

    def getter(self):
        print(f"Employee Create with Name : {self.name}, Age :{self.age}, Employee Id :{self.employee_id} and Salary : ${self.salary}\n")
    
    def display(self):
        print("\nEmployee Details:")
        print(f"Name :{self.name}")
        print(f"Age :{self.age}")
        print(f"Employee Id :{self.employee_id}")
        print(f"Salary : ${self.salary}\n")

    def __del__(self):
        pass

class manager(employee):
    def __init__(self, name, age, employee_id, salary,department):
        super().__init__(name, age, employee_id, salary)
        self.department=department

    def getter(self):
        print(f"Manager Create with Name : {self.name}, Age :{self.age}, Employee Id :{self.employee_id}, Salary : ${self.salary} and department :{self.department}\n")
    
    def display(self):
        print("\nManager Details:")
        print(f"Name :{self.name}")
        print(f"Age :{self.age}")
        print(f"Employee Id :{self.employee_id}")
        print(f"Salary : ${self.salary}")
        print(f"Department :{self.department}\n")

    def __del__(self):
        pass

class developer(employee):
    def __init__(self, name, age, employee_id, salary,programming_language):
        super().__init__(name, age, employee_id, salary)
        self.programming_language=programming_language

    def getter(self):
        print(f"Developer Create with Name : {self.name}, Age :{self.age}, Employee Id :{self.employee_id} Salary : ${self.salary} and Programming language :{self.programming_language}\n")

    def display(self):
        print("\nDeveloper Details:")
        print(f"Name :{self.name}")
        print(f"Age :{self.age}")
        print(f"Employee Id :{self.employee_id}")
        print(f"Salary : ${self.salary}")
        print(f"Programming Language :{self.programming_language}\n")

    def __del__(self):
        pass

eobj=None
mobj=None
dobj=None

print("--- Python oop Project : Employee Management System ----\n")
first_time = True
while True:
    if not first_time:
        print("\n--- Choose another operation ---\n")
    first_time = False
    print("choose an operation:")
    print("1. Create an Employee")
    print("2. Creaet a Manager")
    print("3. Creaet a Developer")
    print("4. Show Details")
    print("5. Exit\n")

    choice=int(input("Enter youer choice:"))

    if choice==1:
        name=input("Enter Name :")
        age=int(input("Enter Age:"))
        emp_id=input("Enter Id (First Later for ID is E):")
        salary=int(input("Enter Salary :"))

        eobj=employee(name,age,emp_id, salary)
        eobj.getter()

    elif choice==2:
        name=input("Enter Name :")
        age=int(input("Enter Age :"))
        emp_id=input("Enter Id (First Later for ID is M) :")
        department=input("Enetr Department Name :")
        salary=int(input("Enter Salary :"))

        mobj=manager(name,age,emp_id,salary,department)
        mobj.getter()

    elif choice==3:
        name=input("Enter Name :")
        age=int(input("Enter Age :"))
        emp_id=input("Enter Id (First Later for ID is D) :")
        pro_lan=input("Enetr Programming Language Name :")
        salary=int(input("Enter Salary :"))

        dobj=developer(name,age,emp_id,salary,pro_lan)
        dobj.getter()

    elif choice==4:
        print("\nChoose details to show:")
        print("1. Employee")
        print("2. Manageer")
        print("3. Developer")

        vchoice=int(input("Enter your choice:"))

        if vchoice==1:
            eobj.display()

        elif vchoice==2:
            mobj.display()

        elif vchoice==3:
            dobj.display()

        else:
            print("\nInvalided Choice\n")

    elif choice==5:
        print("\n Exiting the system. All resources have been freed.\n")
        break

    else:
        print("\nInvalided Choice\n")