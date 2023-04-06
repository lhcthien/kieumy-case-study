from tkinter import messagebox, END
from tkinter import *

from controllers.admin_controller import AdminController
from controllers.client_controller import ClientController
from controllers.ww_controller import WwController
from data_files.DbContext import DbContext
from models.user_model import *


class LoginModel:
    def __init__(self, parent):
        self.parent = parent
        # self.ctrl = ctrl
        # self.adm_ctrl = AdminController(parent)

    def user_check(self, view):
        def clear_text():
            view.username_entry.delete(0, END)
            view.password_entry.delete(0, END)

        users = DbContext.load_from_json_file(DbContext.USERS_DB)
        usernames = DbContext.values_from_dictionary(users, 'username')
        username = view.username_entry.get()
        password = view.password_entry.get()
        if username not in usernames:
            # = self.password_entry = ' '.strip()
            clear_text()
            messagebox.showerror('FAIL', 'Wrong Username')
        else:
            index = usernames.index(username)
            yy = users[index]['password']
            if password != users[index]['password']:
                clear_text()
                messagebox.showerror('FAIL', 'Wrong Password')
            else:
                if users[index]['role'] == 'administrator':
                    self.parent.destroy()
                    user = Administrator(username, password, users[index]['role'], users[index]['code'])
                    view = Tk()
                    self.ac = AdminController(view, user)
                    self.ac.show_admin_panel()
                    # menu = AdministratorView(view, username, password, users[index]['role'], users[index]['code'])
                    view.mainloop()
                elif users[index]['role'] == 'client':
                    self.parent.destroy()
                    user = Client(username, password, users[index]['role'], users[index]['code'])
                    view = Tk()
                    self.cc = ClientController(view, user)
                    self.cc.show_client_main_view()
                    # menu = ClientView(view, username, password, users[index]['role'], users[index]['code'])
                    view.mainloop()
                elif users[index]['role'] == 'ww':
                    self.parent.destroy()
                    user = WarehouseWorker(username, password, users[index]['role'], users[index]['code'])
                    view = Tk()
                    self.wwc = WwController(view, user)
                    self.wwc.show_ww_main_view()
                    # menu = WarehouseWorkerView(view, username, password, users[index]['role'], users[index]['code'])
                    view.mainloop()
