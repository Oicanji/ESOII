from time import sleep
import classes.user as user
import classes.guest as guest
import os

#create var to clear terminal
clear = 'cls' if os.name == 'nt' else 'clear'

logins = []
comic = []
page = []
grid = []
form = []
image = []

def submitMenu():
    while True:
        os.system(clear)
        print("0. Back")
        print("1. Submit Comic")
        print("2. Submit Page")
        print("3. Submit Grid")
        print("4. Submit Form")
        print("5. Submit Image")
        choice = input("Enter your choice: ")
        if choice == '0':
            userMenu()

def deleteMenu():
    while True:
        os.system(clear)
        print("0. Back")
        print("1. Delete Comic")
        print("2. Delete Page")
        print("3. Delete Grid")
        print("4. Delete Form")
        print("5. Delete Image")
        choice = input("Enter your choice: ")
        if choice == '0':
            userMenu()

def viewMenu():
    while True:
        os.system(clear)
        print("0. Back")
        print("1. View Comic")
        print("2. View Page")
        print("3. View Grid")
        print("4. View Form")
        print("5. View Image")
        choice = input("Enter your choice: ")
        if choice == '0':
            userMenu()

def userMenu():
    #menu for user
    while True:
        os.system(clear)
        print("0. Poweroff")
        print("1. Logout")
        print("2. Submit")
        print("3. Delete")
        print("4. View")

        choice = input("Enter your choice: ")
        if choice == '1':
            guestMenu()
        elif choice == '2':
            submitMenu()
        elif choice == '3':
            deleteMenu()
        elif choice == '4':
            viewMenu()
        elif choice == '0':
            print("\033[1;31mPoweroff System\033[1;m")
            break
        else:
            print("Invalid choice")
def guestMenu():
    #menu for guest
    while True:
        os.system(clear)
        print("0. Poweroff")
        print("1. Login")
        print("2. Register")
        choice = input("Enter your choice: ")
        if choice == '1':
            guest.login(logins)
            sleep(2)

        elif choice == '2':
            guest.register()
        elif choice == '0':
            print("\033[1;31mPoweroff System\033[1;m")
            break
        else:
            print("Invalid choice")

def main():
    #create guest
    quest = guest.Guest()
    guestMenu()
