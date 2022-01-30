import random
from datetime import datetime
import sys
import time
import os
from tkinter import TRUE

start_time = datetime.today().strftime('%H:%M')
passwordFile = open("password.txt", 'r') # Open password file
password = passwordFile.readline()

def check_password_tried(password):
    check = False;
    tried_passwordsFile = open("tried_passwords.txt", 'r', encoding="utf8")
    tried_passwords = tried_passwordsFile.readlines()
    for line in tried_passwords:
        if line == password:
            check = True;
    tried_passwordsFile.close()
    return check;

def save_password_tried(password):
    tried_passwordsFile = open("tried_passwords.txt", 'a+', encoding="utf8")
    tried_passwordsFile.write(password + "\n")
    tried_passwordsFile.close()

def generate_random_password(size):
    random_password = ""
    for i in range(size):
        random_password += random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789")
    if(check_password_tried(random_password) == False):
        save_password_tried(random_password)
        return random_password
    else:
        generate_random_password(size)

def verify_password(password, random_password):
    if password == random_password:
        return True
    else:
        check_password_tried(password)
        return False

size = len(password)
random_password = "abcdefghijklmnopqrstuvwxyz"
trieds = 0

print("Started at: " + start_time)
print("the password in the file is: " + password)
while True:
    trieds = trieds + 1
    if verify_password(password, random_password) == False:
        random_password = generate_random_password(size)
    else:
        print("Congratulations! You cracked the password!")
        print("the password is: " + password)
        print("the random password is: " + random_password)
        print("the number of tries it took to crack the password is: " + str(trieds))
        passwordFile.close()
        print("Do you want to clean the file 'tried_passwords.txt' ? (y/n)")
        clean_file = input('> ')
        if clean_file == "y":
            with open("tried_passwords.txt",'w') as f:
                clean_file.close()
        break