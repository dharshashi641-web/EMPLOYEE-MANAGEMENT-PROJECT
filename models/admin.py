class Admin:

    def __init__(self, username, password):

        self.username = username
        self.__password = password

    def get_password(self):
        return self.__password