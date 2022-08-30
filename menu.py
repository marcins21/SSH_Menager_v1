import os
import json
from server import *
 
 
#VARS
JSON_FILE = "servers.json"
JSON_FILEPATH = "./servers.json"
server_objects = []
server_names = []

#Reading all Json File
with open(JSON_FILE,"r") as f:
    json_data = json.load(f)

#Checking if file exists
def does_file_exists(filename_path:str) -> bool:
    return os.path.exists(filename_path)

#Info message
def menu_init_message():
    print("""n - Add new Server\nd - Delete Server \ns - Server Info\ne - exit """)

#Loading all server names to a list
def load_server_names(data):
    for record in data["servers"]:
        for key in record.keys():
            server_names.append(key)

#Adding new server 'n' -  option
def menu_add_new_server():
    #Clearing Board before interactive menu
    os.system("clear")
    server_name = input("Server name: ")
    username = input("Username: ")
    password = input("Password: ")
    ip = input("Ip: ")

    #Creating server object
    server_name = Server(server_name,username,password,ip)
    server_objects.append(server_name)

    #Adding just server name to antoher list
    server_names.append(server_name.get_server_name())

    #Json Adding new serwer
    data = {f"{server_name.get_server_name()}":{"username":f"{server_name.get_username()}",
                                                "password":f"{server_name.get_password()}",
                                                "ip":f"{server_name.get_ip()}"}}
    #Addting new server to loaded json data
    json_data["servers"].append(data)


#Deleting server 'd' - option
def menu_delete_server():
    # ...
    pass

#Showing server info 's' - option
def menu_show_server_info():
    # ...
    pass


#Main function
def menu_main():
    #Info message
    menu_init_message()
    while True:
        #Menu
        command = input("command: ").lower()

        #Checking Correct user input
        if command == 'n' or command == 's' or command == 'd' or command == 'e':

            #Server Options!
            #Add Option
            if command == 'n':
                menu_add_new_server()
                write = input("Write? Y/n").lower()

                #Write Data option
                if write == '' or write == 'y':
                    break

            #Show option
            elif command == 's':
                # ...
                print("\nSHOW option\nWorking on this option ... ")

            #Delete option
            elif command == 'd':
                print("\nDELETE option\nWorking on this option ... ")
                # ...

            #Exit option
            elif command == 'e':
                print("\nBye Bye!")
                break

        else:
            print("\nYou Entered Wrong option ! ")

    #Dumping json data
    if does_file_exists(JSON_FILEPATH):
        with open(JSON_FILE,"w") as file:
            json.dump(json_data,file,indent=3)
            file.close()

    #loading servers
    load_server_names(json_data)

    # Showing all server names
    counter = 1
    for name in server_names[1:len(server_names)]:
        print(counter, " ", name)
        counter += 1


#Call this function from `app.py` - main python file -  "runner"
#menu_main()
