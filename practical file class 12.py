# Q1: Function to count the occurrence of each character in a given string
def countcharacters(inputstring):
    charcount = {}

    for char in inputstring:
        if char in charcount:
            charcount[char] += 1
        else:
            charcount[char] = 1

    for char, count in charcount.items():
        print("The character '{}' appears {} times in the string." .format(char, count))

userinp = input("Enter a string: ")
countcharacters(userinp)


# Q2: Function to calculate the area of a rectangle
def area(l, b):
    return l * b
length = float(input("Enter length of the rectangle:"))
breadth = float(input("Enter breadth of the rectangle:"))
ar = area(length, breadth)
print("The area of the rectangle is", ar) 


# Q3: Program to check if a number is a palindrome or Armstrong number
def palindrome(number):
    numstr = str(number)
    return numstr == numstr[::-1]

def armstrong(number):
    numstr = str(number)
    numdigits = len(numstr)
    armstrongsum = sum(int(digit) ** numdigits for digit in numstr)
    return armstrongsum == number

while True:
    print("\nMenu:")
    print("1. Check if a number is palindrome")
    print("2. Check if a number is Armstrong")
    print("3. Exit")
    choice = input("Enter your choice (1/2/3): ")
    if choice == '1':
        usernum = int(input("Enter a number: "))
        if palindrome(usernum):
            print(usernum, " is a palindrome.")
        else:
            print(usernum, " is not a palindrome.")

    elif choice == '2':
        usernum = int(input("Enter a number: "))
        if armstrong(usernum):
            print(usernum, " is an Armstrong number.")
        else:
            print(usernum, " is not an Armstrong number.")

    elif choice == '3':
        print("Exiting the program. Bye bye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")


# Q4: Function to generate the Fibonacci series up to 'n' terms
def fibonacciseries(n):
    fibseries = [0, 1]
    while len(fibseries) < n:
        fibseries.append(fibseries[-1] + fibseries[-2])
    return fibseries
n = int(input("Enter value of n:"))
print("Fibonacci Series up to", n, fibonacciseries(n))


# Q5: Program to simulate rolling a dice until the user exits
import random
def roll_a_dice():
    return random.randint(1, 6)

while True:
    print("t-> to throw a dice!")
    print("e-> to exit!")
    r = input("Enter your choice, t or e => ")

    if r == 't':
        print(roll_a_dice())

    elif r == 'e':
        print("Program ended!")
        break


# Q6: Program to count the number of alphabets, digits, spaces, and special characters in a file
myfile = open("E:\\dreams.txt", "r")
readin = myfile.read()
alphabet = 0
uppercase = 0
lowercase = 0
digits = 0
spaces = 0
spchar = 0

for char in readin:
    if char.isalpha():
        alphabet += 1
        if char.isupper():
            uppercase += 1
        elif char.islower():
            lowercase += 1
    elif char.isdigit():
        digits += 1
    elif char.isspace():
        spaces += 1
    else:
        spchar += 1

print("Number of alphabets in the file is:", alphabet)
print("Number of uppercase letters in the file is:", uppercase)
print("Number of lowercase letters in the file is:", lowercase)
print("Number of digits in the file is:", digits)
print("Number of spaces in the file is:", spaces)
print("Number of special characters in the file is:", spchar)
myfile.close()


# Q7: Program to count the number of vowels, consonants, uppercase and lowercase letters in a file
myfile = open("E:\\dreams.txt", "r")
readin = myfile.read()
vcount = 0
ccount = 0
uppercase = 0
lowercase = 0
vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']

for char in readin:
    if char.isalpha():
        if char.isupper():
            uppercase += 1
        elif char.islower():
            lowercase += 1
    if char in vowels:
        vcount += 1
    elif char.isalpha and char not in vowels:
        ccount += 1

print("Number of vowels in the file is:", vcount)
print("Number of consonants in the file is:", ccount)
print("Number of uppercase letters in the file is:", uppercase)
print("Number of lowercase letters in the file is:", lowercase)
myfile.close()


# Q8: Program to read a file and print words separated by '#'
myfile = open("E:\\dreams.txt", "r")
line = myfile.readline()

while line:
    for word in line.split():
        print(word, end='#')
    print()
    line = myfile.readline()

myfile.close()


# Q9: Program to print lines from a file that start with the letter 'T'
myfile = open("E:\\dreams.txt", "r")
for line in myfile:
    if line.startswith('T'):
        print(line)

myfile.close


# Q10: Program to filter lines containing 'a' from a file and write the rest to another file
with open("E:\\dreams.txt", "r") as infile, open("E:\\dreams_filtered.txt", "w") as outfile:
    for line in infile:
        if "a" in line.lower():
            continue
        outfile.write(line)

file1 = open("E:\\dreams_filtered.txt", "r")
line = file1.read()
print(line)


# Q11: Program to write student records using pickle and search by roll number
import pickle
record = []

def write():
    file = open("student.dat", "+wb")
    while True:
        rollno = int(input("Enter your roll number: "))
        name = input("Enter your name: ")
        data = [rollno, name]
        record.append(data)
        ch = input("Want to enter more records (Y/N)?: ")
        if ch.lower() == "n":
            break
            
    pickle.dump(record, file)
    file.close()

def read():
    file = open("student.dat", "rb")
    r = pickle.load(file)
    for i in r:
        print(i)
    file.close()

def search():
    rollno = int(input("Enter roll number you want to search: "))
    file = open("student.dat", "rb")
    a = 0
    r = pickle.load(file)
    for i in r:
        if i[0] == rollno:
            print(i)
            a = 1
            break
    if a == 0:
        print("Roll number not found")

write()
print("Data written successfully!")
read()
print("Data read successfully")
search()


# Q12: Program to write student records with marks, read, and update using pickle
import pickle
record = []

def write():
    file = open("student1.dat", "ab")
    while True:
        rollno = int(input("Enter your roll number: "))
        name = input("Enter your name: ")
        marks = input("Enter your marks: ")
        data = [rollno, name, marks]
        record.append(data)
        ch = input("Want to enter more records (Y/N)?: ")
        if ch.lower() == "n":
            break

    pickle.dump(record, file)
    file.close()

def read():
    file = open("student1.dat", "rb")
    r = pickle.load(file)
    for i in r:
        print(i)
    file.close()

def update():
    rollno = int(input("Enter roll number of student whose marks are to be updated: "))
    file = open("student1.dat", "rb+")
    a = 0
    r = pickle.load(file)
    for i in r:
        if i[0] == rollno:
            i[2] = input("Enter updated marks: ")
            a = 1
            break
    file.seek(0)
    pickle.dump(r, file)
    file.close()

write()
print("Data written successfully!")
read()
print("Data read successfully")
update()
print("Data updated successfully!")
read()


# Q13: Program to generate a list of 5 unique random even numbers within a specified range
import random
even = []
a1 = int(input("Enter lower limit: "))
a2 = int(input("Enter upper limit: "))

while len(even) < 5:
    n = random.randint(a1, a2)
    if n % 2 == 0 and n not in even:
        even.append(n)
        
print(even)


# Q14: Program to write, read, and search players' scores in a CSV file
import csv
def inplayers():
    with open("players.csv", "w", newline = '') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["Name", "Score"])
        while True:
            name = input("Enter player's name: ")
            score = int(input("Enter player's score: "))
            csvwriter.writerow([name, score])
            ch = input("Want to enter more records (Y/N)?: ")
            if ch.lower() == "n":
                break
                
def displayers():
    with open("players.csv", "r") as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            print(row)

def searchplayer():
    search = input("Enter player's name to search: ")
    with open("players.csv", "r") as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            if search == row[0]:
                print(row)

inplayers()
displayers()
searchplayer()


# Q15: Program to compute the average of player scores from a CSV file
import csv

def user():
    with open("useridpwd.csv", "w", newline='') as csvfile:
        file = csv.writer(csvfile)
        file.writerow(["User ID", "Password"])

        while True:
            userid = input("Enter your user ID: ")
            pwd = input("Enter your password: ")
            data = [userid, pwd]
            file.writerow(data)
            ch = input("Want to enter more records (Y/N)?: ")
            if ch.lower() == "n":
                break

def read():
    with open("useridpwd.csv", "r") as csvfile:
        file = csv.reader(csvfile)
        for row in file:
            print(row)

def search():
    with open("useridpwd.csv", "r") as csvfile:
        file = csv.reader(csvfile)
        next(file)
        a = input("Enter the user ID you want to search: ")
        for i in file:
            if i[0] == a:
                print("User ID:", i[0] ,"Password:", i[1])

user()
read()
print("Data read successfully!")
search()



#Q16 Push Elements into Stack Based on Divisibility by 5
def push(arr):
    stack = []

    for num in arr:
        if num % 5 == 0:
            stack.append(num)
    if stack:
        print("Stack:", stack)
    else:
        print("No numbers divisible by 5 in the list.")

list1 = input("Enter list of numbers separated by spaces :")
list2 = [int(num) for num in list1.split()]
push(list2)


#Q17  Pop an Element from the Stack
def pop(stack):
    if not stack:
        print("Stack is empty. Cannot pop.")
        return None
    else:
        popvalue = stack.pop()
        return popvalue

list1 = input("Enter numbers sepearated by spaces:")
stack = [int(num) for num in list1.split()]

popvalue = pop(stack)
print("Value popped from the stack:", popvalue)
print("Updated stack:", stack)
