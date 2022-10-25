from hashlib import new
from time import sleep
import classes.user as user
import classes.guest as guest
import classes.comic as comic
import classes.page as page
import classes.grid as grid
import classes.form as form
import classes.image as image

import os

#create var to clear terminal
clear = 'cls' if os.name == 'nt' else 'clear'

logins = []
comic_list = []
page_list = []
grid_list = []
form_list = []
image_list = []

id = 0

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
            break
        elif choice == '1':
            named = input("Enter name: ")
            new_comic = comic.Comic(named, id)
            
        elif choice == '2':
            new_page = page.Page()
            new_page.create()
            page_list.append(new_page)
        elif choice == '3':
            new_grid = grid.Grid()
            new_grid.create(form_list)
            grid_list.append(new_grid)
        elif choice == '4':
            new_form = form.Form()
            new_form.create(image_list)
            form_list.append(new_form)
        elif choice == '5':
            new_image = image.Image(input("Enter image url: "))
            image_list.append(new_image)


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
            break

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
            break

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
    #create guest
    new_quest = guest.Guest()
    #menu for guest
    while True:
        os.system(clear)
        print("0. Poweroff")
        print("1. Login")
        print("2. Register")
        choice = input("Enter your choice: ")
        if choice == '1':
            the_name = input("Enter your name: ")
            the_password = input("Enter your password: ")
            i=0
            while i < len(logins):
                if logins[i].getName() == the_name:
                    if logins[i].auth(the_password):
                        print("Login successful")
                        id = i
                        userMenu()
                        break
                    else:
                        print("Login failed")
                        break
                i+=1
        elif choice == '2':
            token_session = new_quest.getSession()
            new_user = user.User(token_session)
            new_user.setName(input("Enter your name: "))
            new_user.saltPassword(input("Enter your password: "))
            logins.append(new_user)
        elif choice == '0':
            print("\033[1;31mPoweroff System\033[1;m")
            break
        else:
            print("Invalid choice")

def main():
    guestMenu()
