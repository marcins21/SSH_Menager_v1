import os
import json
from server import *


JSON_FILE = "servers.json"
JSON_FILEPATH = "./servers.json"

#Reading all Json File
with open(JSON_FILE,"r") as f:
    json_data = json.load(f)


#Checking if file exists
def does_file_exists(filename_path:str) -> bool:
    return os.path.exists(filename_path)


#Info message
def menu_init_message():
    print("""n - Add new Server\nd - Delete Server \ns - Server Info """)

#Adding new server 'n' - option
def menu_add_new_server():
    #Clearing Board before interactive menu
    os.system("clear")
    server_name = input("Server name: ")
    username = input("Username: ")
    password = input("Password: ")
    ip = input("Ip: ")

    #Json Adding new serwer
    data = {f"{server_name}":{"username":f"{username}","password":f"{password}","ip":f"{ip}"}}
    json_data["servers"].append(data)

#Main function
def menu_main():
    #Info message
    menu_init_message()
    while True:
        #Menu
        command = input("command: ").lower()
        if command == 'n':
            menu_add_new_server()
            write = input("Write? Y/n").lower()

            #Write Data option
            if write == '' or write == 'y':
                break

    #Writing Data to Json
    if does_file_exists(JSON_FILEPATH):
        with open(JSON_FILE,"w") as file:
            json.dump(json_data,file,indent=3)
            file.close()


menu_main()