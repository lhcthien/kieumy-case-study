from tkinter import ttk

from PIL import ImageTk
from tkinter import *

class LoginView:
    def __init__(self, parent):
        self.root = parent
        self.root.title('Warehouse Management System')
        self.root.geometry('1200x550+200+70')
        self.root.resizable(False, False)

    def setup(self):
        self.create_widgets()
        self.setup_layout()

    def button_check(self):
        print('Login btn was clicked')

    def create_widgets(self):
        self.image = ImageTk.PhotoImage(file='D:\kieumy-case-study\WMS_project_MVC-main\WMS_project_MVC-main\imgs\login_pic4-1.png')
        self.label = Label(self.root, image=self.image)
        self.label.pack()

        # Frame for username and password
        self.frame = ttk.Frame(self.root)  # bg='#000000'

        # Labels and entries for username and password
        self.username_label = Label(self.frame, text='Username', font=('Andalus', 15, 'bold'), fg='DodgerBlue3')

        self.password_label = Label(self.frame, text='Password', font=('Andalus', 15, 'bold'),fg='DodgerBlue3')

        self.username_entry_var = StringVar()
        self.password_entry_var = StringVar()

        self.username_entry = ttk.Entry(self.frame, textvariable=self.username_entry_var, font=('Andalus', 15))

        self.password_entry = ttk.Entry(self.frame, show='*', textvariable=self.password_entry_var,
                                        font=('Andalus', 15))

        self.btn_login = Button(self.frame, text='LOGIN', activebackground='SteelBlue1', activeforeground='white',
                                fg='DodgerBlue3', bg='#F0F8FF', font=('Andalus', 15, 'bold'))

    def setup_layout(self):
        self.frame.place(x=400, y=400, width=400, height=450)
        self.username_label.place(x=20, y=20)
        self.password_label.place(x=20, y=60)
        self.username_entry.place(x=160, y=20, width=200)
        self.password_entry.place(x=160, y=60, width=200)
        self.btn_login.place(x=160, y=100, width=200)

