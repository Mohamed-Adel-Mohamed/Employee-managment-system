class Employee:
    def __init__(self):
        self.employee_list = []

    def display_options(self):
        print("Program Options:")
        print("1) Add new employee")
        print("2) Print all employees")
        print("3) Delete employees by age range")
        print("4) Update employee salary by name")
        print("5) End the program")
        print("Enter your choice from (1 to 5)")

    def AddEmp(self,Ename,Eage,Esalary):
        self.employee_list.append({"Employee Name": Ename, "Age": Eage, "Salary": Esalary})
        print(f"Employee {Ename} added.")

    def PrinList(self):
        if self.employee_list:
            print("Employee List:")
            for employee in self.employee_list:
                print(employee)
        else:
            print("There are no employees.")

    def DeleteEmp(self, age_from, age_to):
        updated_list = []
        for employee in self.employee_list:
            if age_from <= employee['Age'] <= age_to:
                print(f"Employee {employee['Employee Name']} with age {employee['Age']} has been removed.")
            else:
                updated_list.append(employee)
        self.employee_list = updated_list

    def EmpNewSalary(self, Ename, new_salary):
        for employee in self.employee_list:
            if employee["Employee Name"] == Ename:
                employee["Salary"] = new_salary
                print(f"{Ename}'s salary has been updated to {new_salary}")
                break
        else:
            print(f"Employee {Ename} not found.")

    def run_program(self):
        while True:
            self.display_options()
            choice = input("Enter your choice: ")
            if choice == '1':
                Ename = input("Enter employee name: ")
                Eage = int(input("Enter employee age: "))
                Esalary = int(input("Enter employee salary: "))
                self.AddEmp(Ename, Eage, Esalary)
            elif choice == '2':
                self.PrinList()
            elif choice == '3':
                age_from = int(input("Enter age from: "))
                age_to = int(input("Enter age to: "))
                self.DeleteEmp(age_from, age_to)
            elif choice == '4':
                Ename = input("Enter employee name: ")
                new_salary = int(input("Enter new salary: "))
                self.EmpNewSalary(Ename, new_salary)
            elif choice == '5':
                print("Program ended.")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    emp = Employee()
    emp.run_program()
