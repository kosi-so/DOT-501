# Import relevant Libraries 
import csv
import pandas as pd
from collections import defaultdict

users = {}              # The class object of the created users can be found in this dictionary
users_cred = {}         # Houses the username and password of users
users_list = []         # A list of users
admin_cred = {"kosi": "security"}         # Username and Password of the Administrator
admin_list = ["kosi"]        # A list of Administrators
superusers = {}         # Class Object of authorised Suoerusers is contained in this dictionary
superusers_cred = {}    # This Dictionary contains the username and password of Superusers
superusers_list = []    # A list of Superusers 




class Client():   # Create Superclass that can perform all the functions

    def __init__ (self, username):
        self.username = username
        self.access = ['read', 'write', 'create user', 'display user', 'create superuser']

    def read_data (self):

        if 'read' in self.access:
            data = pd.read_csv("sbd.csv")     # Converts the data from CSV file to a table.
            print(data)

        else:
            return "You do not have the adequate privilege to read data"  
        
    def write_data(self):
  

        if "write" in self.access:

            segment = input("What is the Product's Segment: \n")
            country = input("What Country is the Product Produced in: \n")
            product = input("What is the Name of the Product: \n")

            data = pd.read_csv("sbd.csv")                   # Converts the data frrom a CSV file to a table    
            data.loc[len(data.index)] = [segment, country, product] # Adds new information to the table
            data.to_csv("client_data.csv")
            print(data)

            return "\n Data Successfully Added \n"

        else:
            return "You do not have the adequate privilege to write data"

    def create_user(self):
    
        if "create user" in self.access:
            global users_cred, users
            username = input("Enter new username\n")
            password = input("Enter password\n")

            users_list.append(username)         # Adds user to list of users
            user = User(username, password)               # Creates class object for user
            users[username] = user              # Stores the class object in the "users" dictionary
            users_cred[username] = password     # Saves the username and password of the new user
            return "New User Created"
            
        else:
            return "You do not have the adequate privilege to create new users"  

    def display_users(self):
        """ Shows list of users """

        if "display users" in self.access:
            return users_list

        else:

            return "You do not have adequate privilege to perform this task"

    def create_superuser (self):
       
        if "create superuser" in self.access:
            global superusers_cred, superusers
            username = input("Enter new username\n")
            password = input("Enter password \n")

            superusers_list.append(username)            # Adds superuser to list of superusers
            user = SuperUser(username, password)        # Creates class object for superuser
            superusers[username] = user                 # Stores the class object in the "superusers" dictionary
            superusers_cred[username] = password        # Saves the username and password of the new user
            print("New Superuser Created")
            
        else:
            return "You do not have the adequate privilege to create Superuser"



class User(Client):

    def __init__ (self, username, password):
        super().__init__(username)
        self.password = password
        self.access = ["read"]

class Guest(Client):

    def __init__(self, username):
        super().__init__(username) 
        self.access = [] 

class SuperUser(Client):

    def __init__ (self, username, password):
        super().__init__(username)
        self.password = password
        self.access = ["read", "write", "create user", "display users"]

class Admin(Client):

    def __init__ (self, username, password):
        super().__init__(username)
        self.password = password
        self.access = ["read", "write", "create superuser"]


def main():
    while True:
        client = input("How would you like to login?: \n (1) User \n (2) Superuser \n (3) Administrator \n (4) Guest \n")
        username = input ("Enter your Username \n")

        if client == "1":
            if username in users_list:    
                password = input("Please enter your password\n")

                if password == users_cred[username]:
                    
                    user = users[username]
                    print ("You have logged in as a User \n")
                    while True:

                        d = defaultdict(lambda: "This option is not available")

                        d["1"], d["2"], d["3"], d["4"], d["5"] = user.read_data, user.write_data, user.create_user, user.display_users, user.create_superuser
                        
                        Entry = input("What do you want to do?:\n (1) read Data\n (2) write data \n (3) Create User \n (4) Show Users \n (5) Create Superuser \n (6) Log out \n") #it store input data in Entry variable
                        if Entry == "6":
                            break
                        print(d[Entry]())

        

                else:
                    print("\n Incorrect Username or Password \n")
            else:
                print("User does not exist")

        elif client == "2":
            if username in superusers_list:
                password = input("Please enter your password\n")

                if password == superusers_cred[username]:

                    user = SuperUser(username, password)
                    print ("You have logged in as a Superuser \n")
                    while True:
                        d = defaultdict(lambda: "This option is not available")

                        d["1"], d["2"], d["3"], d["4"], d["5"] = user.read_data, user.write_data, user.create_user, user.display_users, user.create_superuser
                        
                        Entry = input("What do you want to do?:\n (1) read Data\n (2) write data \n (3) Create User \n (4) Show Users \n (5) Create Superuser \n (6) Log out \n") #it store input data in Entry variable
                        if Entry == "6":
                            break
                        print(d[Entry]())

                else:
                    print("Incorrect Username or Password")

            else:
                print("Superuser does not exist")

        elif client == "3":
            if username in admin_list:
                password = input("Please enter your password\n")

                if password == admin_cred[username]:

                    user = Admin(username, password)
                    print ("You have logged in as an Administrator \n")
                    while True:
                        d = defaultdict(lambda: "This option is not available")

                        d["1"], d["2"], d["3"], d["4"], d["5"] = user.read_data, user.write_data, user.create_user, user.display_users, user.create_superuser
                        
                        Entry = input("What do you want to do?:\n (1) read Data\n (2) write data \n (3) Create User \n (4) Show Users \n (5) Create Superuser \n (6) Log out \n") #it store input data in Entry variable
                        if Entry == "6":
                            break
                        print(d[Entry]())
                    
                else:
                    print("Incorrect Username or Password")
            
            else:
                print ("Admin does not exist")

        elif client == "4":
            user = Guest(username)
            print ("You have logged in as a Guest \n")
            while True:
                        d = defaultdict(lambda: "This option is not available")

                        d["1"], d["2"], d["3"], d["4"], d["5"] = user.read_data, user.write_data, user.create_user, user.display_users, user.create_superuser
                        
                        Entry = input("What do you want to do?:\n (1) read Data\n (2) write data \n (3) Create User \n (4) Show Users \n (5) Create Superuser \n (6) Log out \n") #it store input data in Entry variable
                        if Entry == "6":
                            break
                        print(d[Entry]())
        else:
            pass
if __name__ == "__main__":
    main()
