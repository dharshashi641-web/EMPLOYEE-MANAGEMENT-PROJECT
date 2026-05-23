import json
from models.employee import Employee


# Auto Employee ID Generator

def generate_employee_id(data):

    if not data:
        return "E001"

    last_employee = data[-1]

    last_id = last_employee.get("id", "")

    if not last_id.startswith("E"):
        return "E001"

    try:
        number = int(last_id[1:])
    except:
        number = 0

    new_number = number + 1

    return f"E{new_number:03d}"


# Add Employee
def add_employee():

    try:
        with open("data/employees.json", "r") as file:
            data = json.load(file)
    except:
        data = []

    emp_id = generate_employee_id(data)

    print(f"Generated Employee ID: {emp_id}")

    name = input("Enter Employee Name: ")
    if not name.strip():
        print("Name cannot be empty")
        return

    department = input("Enter Department: ")
    if not department.strip():
        print("Department cannot be empty")
        return

    try:
        salary = float(input("Enter Salary: "))
        if salary <= 0:
            print("Salary must be greater than 0")
            return
    except ValueError:
        print("Invalid Salary Input")
        return

    employee = Employee(emp_id, name, department, salary)

    employee_data = {
        "id": employee.emp_id,
        "name": employee.name,
        "department": employee.department,
        "salary": employee.salary
    }

    data.append(employee_data)

    with open("data/employees.json", "w") as file:
        json.dump(data, file, indent=4)

    print("Employee Added Successfully")


# View Employees

def view_employees():

    try:
        with open("data/employees.json", "r") as file:

            data = json.load(file)

            if not data:
                print("No Employees Found")
                return

            print("\nEMPLOYEE RECORDS\n")

            for employee in data:

                print(f"ID: {employee['id']}")
                print(f"Name: {employee['name']}")
                print(f"Department: {employee['department']}")
                print(f"Salary: {employee['salary']}")
                print("-" * 30)

    except FileNotFoundError:
        print("Employee File Not Found")

    except json.JSONDecodeError:
        print("JSON File is Empty or Corrupted")


# Search Employee

def search_employee():

    emp_id = input("Enter Employee ID to Search: ")

    try:
        with open("data/employees.json", "r") as file:

            data = json.load(file)

            for employee in data:

                if employee["id"] == emp_id:

                    print("\nEmployee Found")
                    print(f"ID: {employee['id']}")
                    print(f"Name: {employee['name']}")
                    print(f"Department: {employee['department']}")
                    print(f"Salary: {employee['salary']}")

                    return

            print("Employee Not Found")

    except FileNotFoundError:
        print("Employee File Not Found")

    except json.JSONDecodeError:
        print("JSON File Error")


# Update Salary

def update_salary():

    emp_id = input("Enter Employee ID: ")

    try:
        new_salary = float(input("Enter New Salary: "))

    except ValueError:
        print("Invalid Salary Input")
        return

    try:
        with open("data/employees.json", "r") as file:
            data = json.load(file)

        for employee in data:

            if employee["id"] == emp_id:

                employee["salary"] = new_salary

                with open("data/employees.json", "w") as file:
                    json.dump(data, file, indent=4)

                print("Salary Updated Successfully")
                return

        print("Employee Not Found")

    except FileNotFoundError:
        print("Employee File Not Found")

    except json.JSONDecodeError:
        print("JSON File Error")


# Delete Employee

def delete_employee():

    emp_id = input("Enter Employee ID to Delete: ")

    try:
        with open("data/employees.json", "r") as file:
            data = json.load(file)

        for employee in data:

            if employee["id"] == emp_id:

                data.remove(employee)

                with open("data/employees.json", "w") as file:
                    json.dump(data, file, indent=4)

                print("Employee Deleted Successfully")
                return

        print("Employee Not Found")

    except FileNotFoundError:
        print("Employee File Not Found")

    except json.JSONDecodeError:
        print("JSON File Error")


# Mark Attendance
def mark_attendance():

    emp_id = input("Enter Employee ID: ")
    status = input("Enter Attendance (Present/Absent): ")

    if status.lower() not in ["present", "absent"]:
        print("Invalid Attendance Status")
        return

    attendance_record = {
        "id": emp_id,
        "status": status
    }

    try:
        with open("data/attendance.json", "r") as file:
            data = json.load(file)
    except:
        data = []

    data.append(attendance_record)

    with open("data/attendance.json", "w") as file:
        json.dump(data, file, indent=4)

    print("Attendance Marked Successfully")


# View Attendance

def view_attendance():

    try:
        with open("data/attendance.json", "r") as file:

            data = json.load(file)

            if not data:
                print("No Attendance Records Found")
                return

            print("\nATTENDANCE RECORDS\n")

            for record in data:

                print(f"Employee ID: {record['id']}")
                print(f"Attendance: {record['status']}")
                print("-" * 30)

    except FileNotFoundError:
        print("Attendance File Not Found")

    except json.JSONDecodeError:
        print("JSON File Error")


# Filter By Department

def filter_by_department():

    department = input("Enter Department Name: ")

    try:
        with open("data/employees.json", "r") as file:

            data = json.load(file)

            found = False

            print(f"\n{department.upper()} DEPARTMENT EMPLOYEES\n")

            for employee in data:

                if employee["department"].lower() == department.lower():

                    print(f"ID: {employee['id']}")
                    print(f"Name: {employee['name']}")
                    print(f"Department: {employee['department']}")
                    print(f"Salary: {employee['salary']}")
                    print("-" * 30)

                    found = True

            if not found:
                print("No Employees Found In This Department")

    except FileNotFoundError:
        print("Employee File Not Found")

    except json.JSONDecodeError:
        print("JSON File Error")


# Generate Reports

def generate_reports():

    try:
        with open("data/employees.json", "r") as file:

            data = json.load(file)

            if not data:
                print("No Employee Data Found")
                return

            total_employees = len(data)

            salaries = [employee["salary"] for employee in data]

            highest_salary = max(salaries)
            lowest_salary = min(salaries)

            average_salary = sum(salaries) / total_employees

            departments = set()

            for employee in data:
                departments.add(employee["department"])

            total_departments = len(departments)

            print("\nEMPLOYEE REPORT\n")

            print(f"Total Employees: {total_employees}")
            print(f"Highest Salary: {highest_salary}")
            print(f"Lowest Salary: {lowest_salary}")
            print(f"Average Salary: {average_salary:.2f}")
            print(f"Total Departments: {total_departments}")

    except FileNotFoundError:
        print("Employee File Not Found")

    except json.JSONDecodeError:
        print("JSON File Error")