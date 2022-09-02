import os
import json
from server import *
import subprocess
 
 
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
    print("""n - Add new Server\nd - Delete Server \ns - Server Info\ne - LOAD """)

#Loading all server names to a list
def load_server_names(data):
    server_names.clear()
    server_objects.clear()
    for record in data["servers"]:
        server_objects.append(record)
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


    #Json Adding new serwer
    data = {f"{server_name.get_server_name()}":{"username":f"{server_name.get_username()}",
                                                "password":f"{server_name.get_password()}",
                                                "ip":f"{server_name.get_ip()}"}}
    #Addting new server to loaded json data
    json_data["servers"].append(data)

# Showing all server names using server_names list
def menu_show_all_servers(server_list):
    counter = 1
    for name in server_list[1:len(server_list)]:
        print(counter, " ", name)
        counter += 1
    print("\n")


#Connecting into server 'c' - option
def menu_get_into_server(user_choice):
    if user_choice > 0 and user_choice <= len(server_names):
        print("\nYour choice: ",server_names[user_choice])
        username = server_objects[user_choice][server_names[user_choice]]["username"]
        password = server_objects[user_choice][server_names[user_choice]]["password"]
        ip = server_objects[user_choice][server_names[user_choice]]["ip"]

        subprocess.call(f"./bash_script.sh {username} {password} {ip}", shell=True)
    else:
        print("You Typed Wrong Server ID")

#Showing specific server info 's' - option
def menu_show_server_info(user_choice):
    if user_choice > 0 and user_choice <= len(server_names):
        server_info = {}
        server_name = server_names[user_choice]
        username = server_objects[user_choice][server_names[user_choice]]["username"]
        password = server_objects[user_choice][server_names[user_choice]]["password"]
        ip = server_objects[user_choice][server_names[user_choice]]["ip"]
        server_info["Name"] = server_name
        server_info["Username"] = username
        server_info["Password"] = password
        server_info["Ip"] = ip
        print()
        for k,v in server_info.items():
            print(k," ",v)
        print()
    else:
        print("You Typed Wrong Server ID")


#Deleting server 'd' - option
def menu_delete_server():
    # ...
    pass




#Main function
def menu_main():
    #Info message
    menu_init_message()
    while True:
        #Menu
        #Loading all server names

        command = input("command: ").lower()

        #Checking Correct user input
        if command == 'n' or command == 's' or command == 'd' or command == 'e' or command == 'c':
            load_server_names(json_data)

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
                user_server_number_input1 = int(input(": "))
                menu_show_server_info(user_server_number_input1)
                # # ...
                # print("\nSHOW option\nWorking on this option ... ")

            #Delete option
            elif command == 'd':
                print("\nDELETE option\nWorking on this option ... ")
                # ...

            #Load option
            elif command == 'e':
                os.system("clear")
                print("\nListing ... ")

                # loading servers
                load_server_names(json_data)
                # Showing all servers
                menu_show_all_servers(server_names)
                break

            elif command == "c":
                user_server_number_input = int(input(": "))
                menu_get_into_server(user_server_number_input)
        else:
            print("\nYou Entered Wrong option ! ")

    #Dumping json data
    if does_file_exists(JSON_FILEPATH):
        with open(JSON_FILE,"w") as file:
            json.dump(json_data,file,indent=3)
            file.close()



#Call this function from `app.py` - main python file -  "runner"
#menu_main()
