import mysql.connector

# Database connection
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Nad@9168",
    database="employee"
)

cursor = con.cursor()

# Function to check if an employee exists
def check_employee(Id):
    sql = "SELECT ID FROM employee WHERE ID = %s"
    cursor.execute(sql, (Id,))
    return cursor.fetchone() is not None

# Function to add an employee
def add_employee():
    Id = input("Enter Employee Id: ")
    if check_employee(Id):
        print("Employee already exists. Please try again.")
        return

    name = input("Enter Employee Name: ")
    Post = input("Enter Employee Post: ")
    salary = input("Enter Employee Salary: ")

    sql = 'INSERT INTO employee (ID, name, Post, salary) VALUES (%s, %s, %s, %s)'
    data = (Id, name, Post, salary)
    try:
        cursor.execute(sql, data)
        con.commit()
        print("Employee Added Successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        con.rollback()

# Function to remove an employee
def remove_employee():
    Id = input("Enter Employee Id: ")
    if not check_employee(Id):
        print("Employee does not exist. Please try again.")
        return

    sql = 'DELETE FROM employee WHERE ID = %s'
    try:
        cursor.execute(sql, (Id,))
        con.commit()
        print("Employee Removed Successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        con.rollback()

# Function to promote an employee
def promote_employee():
    Id = input("Enter Employee Id: ")
    if not check_employee(Id):
        print("Employee does not exist. Please try again.")
        return

    try:
        Amount = float(input("Enter increase in Salary: "))

        # Fetch current salary
        sql_select = 'SELECT salary FROM employee WHERE ID = %s'
        cursor.execute(sql_select, (Id,))
        current_salary = cursor.fetchone()[0]

        # Update salary
        new_salary = current_salary + Amount
        sql_update = 'UPDATE employee SET salary = %s WHERE ID = %s'
        cursor.execute(sql_update, (new_salary, Id))
        con.commit()
        print("Employee Promoted Successfully")
    except (ValueError, mysql.connector.Error) as e:
        print(f"Error: {e}")
        con.rollback()

# Function to display all employees
def display_employees():
    try:
        sql = 'SELECT * FROM employee'
        cursor.execute(sql)
        employees = cursor.fetchall()
        for employee in employees:
            print("Employee Id:", employee[0])
            print("Employee Name:", employee[1])
            print("Employee Post:", employee[2])
            print("Employee Salary:", employee[3])
            print("-----------------------------------------------------")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

# Function to display the menu
def menu():
    while True:
        print("\nWelcome to Employee Management Record")
        print("Press:")
        print("1 to Add Employee")
        print("2 to Remove Employee")
        print("3 to Promote Employee")
        print("4 to Display Employees")
        print("5 to Exit")

        ch = input("Enter your Choice: ")
        if ch == '1':
            add_employee()
        elif ch == '2':
            remove_employee()
        elif ch == '3':
            promote_employee()
        elif ch == '4':
            display_employees()
        elif ch == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid Choice! Please try again.")

if __name__ == "__main__":
    menu()
