#!python3
'''
The program will ask the user for a username and a password
If the user name and password are correct, the program will
exit and say "Access Granted".
If they are not correct, the program will say "Access Denied".
There will be a maximum of 3 guesses allowed
'''

expUser = "systemadmin"
expPass = "master"

User = input("welcome, please enter your User and password, User: ")
for i in range(1,4):
    if User == expUser:
        Pass = input(f"{expUser} is Correct, enter password: ")
        for i in range(1,4):
            if Pass == expPass:
                print(f"{expUser} and {expPass}")
                break
            else:
                print("get out of my pc :[")
        break        
    else:
        print("get out of my pc :[")