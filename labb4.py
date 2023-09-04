#python code
class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"{self.emp_id} {self.name} {self.age} {self.salary}"


def sort_employee_data(employees, sort_key):
    if sort_key == 1:
        return sorted(employees, key=lambda emp: emp.age)
    elif sort_key == 2:
        return sorted(employees, key=lambda emp: emp.name)
    elif sort_key == 3:
        return sorted(employees, key=lambda emp: emp.salary)
    else:
        return employees


def main():
    employees = [
        Employee("161E90", "Raman", 41, 56000),
        Employee("161F91", "Himadri", 38, 67500),
        Employee("161F99", "Jaya", 51, 82100),
        Employee("171E20", "Tejas", 30, 55000),
        Employee("171G30", "Ajay", 45, 44000)
    ]

    print("Employee Table:")
    print("Employee ID Name Age Salary (PM)")
    for emp in employees:
        print(emp)

    while True:
        print("\nSort Options:")
        print("1. Sort by Age")
        print("2. Sort by Name")
        print("3. Sort by Salary")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 4:
            break

        employees = sort_employee_data(employees, choice)

        print("\nSorted Employee Table:")
        print("Employee ID Name Age Salary (PM)")
        for emp in employees:
            print(emp)


if __name__ == "__main__":
    main()
