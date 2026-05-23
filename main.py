from services.employee_service import (
    add_employee,
    view_employees,
    search_employee,
    update_salary,
    delete_employee,
    mark_attendance,
    view_attendance,
    filter_by_department,
    generate_reports
)

from services.auth_service import register, login


# ---------------------------
# AUTHENTICATION SYSTEM
# ---------------------------

while True:

    print("\nWELCOME")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    auth_choice = input("Enter Choice: ")

    if auth_choice == "1":
        register()

    elif auth_choice == "2":

        if login():
            break   # move to employee system after login

    elif auth_choice == "3":
        print("Exiting Program")
        exit()

    else:
        print("Invalid Choice")


# ---------------------------
# EMPLOYEE MANAGEMENT SYSTEM
# ---------------------------

while True:

    print("\nEMPLOYEE MANAGEMENT SYSTEM")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Update Salary")
    print("5. Delete Employee")
    print("6. Mark Attendance")
    print("7. View Attendance")
    print("8. Filter By Department")
    print("9. Generate Reports")
    print("10. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_employee()

    elif choice == "2":
        view_employees()

    elif choice == "3":
        search_employee()

    elif choice == "4":
        update_salary()

    elif choice == "5":
        delete_employee()

    elif choice == "6":
        mark_attendance()

    elif choice == "7":
        view_attendance()

    elif choice == "8":
        filter_by_department()

    elif choice == "9":
        generate_reports()

    elif choice == "10":
        print("Exiting Program")
        break

    else:
        print("Invalid Choice")