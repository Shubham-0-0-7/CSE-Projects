import mysql.connector as sql

con = sql.connect(
    host = "localhost",
    user = "root",
    password = "shubham@2006",
    database = "abc")
c = con.cursor()

create_account_table_query = '''
CREATE TABLE IF NOT EXISTS account (
    name VARCHAR(50),
    accno INT,
    dob DATE,
    address VARCHAR(50),
    openbal INT
);
'''
c.execute(create_account_table_query)

create_amount_table_query = '''
CREATE TABLE IF NOT EXISTS amount (
    name VARCHAR(50),
    accno INT,
    totalbalance INT
);
'''
c.execute(create_amount_table_query)
con.commit()

def main():
    while True:
        print("\n" + "="*30)
        print("        BANKING SYSTEM")
        print("="*30 + "\n")
        print("""
        1. OPEN NEW ACCOUNT
        2. DEPOSIT MONEY
        3. WITHDRAW MONEY
        4. BALANCE ENQUIRY
        5. DISPLAY CLIENT DETAILS
        6. CLOSE AN ACCOUNT
        7. EXIT
        """)
        ch = int(input("Enter the task no.: "))
        print("="*30 + "\n")

        if ch == 1:
            print("=== OPENING A NEW ACCOUNT ===")
            openacc()
        elif ch == 2:
            print("=== DEPOSIT MONEY ===")
            depam()
        elif ch == 3:
            print("=== WITHDRAW MONEY ===")
            witham()
        elif ch == 4:
            print("=== BALANCE ENQUIRY ===")
            balance()
        elif ch == 5:
            print("=== DISPLAY CLIENT DETAILS ===")
            dispacc()
        elif ch == 6:
            print("=== CLOSE AN ACCOUNT ===")
            closeacc()
        elif ch == 7:
            print("\nThank you for using our Banking System. Have a great day!")
            break
        else:
            print("Invalid Entry!!")
            print("Please Try again...")


def openacc():
    n = input("Enter Name: ")
    ac = input("Enter Account No.: ")
    db = input("Enter D.O.B: ")
    ad = input("Enter Address: ")
    totalbalance = int(input("Enter Opening Balance :"))
    data1 = (n, ac, db, ad, totalbalance)
    data2 = (n, ac, totalbalance)
    sql1 = 'insert into account values(%s, %s, %s, %s, %s)'
    sql2 = 'insert into amount values(%s,%s,%s)'
    c = con.cursor()
    c.execute(sql1, data1)
    c.execute(sql2, data2)
    con.commit()

    print("\n=== ACCOUNT OPENED SUCCESSFULLY ===")
    print("Name:", n)
    print(f"Account No.: {ac}")
    print(f"New Balance: ${totalbalance}")
    print("="*30)
    main()


def depam():
    am = int(input("Enter Amount: "))
    ac = input("Enter account no.: ")

    selectquery = "SELECT totalbalance FROM amount WHERE accno = %s"
    data = (ac,)
    c.execute(selectquery, data)
    myresult = c.fetchone()

    if myresult:
        currentbalance = myresult[0]
        newbalance = currentbalance + am

        updatequery = "UPDATE amount SET totalbalance = %s WHERE accno = %s"
        data = (newbalance, ac)
        c.execute(updatequery, data)
        con.commit()

        print("\n=== UPDATED ACCOUNT BALANCE ===")
        print(f"Account No.: {ac}")
        print(f"New Balance: ${newbalance}")
        print("="*30)

        print("Amount deposited successfully.")
    else:
        print("Account not found.")

    main()


def witham():
    am = int(input("Enter Amount: "))
    ac = input("Enter Account No: ")

    selectquery = "SELECT totalbalance FROM amount WHERE accno = %s"
    data = (ac,)
    c.execute(selectquery, data)
    myresult = c.fetchone()

    if myresult:
        currentbalance = myresult[0]

        if currentbalance >= am:
            newbalance = currentbalance - am

            updatequery = "UPDATE amount SET totalbalance = %s WHERE accno = %s"
            data = (newbalance, ac)
            c.execute(updatequery, data)
            con.commit()

            print("\n=== UPDATED ACCOUNT BALANCE ===")
            print(f"Account No.: {ac}")
            print(f"New Balance: ${newbalance}")
            print("="*30)

            print("Amount withdrawn successfully.")
        else:
            print("Insufficient balance.")
    else:
        print("Account not found.")

    main()


def balance():
    ac = input("Enter Account No: ")
    selectquery = "SELECT totalbalance FROM amount WHERE accno = %s"
    data = (ac,)
    c.execute(selectquery, data)
    myresult = c.fetchone()

    if myresult:
        balance_amount = myresult[0]
        print("\n=== ACCOUNT BALANCE ===")
        print(f"Account No.: {ac}")
        print(f"Current Balance: ${balance_amount}")
        print("="*30)
    else:
        print("Account not found.")

def dispacc():
    ac = input("Enter Account No. Whose Info. is needed:")
    select_query = '''SELECT account.*, amount.totalbalance 
                      FROM account, amount 
                      WHERE account.accno = amount.accno 
                      AND account.accno = %s'''
    data = (ac,)
    c.execute(select_query, data)
    my_result = c.fetchone()

    if my_result:
        print("\n=== CLIENT DETAILS ===")
        print(f"Name: {my_result[0]}")
        print(f"Account No.: {my_result[1]}")
        print(f"Date of Birth: {my_result[2]}")
        print(f"Address: {my_result[3]}")
        print(f"Balance: {my_result[5]}")
        print("=" * 30)
    else:
        print("Account not found.")

    main()



def closeacc():
    ac = input("Enter Account No: ")
    deleteaccountquery = "DELETE FROM account WHERE accno = %s"
    deleteamountquery = "DELETE FROM amount WHERE accno = %s"
    data = (ac,)

    c.execute(deleteaccountquery, data)
    c.execute(deleteamountquery, data)
    con.commit()

    print("\n=== ACCOUNT CLOSURE ===")
    print(f'''We appreciate the time you spent with us. 
          Your account (No. {ac}) has been closed successfully. 
          If you ever decide to return, we'll be here for you. 
          Thank you, and best wishes on your financial journey!''')
    print("=" * 70)



main()
