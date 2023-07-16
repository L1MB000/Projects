#Ericko Bayu Listyo Suherman
#TP062715
def start_program():
    word = "Welcome to myBank!"
    my_decoration_str((" " * 4) + word) #to concatenate strings with decorations
    account_id_validation()

def my_decoration_str(string_to_wrap):
    print("=" * 26 + "\n" + string_to_wrap + "\n" + "=" *26) #concatenate strings

def account_id_validation():
    while True:
        with open("AccountData.txt", "r") as account_list:
            acc_data = account_list.readlines() #convert the txt, into a list format which already splitted with ("\n")
            account_id = input("Account ID: ")
            checker = 0
            for line in acc_data:
                acc_line = line.replace("\n",":").split(":") #replace the \n to :, and split the list whenever there are : occur.
                if account_id == acc_line[0]:
                    checker = 1
                    account_id_rec = acc_line[0]
                    account_pass_rec = acc_line[1]
                    account_type_rec = acc_line[2]
                    account_password_validation(account_pass_rec, account_type_rec, account_id_rec, acc_line)
                    break
                else:
                    pass
            if checker == 1:
                break
            else:
                print("You enter a wrong account ID! \n")
                my_decoration_str(" Please re-enter your ID!")

def account_password_validation(acc_password, acc_type, acc_id, acc_line):
    account_pass = input("Password: ")
    if account_pass == acc_password:
        account_type_checker(acc_type, acc_id, acc_line)
    else:
        print("Invalid Password! \n")
        my_decoration_str(" Please re-enter your ID!")
        account_id_validation()

def account_type_checker(acc_type, acc_id, acc_line):
    if acc_type == "super":
        print("\nWelcome back boss!")
        super_function(acc_id)
    elif acc_type == "admin":
        print("\nWelcome back " + acc_line[3] + "!")
        admin_function(acc_type, acc_id)
    else:
        print("\nWelcome back " + acc_line[4] + "!")
        customer_function(acc_id)

def super_function(id):
    while True:
        super_acc_menu()
        user_choice = str(input("Select your option (1-6): "))
        if user_choice == "1":
            type = 'super'
            create_account(type) #since type = super, then it will create admin ID
        elif user_choice == "2":
            type = 'admin'
            create_account(type) #since type = admin, then it will create customer ID
        elif user_choice == "3":
            edit_admin_account(id)
        elif user_choice == "4":
            account_finder()
        elif user_choice == "5":
            showing_customer_report()
        elif user_choice == "6":
            print("\n*Thankyou for your visit*")
            break
        else:
            print("\nSorry, we dont have that option")

def edit_admin_account(id_super):
    id = admin_checker_to_edit() #function for checking the id of customer
    while True:
        data_location, index_of_line = admin_checker_updater(id) #function for checking the data line
        print("\n" + (" " * 2) + "Edit Admin Account")
        print("=" * 26)
        print(" Admin account details\n")
        print(f'1. Name: {data_location[3]}\n2. Email Address: {data_location[4]}\n3. Address: {data_location[5]}\n4. Phone Number: {data_location[6]}\n5. Exit editing customer menu')
        print("=" * 26)
        answer = edit_admin_account_option_checker() #function to let admin choose what data wanted to be changed
        if answer != "exit":
            change_data_admin(data_location, index_of_line, answer, id_super, id) #function to replace data
            print(("\n" + "=" * 26) + "\n   **account updated!**\n" + ("=" * 26))
        else:
            break

def change_data_admin(data_location, index_of_line, answer, id_super, id_admin_to_change):
    with open("AccountData.txt","r") as data_file: #open file in read mode
        list_of_lines = data_file.readlines()
        while True:
            data_changed = (input("New data: ")).strip()
            if answer == "email":
                checker = acc_email_address_checker(data_changed)
                if checker == 1:
                    print("")
                    continue
                else:
                    list_of_lines[index_of_line] = f'{data_location[0]}:{data_location[1]}:{data_location[2]}:{data_location[3]}:{data_changed}:{data_location[5]}:{data_location[6]}' + f"\n"
                    break
            elif answer == "address":
                checker = acc_address_checker(data_changed)
                if checker == 1:
                    print("")
                    continue
                else:
                    list_of_lines[index_of_line] = f'{data_location[0]}:{data_location[1]}:{data_location[2]}:{data_location[3]}:{data_location[4]}:{data_changed}:{data_location[6]}' + f"\n"
                    break
            elif answer == "phone number":
                checker = acc_phone_num_checker(data_changed)
                if checker == 1:
                    list_of_lines[index_of_line] = f'{data_location[0]}:{data_location[1]}:{data_location[2]}:{data_location[3]}:{data_location[4]}:{data_location[5]}:{data_changed}' + f"\n"
                    break
                else:
                    print("") #new line
                    continue
        with open("AccountData.txt", "w") as f: #open file in write mode
            f.writelines(list_of_lines)


def edit_admin_account_option_checker():
    while True:
        choice = input("Which one would you like to edit? (2-5): ")
        if choice == "1":
            print("\nSorry, but editing name are not allowed!\n")
            continue
        elif choice == "2":
            answer = "email"
        elif choice == "3":
            answer = "address"
        elif choice == "4":
            answer = "phone number"
        elif choice == "5":
            answer = "exit"
        else:
            print("\nSorry, we dont have that option\n")
            continue
        return answer

def admin_checker_updater(id):
    while True:
        with open("AccountData.txt", "r") as account_list:
            acc_datas = account_list.readlines()
            index_line = -1
            for line in acc_datas:
                acc_line = line.replace("\n",":").split(":")
                index_line += 1
                if id == acc_line[0] and acc_line[2] == "admin":
                    data_line_location = acc_line
                    return data_line_location, index_line

def admin_checker_to_edit():
    while True:
        with open("AccountData.txt", "r") as account_list:
            acc_datas = account_list.readlines()
            id = input("\nInput admin account id: ")
            checker = 0
            for line in acc_datas:
                acc_line = line.replace("\n",":").split(":")
                if id == acc_line[0] and acc_line[2] == "admin":
                    checker = 1
                    break
                elif id == acc_line[0] and acc_line[2] != "admin":
                    checker = 2
                else:
                    pass
            if checker == 1:
                return id
            elif checker == 2:
                print("\nYou input a not admin ID, only allowed to edit admin account.")
            else:
                print("\nAccount's ID not found.")

def super_acc_menu(): #Menu for super account
    print("\n" + (" " * 8) + "Super Menu")
    print("=" * 26)
    print("1. Create Admin Account")
    print("2. Create Customer Account")
    print("3. Edit Admin Account")
    print("4. View Admin/Customer Account")
    print("5. View Costumer's Report")
    print("6. Exit")
    print("=" * 26)
    print("What do you want to do?")

def account_finder():
    while True:
        checker = 0
        with open('AccountData.txt', 'r') as data_file:
            data_file = data_file.readlines()
            account = input("\nAccount ID to check: ")
            for each_line in data_file:
                each_line = each_line.replace("\n",":").split(":")
                if each_line[0] == account and each_line[2] == "super":
                    checker = 2
                    break
                elif each_line[0] == account:
                    checker = 1
                    break
        if checker == 0:
            print("Sorry, no account found!")
            continue
        elif checker == 2:
            print("There are no details in your super account")
            continue
        else:
            if each_line[2] == "admin":
                print("=" * 26)
                print(f'     Account Details\n\nName         : {each_line[3]}\nEmail Address: {each_line[4]}\nAddress      : {each_line[5]}\nPhone Number : {each_line[6]}')
                print("=" * 26)
            elif each_line[2] == "customer":
                print("=" * 26)
                print(f'     Account Details\n\nName         : {each_line[4]}\nEmail Address: {each_line[5]}\nAddress      : {each_line[6]}\nPhone Number : {each_line[7]}\nType Account : {each_line[3]}')
                print("=" * 28)
        next_option = input("Type anything to continue: ")
        if next_option != None: #enter anything to continue
            break

def create_account(type_of_an_account):
    with open("AccountData.txt","a") as create_new_acc:
        if type_of_an_account == "super":
            acc_type = "admin"
            acc_id, acc_def_pass, acc_name, acc_email_address, acc_address, acc_phone = id_pass_giving(type_of_an_account)
            create_new_acc.write(f"{acc_id}:{acc_def_pass}:{acc_type}:{acc_name}:{acc_email_address}:{acc_address}:{acc_phone}\n")
        elif type_of_an_account == "admin":
            acc_type = "customer"
            acc_id, acc_def_pass, acc_name, acc_email_address, acc_address, acc_phone, acc_type_cos = id_pass_giving(type_of_an_account)
            if acc_type_cos == "saving":
                create_new_acc.write(f"{acc_id}:{acc_def_pass}:{acc_type}:{acc_type_cos}:{acc_name}:{acc_email_address}:{acc_address}:{acc_phone}:100.0\n") #write into txt
            elif acc_type_cos == "current":
                create_new_acc.write(f"{acc_id}:{acc_def_pass}:{acc_type}:{acc_type_cos}:{acc_name}:{acc_email_address}:{acc_address}:{acc_phone}:500.0\n")
        print("\n   " + ("=" * 22) + "\n   ***Account created!***\n   " + ("=" * 22))

def id_pass_giving(type_of_account):
    with open("AccountData.txt","r") as file:
        acc_data = file.readlines()
        last_line = len(acc_data) - 1 #find the last line index in txt
        splitter = acc_data[last_line].split(":")
        first_element = splitter[0] #find id elements
        new_id = "ABC" + str(int(first_element[3:]) + 1).zfill(4) #find the digit only
        default_password = str(int(first_element[3:]) + 1).zfill(6) #generate password by following the ID
        if type_of_account == "super":
            acc_name, acc_email_address, acc_address, acc_phone_num = super_create_admin_menu(new_id, default_password)
            return new_id, default_password, acc_name, acc_email_address, acc_address, acc_phone_num
        elif type_of_account == "admin":
            acc_name, acc_email_address, acc_address, acc_phone_num, acc_type = admin_create_customer_menu(new_id, default_password)
            return new_id, default_password, acc_name, acc_email_address, acc_address, acc_phone_num, acc_type

def super_create_admin_menu(new_id, default_password):
    while True:
        print("\n" + (" " * 2)+ "Admin Account Registration Form")
        print("=" * 26)
        acc_name = (input("Name: ")).strip()
        name_checker = acc_name_checker(acc_name)
        if name_checker == 1 or name_checker == 2:
            continue
        else:
            pass

        acc_email_address = (input("Email Address: ")).strip()
        email_checker = acc_email_address_checker(acc_email_address)
        if email_checker == 1:
            continue
        else:
            pass

        acc_address = (input("Address: ")).strip()
        address_checker = acc_address_checker(acc_address)
        if address_checker == 1:
            continue
        else:
            pass

        acc_phone_num = (input("Phone Number: ")).strip()
        phone_num_checker = acc_phone_num_checker(acc_phone_num)
        if phone_num_checker == 1:
            pass
        else:
            continue

        print(("=" * 26) + "\n\n" + ("=" * 26))
        print("Admin account details:\n")
        print(f'Name: {acc_name}\nEmail Address: {acc_email_address}\nAddress: {acc_address}\nPhone Number: {acc_phone_num}')
        print("\n" + "   ***Given by MyBank***")
        print(f'Admin ID: {new_id}\nDefault password: {default_password}')
        print("=" * 26)
        answer_from_user = confirmation()
        if answer_from_user == "register":
            return acc_name, acc_email_address, acc_address, acc_phone_num
        elif answer_from_user == "re-register":
            pass

def acc_name_checker(data):
    checker = 0
    letter = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ '
    for data_character in data:
        if data_character in letter: #checking if each character are exist in letter.
            continue
        else:
            checker = 1
            break
    if checker == 1:
        print("Sorry, only letters are allowed!")
    elif data == "" or data == " ":
        print("You should not leave it empty!")
        checker = 2
    else:
        pass
    return checker

def acc_email_address_checker(data):
    checker1 = 0
    checker2 = 0
    instant_no = False
    for data_character in data:
        if data_character == "@":
            checker1 += 1 #to check if there is "@" symbol in the user input
        elif data_character == ".":
            checker2 = 1 #to check if there is "." symbol in the user input
        elif data_character == " ":
            instant_no = True #to check if the input is empty
        else:
            pass
    if instant_no == True:
        print("Sorry, no whitespaces allowed!")
        final_checker = 1
    elif checker1 == 1 and checker2 == 1:
        final_checker = 0
    else:
        print("Please write the email address carefully!")
        final_checker = 1
    return final_checker

def acc_address_checker(data):
    checker = 0
    if data == "" or data == " ":
        checker = 1
    else:
        pass
    if checker == 1:
        print("You should not leave it empty!")
    else:
        pass
    return checker

def acc_phone_num_checker(data):
    checker = 0
    try:
        if (data[0].isdigit() or data[0] == "+") and data[1:].isdigit(): #ID phone number allowed to start either with +, or digit.
            checker = 1
        else:
            pass
    except:
        pass
    if checker == 1:
        pass
    else:
        print("Sorry, please write in this format (+xxxxxxxxxx)")
    return checker

def acc_card_type_checker(data):
    checker = 0
    acc_type = ""
    if data == "s":
        acc_type = "saving"
        checker = 1
    elif data == "c":
        acc_type = "current"
        checker = 1
    else:
        print(("=" * 26) + "\nPlease choose only between c / s!\nc for current account\ns for saving account")
    return checker, acc_type

def admin_create_customer_menu(new_id, default_password):
    while True:
        while True:
            print("\n" + (" " * 2)+ "Customer Account Registration Form")
            print("=" * 26)

            acc_name = (input("Name: ")).strip()
            name_checker = acc_name_checker(acc_name)
            if name_checker == 1 or name_checker == 2:
                continue
            else:
                pass

            acc_email_address = (input("Email Address: ")).strip()
            email_checker = acc_email_address_checker(acc_email_address)
            if email_checker == 1:
                continue
            else:
                pass

            acc_address = (input("Address: ")).strip()
            address_checker = acc_address_checker(acc_address)
            if address_checker == 1:
                continue
            else:
                pass

            acc_phone_num = (input("Phone Number: ")).strip()
            phone_num_checker = acc_phone_num_checker(acc_phone_num)
            if phone_num_checker == 1:
                pass
            else:
                continue

            acc_card_type = (input("Account type (s/c):")).strip()
            card_type_checker, acc_type = acc_card_type_checker(acc_card_type)
            if card_type_checker == 1:
                break
            else:
                continue

        print(("=" * 26) + "\n\n" + ("=" * 26))
        print("Admin account details:\n")
        print(f'Name: {acc_name}\nEmail Address: {acc_email_address}\nAddress: {acc_address}\nPhone Number: {acc_phone_num}\nAccount Type: {acc_type} account')
        print("\n" + "   ***Given by MyBank***")
        print(f'Admin ID: {new_id}\nDefault password: {default_password}')
        print("=" * 26)
        answer_from_user = confirmation()
        if answer_from_user == "register":
            return acc_name, acc_email_address, acc_address, acc_phone_num, acc_type
        elif answer_from_user == "re-register":
            pass

def confirmation():
    while True:
        print("Please check the account detail\nis everything fine?")
        print("1. Yes, please register this account")
        print("2. No, I want to re-register")
        user_choice = str(input("\nSelect your option (1-2): "))
        if user_choice == "1":
            return "register"
        elif user_choice == "2":
            return "re-register"
        else:
            print("\nSorry, we dont have that option")

def admin_function(type, id_admin):
    while True:
        admin_acc_menu()
        user_choice = str(input("Select your option (1-4): "))
        if user_choice == "1":
            create_account(type)
        elif user_choice == "2":
            edit_customer_account(id_admin)
        elif user_choice == "3":
            showing_customer_report()
        elif user_choice == "4":
            change_admin_password(id_admin)
        elif user_choice == "5":
            print("\n*Thankyou for your visit*")
            break
        else:
            print("\nSorry, we dont have that option")

def change_admin_password(id):
    print("\n" + "=" * 26)
    while True:
        data_location, index_of_line = admin_checker_updater(id) #function for checking the data
        old_password = data_location[1]
        new_password = (input("New password: ")).strip()
        if new_password == "" or new_password == " ":
            print("You should not leave it empty!\n")
            continue
        else:
            confirm_password = (input("Confirm password: ")).strip()
        if new_password == confirm_password:
            pass
        else:
            print("Sorry, try again\n")
            continue
        with open("AccountData.txt", "r") as data_file:
            data_file = data_file.readlines()
            data_file[index_of_line] = f'{data_location[0]}:{confirm_password}:{data_location[2]}:{data_location[3]}:{data_location[4]}:{data_location[5]}:{data_location[6]}' + "\n"
        with open("AccountData.txt", 'w') as data_write:
            data_write.writelines(data_file)
        print("\n" + "  ***Password Changed!***")
        break

def admin_acc_menu(): #Menu for admin
    print("\n" + (" " * 8) + "Admin Menu")
    print("=" * 26)
    print("1. Create Customer Account")
    print("2. Edit Customer's Account Detail")
    print("3. Customer's Account Report")
    print("4. Change Password")
    print("5. Exit")
    print("=" * 26)
    print("What do you want to do?")

def showing_customer_report():
    id = account_checker_to_edit()
    print("\n" + "=" * 26 + "\n" + "1. Show Customer's Balance Record\n2. Show Customer's Changed Data Record\n3. Exit\n" + "=" * 26)
    while True:
        admin_choice = input("What would you like to do? (1-3): ")
        if admin_choice == "1":
            customer_report_option(id)
            print("\n" + "=" * 26 + "\n" + "1. Show Customer's Balance Record\n2. Show Customer's Changed Data Record\n3. Exit\n" + "=" * 26)
        elif admin_choice == "2":
            checker = 0
            with open(f'AccountDataChangeRecord.txt','r') as data_change_record:
                data_change_record = data_change_record.readlines()
                print("\n" + "=" * 26)
                for each_line in data_change_record:
                    each_line = each_line.split(";")
                    if each_line[0] == id:
                        print(each_line[1], end='')
                        checker = 1
                if checker == 0:
                    print("No record found!")
                print("=" * 26)
                input("Type anything to continue: ")
                print("\n" + "=" * 26 + "\n" + "1. Show Customer's Balance Record\n2. Show Customer's Changed Data Record\n3. Exit\n" + "=" * 26)
        elif admin_choice == "3":
            break
        else:
            print("\nSorry, we dont have that option")
            continue

def edit_customer_account(id_admin):
    id = account_checker_to_edit() #function for checking the id of customer
    while True:
        data_location, index_of_line = account_checker_updater(id) #function for checking the data
        print("\n" + (" " * 2) + "Edit Customer Account")
        print("=" * 26)
        print(" Customer account details\n")
        print(f'1. Name: {data_location[4]}\n2. Email Address: {data_location[5]}\n3. Address: {data_location[6]}\n4. Phone Number: {data_location[7]}\n5. Account Type: {data_location[3]} account\n6. Password: {data_location[1]}\n\n7. Exit editing customer menu')
        print("=" * 26)
        answer = edit_customer_account_option_checker() #function to let admin choose what data wanted to be changed
        if answer != "exit":
            change_data(data_location, index_of_line, answer, id_admin, id) #function to replace data
            print(("\n" + "=" * 26) + "\n   **account updated!**\n" + ("=" * 26))
        else:
            break

def change_data(data_location, index_of_line, answer, id_admin, id_customer_to_change):
    with open("AccountData.txt","r") as data_file: #open file in read mode
        list_of_lines = data_file.readlines() #reading all lines inside lists (file)
        while True:
            old_data = data_location
            if answer == "type account":
                data_changed = (input("New account type (c/s): ")).strip()
                if data_changed == "c":
                    data_changed = "current"
                    list_of_lines[index_of_line] = f'{data_location[0]}:{data_location[1]}:{data_location[2]}:{data_changed}:{data_location[4]}:{data_location[5]}:{data_location[6]}:{data_location[7]}:{data_location[8]}' + f"\n"
                    break
                elif data_changed == "s":
                    data_changed = "saving"
                    list_of_lines[index_of_line] = f'{data_location[0]}:{data_location[1]}:{data_location[2]}:{data_changed}:{data_location[4]}:{data_location[5]}:{data_location[6]}:{data_location[7]}:{data_location[8]}' + f"\n"
                    break
                else:
                    print("\nPlease choose only between c / s!\nc for current account\ns for saving account\n")
                    continue
            else:
                data_changed = (input("New data: ")).strip()
                if answer == "email":
                    checker = acc_email_address_checker(data_changed)
                    if checker == 1:
                        print("") #new line
                        continue
                    else:
                        list_of_lines[index_of_line] = f'{data_location[0]}:{data_location[1]}:{data_location[2]}:{data_location[3]}:{data_location[4]}:{data_changed}:{data_location[6]}:{data_location[7]}:{data_location[8]}' + f"\n"
                        break
                elif answer == "address":
                    checker = acc_address_checker(data_changed)
                    if checker == 1:
                        print("") #new line
                        continue
                    else:
                        list_of_lines[index_of_line] = f'{data_location[0]}:{data_location[1]}:{data_location[2]}:{data_location[3]}:{data_location[4]}:{data_location[5]}:{data_changed}:{data_location[7]}:{data_location[8]}' + f"\n"
                        break
                elif answer == "phone number":
                    checker = acc_phone_num_checker(data_changed)
                    if checker == 1:
                        list_of_lines[index_of_line] = f'{data_location[0]}:{data_location[1]}:{data_location[2]}:{data_location[3]}:{data_location[4]}:{data_location[5]}:{data_location[6]}:{data_changed}:{data_location[8]}' + f"\n"
                        break
                    else:
                        print("")
                        continue
                elif answer == "password":
                    if data_changed == "" or data_changed == " ":
                        print("You should not leave it empty!\n")
                    else:
                        list_of_lines[index_of_line] = f'{data_location[0]}:{data_changed}:{data_location[2]}:{data_location[3]}:{data_location[4]}:{data_location[5]}:{data_location[6]}:{data_location[7]}:{data_location[8]}' + f"\n"
                        break
        with open("AccountData.txt", "w") as f:
            f.writelines(list_of_lines)
        edited_id = data_location[0]
        write_data_change_record(id_admin, answer, data_changed, old_data, id_customer_to_change)

def write_data_change_record(id_of_user, kind_of_data, new_data, old_data, id_customer):
    date = datetime_checker()
    with open(f'AccountDataChangeRecord.txt','a') as user_data_file:
        if kind_of_data == "type account" and new_data == "saving":
            user_data_file.write(f'{id_customer};ADMIN ({id_of_user}), change {kind_of_data} from current account to saving account {date}\n')
        elif kind_of_data == "type account" and new_data == "current":
            user_data_file.write(f'{id_customer};ADMIN ({id_of_user}), change {kind_of_data} from saving account to current account {date}\n')
        elif kind_of_data == "email":
            user_data_file.write(f'{id_customer};ADMIN ({id_of_user}), change {kind_of_data} from {old_data[5]} to {new_data} {date}\n')
        elif kind_of_data == "address":
            user_data_file.write(f'{id_customer};ADMIN ({id_of_user}), change {kind_of_data} from {old_data[6]} to {new_data} {date}\n')
        elif kind_of_data == "phone number":
            user_data_file.write(f'{id_customer};ADMIN ({id_of_user}), change {kind_of_data} from {old_data[7]} to {new_data} {date}\n')
        elif kind_of_data == "password":
            user_data_file.write(f'{id_customer};ADMIN ({id_of_user}), change {kind_of_data} from {old_data[1]} to {new_data} {date}\n')

def datetime_checker():
    import datetime as find_date
    now_date = find_date.datetime.now() #find the local date
    now_date = now_date.strftime('on %Y-%m-%d at %H:%M:%S') #formating the local date into a formated string, ex: on 2021-12-25 at 05:40:21
    return now_date

def account_checker_to_edit():
    while True:
        with open("AccountData.txt", "r") as account_list:
            acc_datas = account_list.readlines()
            id = input("\nInput customer account id: ")
            checker = 0
            for line in acc_datas:
                acc_line = line.replace("\n",":").split(":")
                if id == acc_line[0] and acc_line[2] == "customer":
                    checker = 1
                    break
                elif id == acc_line[0] and acc_line[2] != "customer":
                    checker = 2
                else:
                    pass
            if checker == 1:
                return id
            elif checker == 2:
                print("\nYou input a not customer ID, only allowed to edit customer account.")
            else:
                print("\nAccount's ID not found.")

def account_checker_updater(id):
    with open("AccountData.txt", "r") as account_list:
        acc_datas = account_list.readlines()
        index_line = -1
        for line in acc_datas:
            acc_line = line.replace("\n",":").split(":")
            index_line += 1
            if id == acc_line[0] and acc_line[2] == "customer":
                data_line_location = acc_line
                return data_line_location, index_line #returning the index and the data

def edit_customer_account_option_checker():
    while True:
        choice = input("Which one would you like to edit? (2-7): ")
        type_change = 0
        if choice == "1":
            print("\nSorry, but editing name are not allowed!\n")
            continue
        elif choice == "2":
            answer = "email"
        elif choice == "3":
            answer = "address"
        elif choice == "4":
            answer = "phone number"
        elif choice == "5":
            answer = "type account"
        elif choice == "6":
            answer = "password"
        elif choice == "7":
            answer = "exit"
        else:
            print("\nSorry, we dont have that option\n")
            continue
        return answer

def customer_function(acc_id):
    while True:
        customer_acc_menu()
        user_choice = str(input("Select your option (1-5): "))
        if user_choice == "1":
            deposit_money(acc_id)
        elif user_choice == "2":
            withdrawal_money(acc_id)
        elif user_choice == "3":
            transfer_money(acc_id)
        elif user_choice == "4":
            printing_customer_balance_report(acc_id)
        elif user_choice == "5":
            customer_report_option(acc_id)
        elif user_choice == "6":
            change_customer_password(acc_id)
        elif user_choice == "7":
            print("\n*Thankyou for your visit*")
            break
        else:
            print("\nSorry, we dont have that option")

def change_customer_password(id):
    print("\n" + "=" * 26)
    while True:
        data_location, index_of_line = account_checker_updater(id) #function for checking the data
        old_password = data_location[1]
        new_password = (input("New password: ")).strip()
        if new_password == "" or new_password == " ":
            print("You should not leave it empty!\n")
            continue
        else:
            confirm_password = (input("Confirm password:")).strip()
        if new_password == confirm_password:
            pass
        else:
            print("Sorry, try again\n")
            continue
        with open("AccountData.txt", "r") as data_file:
            data_file = data_file.readlines()
            data_file[index_of_line] = f'{data_location[0]}:{confirm_password}:{data_location[2]}:{data_location[3]}:{data_location[4]}:{data_location[5]}:{data_location[6]}:{data_location[7]}:{data_location[8]}' + "\n"
        with open("AccountData.txt", 'w') as data_write:
            data_write.writelines(data_file)
        write_records(id, old_password, confirm_password)
        print("\n" + "  ***Password Changed!***")
        break

def write_records(id, old_password, confirm_password):
    date = datetime_checker()
    with open("AccountDataChangeRecord.txt", "a") as data_file:
        data_file.write(f'{id};CUSTOMER ({id}), change password from {old_password} to {confirm_password} {date}\n')

def customer_report_option(id):
    print('\n' + "=" * 26)
    print("1. Print all customer balance report")
    print("2. Print specific date for customer balance report")
    print("=" * 26)
    while True:
        user_choice = input("Which one do you want to see? (1/2): ")
        if user_choice == "1":
            printing_customer_report_all(id)
            break
        elif user_choice == "2":
            checking_customer_report_specific(id)
            break
        else:
            print("Sorry, we dont have that option!\n")

def checking_customer_report_specific(id):
    while True:
        start_date = input("Start date (yyyy-mm-dd): ")
        end_date = input("End date (yyyy-mm-dd): ")
        checker = False
        try:
            start_date_list = start_date.split("-") #spliting the user input with -
            end_date_list = end_date.split("-")
            year_start, month_start, day_start = start_date_list #assigning the element inside list into 3 variables
            year_end, month_end, day_end = end_date_list
            year_start, month_start, day_start, year_end, month_end, day_end = int(year_start), int(month_start), int(day_start), int(year_end), int(month_end), int(day_end)
            month_with_31days = [1,3,5,7,8,10,12]
            month_with_30days = [4,5,9,11]
            year_start_check = str(year_start).zfill(4) #converting in case if user input uncomplete format, ex: 998 into 0998
            month_start_check = str(month_start).zfill(2)
            day_start_check = str(day_start).zfill(2)
            year_end_check = str(year_end).zfill(4)
            month_end_check = str(month_end).zfill(2)
            day_end_check = str(day_end).zfill(2)
            check_start = f'{year_start_check}-{month_start_check}-{day_start_check}' #create a format to compare if the date is exist.
            check_end = f'{year_end_check}-{month_end_check}-{day_end_check}'
            if check_start > check_end: #checking if the start input is lesser than end input
                print("Start date should be lesser than end date")
                continue
            if len(start_date_list) == 3 and (month_start >= 1 and month_start <= 12):
                if month_start in month_with_30days and (day_start >= 1 and day_start <= 30):
                    checker = True
                elif month_start in month_with_31days and (day_start >= 1 and day_start <= 31):
                    checker = True
                elif month_start == 2 and (year_start % 4 == 0 and year_start % 100 != 0) and (day_start >= 1 and day_start <= 29):
                    checker = True
                elif month_start == 2 and (year_start % 4 == 0 and year_start % 400 == 0) and (day_start >= 1 and day_start <= 29):
                    checker = True
                elif month_start == 2 and (day_start >= 1 and day_start <= 28):
                    checker = True
                else:
                    x = 1/0
                if checker == True and (len(end_date_list) == 3 and (month_end >= 1 and month_end <= 12)):
                    if month_end in month_with_30days and (day_end >= 1 and day_end <= 30):
                        pass
                    elif month_end in month_with_31days and (day_end >= 1 and day_end <= 31):
                        pass
                    elif month_end == 2 and (year_end % 4 == 0 and year_end % 100 != 0) and (day_end >= 1 and day_end <= 29):
                        pass
                    elif month_end == 2 and (year_end % 4 == 0 and year_end % 400 == 0) and (day_end >= 1 and day_end <= 29):
                        pass
                    elif month_end == 2 and (day_end >= 1 and day_end <= 28):
                        pass
                    else:
                        x = 1/0
                else:
                    x = 1/0
            else:
                x = 1/0
        except:
            print("Sorry, but the requirement format are not fulfilled")
            continue
        date = year_start, month_start, day_start, year_end, month_end, day_end
        date = list(date)
        printing_customer_report_specific(id, date)
        break

def printing_customer_report_specific(id, date):
    with open("AccountBalanceRecord.txt", "r") as record_file:
        record_file = record_file.readlines()
        year_start, month_start, day_start, year_end, month_end, day_end = date
        year_start = str(year_start).zfill(4)
        month_start = str(month_start).zfill(2)
        day_start = str(day_start).zfill(2)
        year_end = str(year_end).zfill(4)
        month_end = str(month_start).zfill(2)
        day_end = str(day_end).zfill(2)
        user_date_start = f'{year_start}-{month_start}-{day_start}'
        user_date_end = f'{year_end}-{month_end}-{day_end}'
        check = 0
        print("\n" + "=" * 26)
        for each_line in record_file:
            the_date = each_line.split()
            the_record = each_line.split(";")
            show_record = the_record[1]
            if the_record[0] == id:
                if the_date[1] == "DEPOSIT" or the_date[1] == "WITHDRAW": #this "if" declared because in txt file, the location of the date is different.
                    date_of_data = the_date[11]
                elif the_date[1] == "TRANSFER":
                    date_of_data = the_date[13]
                if user_date_start <= date_of_data and user_date_end >= date_of_data:
                    print(show_record, end="")
                    check = 1
            else:
                continue
        if check == 0:
            print("No record found!")
        print("=" * 26)
        input("Type anything to continue: ")

def printing_customer_report_all(id):
    checker = 0
    with open(f"AccountBalanceRecord.txt", "r") as data_report:
        data_report = data_report.readlines()
        print("\n" + "=" * 26)
        for each_line in data_report:
            each_line = each_line.split(";")
            if each_line[0] == id:
                print(each_line[1],end='')
                checker = 1
        if checker == 0:
            print("No record found!")
        print("=" * 26)
        input("Type anything to continue: ")

def transfer_money(giver_id):
    with open("AccountData.txt","r") as account_data:
        account_list = account_data.readlines()
        data_location_giver, index_of_line_giver = account_checker_updater(giver_id)
        transfer_destination = transfered_acc_checker(account_list, giver_id) #input and checking if account are exist.
        data_location_receiver, index_of_line_receiver = account_checker_updater(transfer_destination)
        perform_transfer_and_balance_checker(data_location_giver, data_location_receiver, index_of_line_giver, index_of_line_receiver)

def perform_transfer_and_balance_checker(data_of_giver, data_of_receiver, index_of_line_giver, index_of_line_receiver):
    while True:
        now_currency_giver_acc = float(data_of_giver[8])
        now_currency_receiver_acc = float(data_of_receiver[8])
        if now_currency_giver_acc >= 100.0 and data_of_giver[3] == "saving":
            pass
        elif now_currency_giver_acc >= 500.0 and data_of_giver[3] == "current":
            pass
        else:
            print("\nSorry, your minimal balance requirement are not fulfilled")
            return
        while True:
            total_transfer = input("How many would you like to transfer? (x.xx): ")
            try:
                total_transfer = float(total_transfer)
                break
            except:
                print("\nYou are suppose to fill it with numbers")
        if total_transfer < 0.0:
            print("\nYou can't transfer with negative numbers.")
            continue
        elif total_transfer == 0.0:
            print("\nYou can't transfer 0 amount of money.")
            continue

        balance_update_giver_acc = now_currency_giver_acc - total_transfer
        balance_update_receiver_acc = now_currency_receiver_acc + total_transfer
        with open("AccountData.txt","r") as account_file:
            list_of_lines = account_file.readlines()
            if (data_of_giver[3] == "saving" and now_currency_giver_acc > 100.0) and balance_update_giver_acc >= 100.0:
                list_of_lines[index_of_line_giver] = f'{data_of_giver[0]}:{data_of_giver[1]}:{data_of_giver[2]}:{data_of_giver[3]}:{data_of_giver[4]}:{data_of_giver[5]}:{data_of_giver[6]}:{data_of_giver[7]}:{balance_update_giver_acc}' + f'\n'
                list_of_lines[index_of_line_receiver] = f'{data_of_receiver[0]}:{data_of_receiver[1]}:{data_of_receiver[2]}:{data_of_receiver[3]}:{data_of_receiver[4]}:{data_of_receiver[5]}:{data_of_receiver[6]}:{data_of_receiver[7]}:{balance_update_receiver_acc}' + f'\n'
                break
            elif (data_of_giver[3] == "current" and now_currency_giver_acc > 500.0) and balance_update_giver_acc >= 500.0:
                list_of_lines[index_of_line_giver] = f'{data_of_giver[0]}:{data_of_giver[1]}:{data_of_giver[2]}:{data_of_giver[3]}:{data_of_giver[4]}:{data_of_giver[5]}:{data_of_giver[6]}:{data_of_giver[7]}:{balance_update_giver_acc}' + f'\n'
                list_of_lines[index_of_line_receiver] = f'{data_of_receiver[0]}:{data_of_receiver[1]}:{data_of_receiver[2]}:{data_of_receiver[3]}:{data_of_receiver[4]}:{data_of_receiver[5]}:{data_of_receiver[6]}:{data_of_receiver[7]}:{balance_update_receiver_acc}' + f'\n'
                break
            else:
                print("\nSorry, but you are not allowed transfer any money, \nsince your requirement to transfer not met.")
                continue
    with open("AccountData.txt","w") as account_file_write:
        account_file_write.writelines(list_of_lines)
    write_balance_record_transfer(total_transfer, now_currency_giver_acc, now_currency_receiver_acc, balance_update_giver_acc, balance_update_receiver_acc, data_of_giver, data_of_receiver)
    print("\n" + ("=" * 26) + "\n    transfer success!\n" + ("=" * 26))

def write_balance_record_transfer(total, last_balance_of_giver, last_balance_of_receiver, new_balance_of_giver, new_balance_of_receiver, data_of_giver, data_of_receiver):
    date = datetime_checker()
    acc_giver = data_of_giver[0]
    acc_receiver = data_of_receiver[0]
    with open(f'AccountBalanceRecord.txt','a') as user_data_file:
        user_data_file.write(f'{acc_giver};total TRANSFER of RM{total} to {acc_receiver}, balance updated from {last_balance_of_giver} to {new_balance_of_giver} {date}\n')
        user_data_file.write(f'{acc_receiver};total TRANSFER of RM{total} from {acc_giver}, balance updated from {last_balance_of_receiver} to {new_balance_of_receiver} {date}\n')

def transfered_acc_checker(account_data_opened, id_of_giver):
    while True:
        checker = 0
        transfer_destination = input("\nto whom would you like to transfer,\nplease enter the account ID: ")
        for line in account_data_opened:
            each_line = line.replace("/n",":").split(":")
            if transfer_destination == id_of_giver:
                checker = 3
            elif transfer_destination == each_line[0] and each_line[2] == "customer":
                checker = 1
                break
            elif transfer_destination == each_line[0] and each_line[2] != "customer":
                checker = 2
            else:
                pass
        if checker == 1:
            return transfer_destination
        elif checker == 2:
            print("\nYou input a not customer ID, only allowed to transfer to customer account.")
        elif checker == 3:
            print("\nPlease dont put your own account ID!")
        else:
            print("\nAccount's ID not found.")

def withdrawal_money(id):
    print("")
    action_type = "withdraw"
    data_location, index_of_line = account_checker_updater(id)
    if data_location[3] == "current":
        if float(data_location[8]) > 500:
            pass
        else:
            print("Sorry, you are not allowed to do this transaction,\nsince your require minimal balance not fulfilled")
            return
    elif data_location[3] == "saving":
        if float(data_location[8]) > 100:
            pass
        else:
            print("Sorry, you are not allowed to do this transaction,\nsince your require minimal balance not fulfilled")
            return
    while True:
        while True:
            total_withdrawal = input("How many would you like to withdraw? (x.xx): ")
            try:
                total_withdrawal = float(total_withdrawal)
                break
            except:
                print("\nYou are suppose to fill it with numbers")
        if total_withdrawal < 0.0:
            print("\nYou can't withdraw with negative numbers.")
            continue
        elif total_withdrawal == 0.0:
            print("\nYou can't withdraw 0 amount of money.")
            continue
        now_currency = float(data_location[8])
        balance_update = now_currency - total_withdrawal
        with open("AccountData.txt","r") as account_file:
            list_of_lines = account_file.readlines()
            if (data_location[3] == "saving" and now_currency > 100.0) and balance_update >= 100.0:
                list_of_lines[index_of_line] = f'{data_location[0]}:{data_location[1]}:{data_location[2]}:{data_location[3]}:{data_location[4]}:{data_location[5]}:{data_location[6]}:{data_location[7]}:{balance_update}' + f'\n'
                break
            elif (data_location[3] == "current" and now_currency > 500.0) and balance_update >= 500.0:
                list_of_lines[index_of_line] = f'{data_location[0]}:{data_location[1]}:{data_location[2]}:{data_location[3]}:{data_location[4]}:{data_location[5]}:{data_location[6]}:{data_location[7]}:{balance_update}' + f'\n'
                break
            else:
                print("\nSorry, but you are not allowed withdraw with that amount of money, \nif you do, your requirement minimal balance to withdraw will not met.")
                return
    with open("AccountData.txt","w") as account_file_write:
        account_file_write.writelines(list_of_lines)
    print("\n" + ("=" * 26) + "\n   withdrawal success!\n" + ("=" * 26))
    write_balance_record(total_withdrawal, now_currency, balance_update, id, action_type)

def printing_customer_balance_report(id):
    with open("AccountData.txt", "r") as data_record:
        data_record = data_record.readlines()
        for each_line in data_record:
            each_line = each_line.split(":")
            if each_line[0] == id:
                data_to_check = each_line[8]
                print("\n " + "=" * 23 + "\n Current Balance: RM" + data_to_check + " " + "=" * 23)
                break
        input("Type anything to continue: ")

def deposit_money(this_user_id):
    print("")
    action_type = "deposit"
    data_location, index_of_line = account_checker_updater(this_user_id)
    while True:
        total_deposit = input("How many would you like to deposit? (x.xx): ")
        try:
            total_deposit = float(total_deposit)
            break
        except:
            print("\nYou are suppose to fill it with digits")
    balance_now = float(data_location[8])
    updated_balance = balance_now + total_deposit
    with open("AccountData.txt","r") as account_file:
        list_of_lines = account_file.readlines()
        if data_location[3] == "saving" or data_location[3] == "current":
            list_of_lines[index_of_line] = f'{data_location[0]}:{data_location[1]}:{data_location[2]}:{data_location[3]}:{data_location[4]}:{data_location[5]}:{data_location[6]}:{data_location[7]}:{updated_balance}' + f"\n"
    with open("AccountData.txt", "w") as f:
        f.writelines(list_of_lines)
    print(("=" * 26) + "\n     Balance updated!\n" + ("=" * 26))
    write_balance_record(total_deposit, balance_now, updated_balance, this_user_id, action_type)

def write_balance_record(total, last_balance, new_balance, customer_id, perform):
    date = datetime_checker()
    with open(f'AccountBalanceRecord.txt','a') as user_data_file:
        if perform == "deposit":
            user_data_file.write(f'{customer_id};total DEPOSIT of RM{total}, balance updated from {last_balance} to {new_balance} {date}\n')
        elif perform == "withdraw":
            user_data_file.write(f'{customer_id};total WITHDRAW of RM{total}, balance updated from {last_balance} to {new_balance} {date}\n')

def customer_acc_menu():
    print("\n" + (" " * 6) + "Customer Menu")
    print("=" * 26)
    print("1. Deposit")
    print("2. Withdrawal")
    print("3. Transfer")
    print("4. Balance Enquiry")
    print("5. Account Statement")
    print("6. Change Password")
    print("7. Exit")
    print("=" * 26)
    print("How can we help you today?")

start_program()