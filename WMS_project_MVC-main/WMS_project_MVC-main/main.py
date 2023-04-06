from tkinter import *

from adminView import *
from adminModel import *
from controllers.login_controller import *
import controllers

class AppStart():
    def __init__(self):
        mainwin = Tk()
        self.lc = controllers.login_controller.LoginController(mainwin)
        self.lc.show_login_window()
        
        mainwin.mainloop()


if __name__ == "__main__":
    AppStart()
