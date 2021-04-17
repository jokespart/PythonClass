# register
# - need username,password,email
# - generate user account

# login
# -  need username or email and password

# initializing the system
import random
import validation
import database
from getpass import getpass
import os

user_db_path = "data/user_record/"
auth_db_path = "data/auth_session/"

global user_account_number


# database_a = {}  # dictionary


def init():
    print("Welcome to BankPHP")

    have_account = int(input("Do you have account with us: 1(yes) 2 (no) \n"))

    if have_account == 1:
        login()

    elif have_account == 2:
        register()

    else:
        print("You have selected invalid option")
        init()


def login():
    print("**********Login**********")
    account_number_from_user = input("What is your account number? \n")

    is_valid_account_number = validation.account_number_validation(account_number_from_user)

    if is_valid_account_number:
        password = getpass("What is your password? \n")

        user = database.authenticated_user(account_number_from_user, password)

        if user:
            bank_operation(user)
            log_in(user)
    else:
        print("Account Number Invalid: check that you have up to 10 digits and only integers")
        init()


def register():
    print("Now you can Register a new account")
    email = input("What is your email address \n")
    first_name = input("What is your first name \n")
    last_name = input("What is your last name \n")
    # password = input("create a password for yourself \n")
    password = getpass("Create a password for yourself \n")

    # accountNumber = generationAccountNumber()
    account_number = generation_account_number()

    # database[accountNumber] = [first_name, last_name, email, password]

    is_user_created = database.create(account_number, first_name, last_name, email, password)

    if is_user_created:
        print("Congratulations,your Account has been created")
        print("=============================================")
        print("Your account number is %d" % account_number)

        login()

    else:
        print("Something went wrong, please try again")
        register()


def bank_operation(user):
    print("Welcome %s %s " % (user[0], user[1]))

    selected_option = int(input("What would you like to do?: (1) Withdrawal (2) Deposit (3) Complaint  (4) Exit \n"))

    if selected_option == 1:
        withdrawal_operation(user)
        a = int(input('Will you like another transaction: (1) yes (2) no \n'))
        if a == 1:
            bank_operation(user)
        else:
            exit()

    elif selected_option == 2:
        deposit_operation(user)
        a = int(input('Will you like another transaction: (1) yes (2) no \n'))
        if a == 1:
            bank_operation(user)
        else:
            exit()

    elif selected_option == 3:
        complaint = input('What issue do you want to report: \n')
        print('Thank you for contacting us')
        a = int(input('Will you like another transaction: (1) yes (2) no \n'))
        if a == 1:
            bank_operation(user)
        else:
            exit()

    elif selected_option == 4:
        print('Thank you for using our ATM machine')
        exit()

    else:
        print("Invalid Option selected")
        print("=======================")

    bank_operation(user)


def deposit_operation(user):
    print("Deposit Operations")
    # get current balance
    account_balance = user[4]
    amount = float(input("How much will you like to deposit \n"))
    account_balance += amount
    print("Your current balance is %d" % account_balance)


def withdrawal_operation(user):
    print("Withdrawal Operations")
    account_balance = user[4]
    amount = float(input('How much will you like to withdraw? '))
    # check if current balance > withdraw balance
    if account_balance >= amount:
        # deduct withdrawn amount from current balance
        try:
            print("\n You have withdrawn %d" % amount)
            account_balance = account_balance - amount
            # display current balance
            print("\n Your current balance is  %d" % account_balance)
        except:
            print("Cannot be withdrawn at this time")

    else:
        print("\n You have Insufficient balance in your account")


def set_current_balance(user_details, balance):
    user_details[4] = balance


def get_current_balance(user_details):
    return user_details[4]


def logout():
    print('Thank you for using our ATM machine')
    if os.path.exists(auth_db_path + str(user_account_number) + ".txt"):
        try:

            os.remove(auth_db_path + str(user_account_number) + "txt")
            is_delete_successful = True

        except FileNotFoundError:

            print("File Not Found")
    login()


def log_in():
    print('Thanks for logging in')

    is_login_successful = True

    try:
        f = open(auth_db_path + str(user_account_number) + ".txt", "x")
        is_login_successful = False
    except FileExistsError:
        print("File Exist")

    f.close()


def generation_account_number():
    return random.randrange(11111111, 99999999)


init()
