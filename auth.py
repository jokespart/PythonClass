#register
# - need username,password,email
# - generate user account

# login
# -  need username or email and password

# initializing the system
import random
from datetime import datetime
database={}

def init():

    print("Welcome to BankPHP")

    haveAccount = int(input("Do you have account with us: 1(yes) 2 (no) \n"))

    if(haveAccount == 1):
        login()
    elif(haveAccount == 2):
        register()
    else:
        print("You have selected invalid option")
        init()

def login():

        accountNumberFromUser = int(input("What is your account number? \n"))
        password = input("What is your password? \n")

        for accountNumber,userDetails in database.items():
            if(accountNumber == accountNumberFromUser):

                if(userDetails[3] == password):
                    print("Login Successful")
                    bankOperation(userDetails)
             else:
                 print("Invalid account or password")
        init()


def register():
    print("Now you can Register a new account")
    email = input("What is your email address \n")
    first_name = input("What is your first name \n")
    last_name = input("What is your last name \n")
    password = input("create a password for yourself \n")

    accountNumber = generationAccountNumber()

    database[accountNumber] = [first_name,last_name,email,password]

    print("Congratulations,your Account has been created")
    print("=============================================")
    print("Your account number is %d" % accountNumber)
    login()


def bankOperation(user):
    print("Welcome %s %s " % (user[0], user[1]))
    #selectedOption=1
    selectedOption = int(input("What would you like to do?: (1) Withdrawal (2) Deposit (3) Complaint  (4) Exit \n"))

    if(selectedOption) == 1:
        withdrawalOperation()
        a = int(input('Will you like another transaction: (1) yes (2) no \n'))
        if (a == 1):
            bankOperation(user)
        else:
            exit()

    elif(selectedOption) == 2:
        depositOperation()
        a = int(input('Will you like another transaction: (1) yes (2) no \n'))
        if (a == 1):
            bankOperation(user)
        else:
            exit()

    elif(selectedOption) == 3:
        Complaint = input('What issue do you want to report: \n')
        print('Thank you for contacting us')
        a = int(input('Will you like another transaction: (1) yes (2) no \n'))
        if (a == 1):
            bankOperation(user)
        else:
            exit()

    elif(selectedOption) == 4:
        print('Thank you for using our ATM machine')
        exit()

    else:
        print("Invalid Option selected")
        print("=======================")

    bankOperation(user)

def depositOperation():
    print("Deposit Operations")
    deposit = int(input("How much do you want to deposit? \n"))
    #balance = [100, 150, 200]
    #balance += deposit
    print("Your cash is deposited")

def withdrawalOperation():
    print("Withdrawal Operations")
    withdrawal = int(input('How much will you like to withdraw?: \n'))
    #balance = [100, 150, 200]
    #balance -= withdrawal
    print('Take your cash.')

def logout():
    print('Thank you for using our ATM machine')
    exit()

def generationAccountNumber():

    return random.randrange(11111111,99999999)

#print(generationAccountNumber())
init()
register()
