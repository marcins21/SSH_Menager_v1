#SERVER CLASS


class Server:
    def __init__(self,server_name="",username="",password="",ip=""):
        self.username = username
        self.password = password
        self.ip = ip
        self.server_name = server_name

    #Setters
    def set_username(self,username):
        self.username = username
    def set_password(self,password):
        self.password = password
    def set_ip(self,ip):
        self.ip = ip
    def set_server_name(self,name):
        self.server_name = name

    #Getters
    def get_username(self):
        return self.username
    def get_password(self):
        return self.password
    def get_ip(self):
        return self.ip
    def get_server_name(self):
        return self.server_name