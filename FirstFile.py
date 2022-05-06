import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017')
db = client.Banking
accounts = db.accounts
loan = db.loan

def Account_Details():
    account_number = int(input("Enter your account number: "))
    find = db.accounts.find_one({"AccountNumber": account_number})
    print("")
    print(f'Account info:\n{find}')
    print()
    menu()

def Create_Account():
    account_number_in = int(input("Please create an account number: "))
    name_in = input("Enter your full name: ")
    phone_in = input("Enter your phone number: ")
    email_in = input("Enter your email: ")
    balance_in = float(input("How much would you like to deposit: $"))
    insert = db.accounts.insert_one({
        "AccountNumber": account_number_in,
        "FullName" : name_in,
        "PhoneNumber":phone_in,
        "Email":email_in,
        "Account balance": balance_in
    })
    insert
    print("")
    print("Your account has been created.\nThank you for being part of our family.")
    print("")
    menu()

def update():
    account_update = int(input("Please enter the account number you want to update: "))
    phone_update = input("Please enter the phone number you want to update: ")
    email_update = input("Please enter the email you want to update: ")
    change = db.accounts.update_one({"AccountNumber": account_update}, {"$set": {"PhoneNumber": phone_update,
                                                                                 "Email":email_update}})
    change
    print("Update Completed")
    print("")
    menu()


def Delete_Account():
    account_delete = int(input("Enter the account number you want to delete: "))
    remove = db.accounts.delete_one({"AccountNumber": account_delete})
    remove
    print("")
    print("Your account has beem deleted.\nWe are sad to see you go.")
    print("")
    exit()


def Make_Loan():

    account_loan = int(input("Please enter the account number you want to make a loan with: "))
    loan_amount = float(input("Enter the amount you wish acquire: $"))
    loan_lenght = int(input("How many months would you like the loan for: "))
    loan_goal = input("What is the loan for: ")
    loan_credit = int(input("What is your credit score: "))

    db.loan.insert_one({
        "AccountNumber":account_loan,
        "Loan Amount": loan_amount,
        "Length of Loan in Months": loan_lenght,
        "The Goal": loan_goal,
        "Credit Score":loan_credit
    })
    if loan_credit > 650 and loan_amount < 100000:
        print("Granted\nCongradulations!")
    else:
        print("Sorry you don't qualify")
    print("")
    menu()





def menu():
    print('Welcome to Banking LLC \n1.Account Details\n2.Create Account\n3.update\n4.Get a Loan\n5.delete Account\n6.exit')
    choice = int(input("Select an option: "))
    if(choice == 1):
        Account_Details()
    elif(choice == 2):
        Create_Account()
    elif(choice == 3):
        update()
    elif(choice == 4):
        Make_Loan()
    elif(choice == 5):
        Delete_Account()
    elif(choice == 6):
        print("Have a nice day!")
        exit()
    else:
        print('Please select the options available above')
        menu()
menu()









