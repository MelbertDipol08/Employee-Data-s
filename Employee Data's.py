class Employee :
    def __init__(self,name,department,position,rate):
        self.name = name
        self.department = department
        self.position = position
        self.rate = rate

start = True

employees = []

while start :
    print("""
        ****************************
        [q] Add new Employee
        [w] Enter hourly of Employee
        [e] Show Employee Information
        [r] Exit
        ****************************
        """)

    choice = input("Enter your option ")

    if choice == "q" :
        Name = (input("Enter name: " + "\n"))
        Department = (input("Enter Department: " + "\n"))
        Position = (input("Enter a Positon: " + "\n"))
        rate = int(input("Enter a rate: " + "\n"))

        employees.append(Employee(Name, Department, Position, rate))
        print("Done!")

    elif choice == "w" :
        index = int(input("Index no. of Employee: "))
        print(employees[index].name, "is selected!")
        hourly = int(input("Hourly of Employee: "))
        print("Employee's Salary: ", employees[index].rate * hourly)

    elif choice == "e" :
        input("Melbert Dipol,IT,Programmer,50,000")
        for e in employees :
            print("*******************************")
            print(employees.index(e), "\n", "Name:", e.name, "\n", "Department:", e.department, "\n", "Position:",
                  e.position, "\n", "Rate:", e.rate, "\n")


    elif choice == "r" :

        start = False
        print("Exit")

    else :
        print("Invalid number, please try again")