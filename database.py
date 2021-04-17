# create record
# update record
# read record
# delete record
# CRUD operation

# find user

import os
import validation

user_db_path = "data/user_record/"
auth_db_path = "data/auth_session/"


def create(user_account_number, first_name, last_name, email, password):
    user_data = first_name + "," + last_name + "," + email + "," + password + "," + str(0)

    if does_account_number_exist(user_account_number):
        return False

    if does_email_exist(email):
        return False

    completion_state = False

    try:
        print("create a new user record")
        f = open(user_db_path + str(user_account_number) + ".txt", "x")

    except FileExistsError:
        print("Username already exist")

        does_file_contain_data = read(user_db_path + str(user_account_number) + ".txt")

        if not does_file_contain_data:
            delete(user_account_number)

    else:
        f.write(str(user_data))
        completion_state = True

    finally:
        f.close()
        return completion_state

    # create a file
    # name of the file would be account_number.txt
    # add the user_details to the file
    # return true


def update(user_details):
    print("update user record")
    # find user with account number
    # fetch the content of the file
    # update the content of the file
    # save the file


def read(user_account_number):
    print("read user record")
    # find user with account number
    # fetch content of the file

    is_valid_account_number = validation.account_number_validation(user_account_number)

    try:
        if is_valid_account_number:
            f = open(user_db_path + str(user_account_number) + ".txt", "r")

        else:
            f = open(user_db_path + user_account_number, "r")

    except FileNotFoundError:

        print("User not found")

    except TypeError:
        print("Invalid Account number format")

    else:

        return f.readline()

    return False


def delete(user_account_number):
    print("delete user record")
    # find user with account number
    # delete the user record(file)
    # return true

    is_delete_successful = False

    if os.path.exists(user_db_path + str(user_account_number) + ".txt"):
        try:

            os.remove(user_db_path + str(user_account_number) + "txt")
            is_delete_successful = True

        except FileNotFoundError:

            print("User Not Found")

        finally:

            return is_delete_successful


def does_email_exist(email):
    all_users = os.listdir(user_db_path)

    for user in all_users:
        user_list = str.split(read(user), ',')
        if email in user_list:
            return True

    return False


def does_account_number_exist(account_number):
    all_users = os.listdir(user_db_path)
    for user in all_users:
        if user == str(account_number) + ".txt":
            return True

    return False


def authenticated_user(account_number, password):
    if does_account_number_exist(account_number):

        user = str.split(read(account_number), ',')

        if password == user[3]:
            return user

    return False


def find(user_account_number):
    print("find user")
    # find user record in the data folder


