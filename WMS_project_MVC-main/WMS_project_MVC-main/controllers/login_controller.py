from business_logic.login_bl import LoginModel
from views.login_view import LoginView


class LoginController:
    def __init__(self, parent):
        self.parent = parent

        self.view = LoginView(parent)
        self.model = LoginModel(parent)

    def show_login_window(self):
        self.view.setup()
        self.view.btn_login.config(command=self.user_check)

    def user_check(self):
        self.model.user_check(self.view)
