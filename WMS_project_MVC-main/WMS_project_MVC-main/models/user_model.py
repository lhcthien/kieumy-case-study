class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role


class Administrator(User):
    def __init__(self, username, password, role, code):
        super().__init__(username, password,role)
        self.code = code

class Client(User):
    def __init__(self, username, password, role, code):
        super().__init__(username, password,role)
        self.code = code

class WarehouseWorker(User):
    def __init__(self, username, password, role, code):
        super().__init__(username, password,role)
        self.code = code
