import csv
import os
import matplotlib.pyplot as plt

filename = "report.csv"
headers = ["EmpID", "DeptID", "Name", "Salary"]

if not os.path.isfile(filename):
    with open(filename, "w", newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(headers)

def read():
    with open("report.csv", "r") as csvfile:
        file = csv.reader(csvfile)
        next(file)
        for row in file:
            print(row)

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
        ch = int(input("Enter the task no.: "))
        if ch == 1:
            newrec()
        elif ch == 2:
            remrec()
        elif ch == 3:
            updaterec()
        elif ch == 4:
            empdata()
        elif ch == 5:
            disrep()
        elif ch == 6:
            break
        else:
            print("Invalid Entry!!")
            print("Please Try again...")
    sal = []
    name = []

    with open("report.csv", "r") as csvfile:
        file = csv.reader(csvfile)
        next(file) 
        for row in file:
            if row:
                sal.append(float(row[3]))  
                name.append(row[2])  

    plt.bar(name, sal, color='blue')
    plt.xlabel('Name')
    plt.ylabel('Salary')
    plt.title('Employee Management Chart')
    plt.show()

def newrec():
    with open("report.csv", "a", newline='') as csvfile:
        file = csv.writer(csvfile)

        while True:
            empid = int(input("Enter employee ID: "))
            deptid = int(input("Enter department ID: "))
            name = input("Enter employee's name:")
            salary = float(input("Enter employee's salary:"))  

            data = [empid, deptid, name, salary]
            file.writerow(data)

            ch = input("Want to enter more records (Y/N)?: ")
            if ch.lower() != "y":
                break

        print("Data written successfully!")

def remrec():
    empidremove = int(input("Enter the Employee ID to remove: "))
    rows = []

    with open("report.csv", "r", newline='') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)
        rows = list(reader)

    new_rows = []  
    found = False

    for row in rows:
        if row and int(row[0]) == empidremove:
            found = True
            print("Employee with ID removed:", empidremove)
        else:
            new_rows.append(row)

    if not found:
        print("No employee found with ID:", empidremove)
        
    with open("report.csv", "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        writer.writerows(new_rows)

    read()

def updaterec():
    idtoupdate = int(input("Enter emp ID whose record is to be updated: "))
    updated_rows = []

    with open("report.csv", "r") as csvfile:
        file = csv.reader(csvfile)
        headers = next(file)
        updated_rows.append(headers)

        found = False

        for row in file:
            if row and row[0] == str(idtoupdate):
                updated_row = list(row)
                updated_row[1] = int(input("Enter updated department ID: "))
                updated_row[2] = input("Enter updated name: ")
                updated_row[3] = input("Enter updated salary:")
                updated_rows.append(updated_row)
                found = True
            else:
                updated_rows.append(row)

    if not found:
        print("No employee found with ID", idtoupdate)
    else:
        with open("report.csv", "w", newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(updated_rows)

    read()


def empdata():
    with open("report.csv", "r") as csvfile:
        file = csv.reader(csvfile)
        id_to_find = int(input("Enter employee ID:"))
        found = False
        
        next(file)

        for row in file:
            if row and int(row[0]) == id_to_find:
                print("Employee found!")
                print(row)
                found = True
                break

        if not found:
            print("Employee not found!")

def disrep():
    with open("report.csv", "r") as csvfile:
        file = csv.reader(csvfile)
        print("---- Report Menu ----")
        print("Enter 1 to display salary.")
        print("Enter 2 to display name.")
        ch = int(input("Enter your choice(1/2):"))

        if ch == 1:
            id = int(input("Enter employee ID:"))
            next(file)
            for row in file:
                if row and int(row[0]) == id:
                    print(row[3])
                    break
            else:
                print("No such employee!")

        elif ch == 2:
            id = int(input("Enter employee ID:"))
            csvfile.seek(0)
            next(file)  
            for row in file:
                if row and int(row[0]) == id:
                    print(row[2])
                    break
            else:
                print("No such employee!")


main()


