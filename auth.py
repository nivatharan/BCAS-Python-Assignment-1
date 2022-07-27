import os
import task101


def authentication():
    os.system("cls")
    print("""
    ======Login======
    """)
    UserName = input("Enter User Name: ")
    Password = input("Enter Password: ")

    with open("C:/Users/Nivan/Desktop/Python ESOFT/name.txt", "r") as F:
        Line = F.readlines()

    if UserName == (Line[0]).rstrip():
        if Password == (Line[1]).rstrip():
            print("\nWelcome To the Dashboard\n")
            D = task101.Task()
            D
        else:
            print("\nEnter the Valid Password\n")
    else:
        print("\nEnter the correct User Name\n")


authentication()
