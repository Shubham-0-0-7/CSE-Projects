import csv
import os
import matplotlib.pyplot as plt

# Define the CSV filename and headers
filename = "report.csv"
headers = ["EmpID", "DeptID", "Name", "Salary"]

# Create the CSV file if it doesn't exist
if not os.path.isfile(filename):
    with open(filename, "w", newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(headers)

# Function to read and display the contents of the CSV file
def read():
    with open("report.csv", "r") as csvfile:
        file = csv.reader(csvfile)
        next(file)  # Skip the header row
        for row in file:
            print(row)

# Main function that acts as the interface for the system
def main():
    while True:
        print("""
        1. Add new record 
        2. Remove a record
        3. Update a record
        4. Display Employee data 
        5. Display reports
        6. Exit
        """)
        ch = int(input("Enter the task no.: "))  # Accept user choice
        if ch == 1:
            newrec()  # Add new employee record
        elif ch == 2:
            remrec()  # Remove an employee record
        elif ch == 3:
            updaterec()  # Update an employee record
        elif ch == 4:
            empdata()  # Display specific employee data
        elif ch == 5:
            disrep()  # Display reports (Salary or Name)
        elif ch == 6:
            break  # Exit the program
        else:
            print("Invalid Entry!!")
            print("Please Try again...")

    # After exiting the loop, plot a bar chart of employee salaries
    sal = []
    name = []

    with open("report.csv", "r") as csvfile:
        file = csv.reader(csvfile)
        next(file)  # Skip header row
        for row in file:
            if row:
                sal.append(float(row[3]))  # Append salary
                name.append(row[2])  # Append employee name

    # Create a bar chart for employee salary visualization
    plt.bar(name, sal, color='blue')
    plt.xlabel('Name')
    plt.ylabel('Salary')
    plt.title('Employee Management Chart')
    plt.show()

# Function to add a new record to the CSV file
def newrec():
    with open("report.csv", "a", newline='') as csvfile:
        file = csv.writer(csvfile)

        while True:
            empid = int(input("Enter employee ID: "))
            deptid = int(input("Enter department ID: "))
            name = input("Enter employee's name: ")
            salary = float(input("Enter employee's salary: "))  # Salary as a float

            data = [empid, deptid, name, salary]
            file.writerow(data)  # Write the data to the CSV file

            ch = input("Want to enter more records (Y/N)?: ")
            if ch.lower() != "y":  # Stop if user enters anything other than 'y'
                break

        print("Data written successfully!")

# Function to remove a record by Employee ID
def remrec():
    empidremove = int(input("Enter the Employee ID to remove: "))
    rows = []

    with open("report.csv", "r", newline='') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)  # Save the headers
        rows = list(reader)  # Save all the remaining rows

    new_rows = []  # List for rows after deletion
    found = False

    # Iterate through rows to find the employee to remove
    for row in rows:
        if row and int(row[0]) == empidremove:  # Match by Employee ID
            found = True
            print("Employee with ID removed:", empidremove)
        else:
            new_rows.append(row)

    if not found:
        print("No employee found with ID:", empidremove)

    # Write the updated rows back to the CSV file
    with open("report.csv", "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)  # Write the headers back
        writer.writerows(new_rows)  # Write the remaining rows

    read()  # Display the updated file

# Function to update an employee record
def updaterec():
    idtoupdate = int(input("Enter emp ID whose record is to be updated: "))
    updated_rows = []

    with open("report.csv", "r") as csvfile:
        file = csv.reader(csvfile)
        headers = next(file)  # Store the headers
        updated_rows.append(headers)

        found = False

        for row in file:
            if row and row[0] == str(idtoupdate):  # Match by Employee ID
                updated_row = list(row)
                updated_row[1] = int(input("Enter updated department ID: "))
                updated_row[2] = input("Enter updated name: ")
                updated_row[3] = input("Enter updated salary:")
                updated_rows.append(updated_row)  # Append the updated row
                found = True
            else:
                updated_rows.append(row)

    if not found:
        print("No employee found with ID", idtoupdate)
    else:
        with open("report.csv", "w", newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(updated_rows)  # Write all rows back to the file

    read()  # Display the updated file

# Function to display a specific employee's data by Employee ID
def empdata():
    with open("report.csv", "r") as csvfile:
        file = csv.reader(csvfile)
        id_to_find = int(input("Enter employee ID:"))
        found = False

        next(file)  # Skip the header row

        for row in file:
            if row and int(row[0]) == id_to_find:  # Match by Employee ID
                print("Employee found!")
                print(row)
                found = True
                break

        if not found:
            print("Employee not found!")

# Function to display reports (salary or name) based on Employee ID
def disrep():
    with open("report.csv", "r") as csvfile:
        file = csv.reader(csvfile)
        print("---- Report Menu ----")
        print("Enter 1 to display salary.")
        print("Enter 2 to display name.")
        ch = int(input("Enter your choice(1/2):"))

        if ch == 1:
            id = int(input("Enter employee ID:"))
            next(file)  # Skip the header row
            for row in file:
                if row and int(row[0]) == id:  # Match by Employee ID
                    print(row[3])  # Print salary
                    break
            else:
                print("No such employee!")

        elif ch == 2:
            id = int(input("Enter employee ID:"))
            csvfile.seek(0)  # Reset the file pointer to the beginning
            next(file)  # Skip the header row again
            for row in file:
                if row and int(row[0]) == id:  # Match by Employee ID
                    print(row[2])  # Print employee name
                    break
            else:
                print("No such employee!")

# Run the main function to start the employee management system
main()
