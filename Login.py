import csv

user_pass_list = []
quarantine_list = []

with open('logins.csv', newline = '') as infofile:
    login_reader = csv.DictReader(infofile)
    for row in login_reader:
        user_pass_list.append((row['username'], row['password']))

with open('quarantine.csv', newline = '') as quarfile:
    login_reader = csv.DictReader(quarfile)
    for row in login_reader:
        quarantine_list.append((row['username'], row['password']))
    
userinput = input("Username: ")
usercounter = 0
quarantinecounter = 0
for tuple in user_pass_list:
    if userinput == tuple[0]:
        while True:
            passinput = input("Password: ")
            if passinput == tuple[1]:
                print("Logged in!")
                break
            else:
                print("Wrong Password!")
                quarantinecounter +=1
                if quarantinecounter > 5:
                    print("Your account has been quarantined because there were too many login attempts.")
                    break
    if userinput != tuple[0]:
        usercounter += 1

if usercounter == len(user_pass_list):
    print("Invalid Username!")
    question = input("Would you like to create an account?\n")
    question_lower = question.lower()
    if question_lower == "yes":
        while True:
            new_user = input("New Username: ")
            overlap_counter = 0
            for tuple in user_pass_list:
                if new_user == tuple[0]:
                    overlap_counter +=1
            if overlap_counter == 1:
                print("This username already exists. Come up with another.")
            elif overlap_counter == 0:
                break
        while True:
            new_password = input("New Password: ")
            conf_password = input("Confirm Password: ")
            if new_password == conf_password:
                print("Information saved! You may now login.")
                break
            else:
                print("Sorry! Those two passwords weren't the same. Try again.")

        with open('logins.csv', 'a') as infofile:
            infofile.write("\n" + new_user + "," + new_password)
    elif question_lower == "no":
        print("Ok, see ya!")


        