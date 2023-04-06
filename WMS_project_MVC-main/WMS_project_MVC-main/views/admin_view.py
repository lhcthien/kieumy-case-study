from tkinter import ttk

# import tk as tk
# from PIL import ImageTk
from tkinter import *

class AdminMainView(ttk.Frame):
    def __init__(self, parent, ctrl):
        super().__init__()
        self.root = parent
        self.root.title('Warehouse Management System')
        style = ttk.Style()
        style.configure('Mitko.TButton', font=('Helvetica', 20))
        self.ctrl = ctrl
        # self.root.rowconfigure(0,weight=1)
        # self.root.columnconfigure(0, weight=1)
        self.username_label_text = ''
        self.role_label_text = ''

    def setup(self):
        self.create_widgets()
        self.setup_layout()

    def create_widgets(self):
        self.container = ttk.Frame(self.root, padding=(3, 3, 12, 12))

        self.frame1 = ttk.Frame(self.container, borderwidth=5, relief="ridge")

        self.users = ttk.Button(self.container, text="USERS", style='Mitko.TButton')

        self.inbounds = ttk.Button(self.container, text="INBOUNDS", style='Mitko.TButton')

        self.outbounds = ttk.Button(self.container, text="OUTBOUNDS", style='Mitko.TButton')

        self.products = ttk.Button(self.container, text="PRODUCTS", style='Mitko.TButton')

        self.locations = ttk.Button(self.container, text="LOCATIONS", style='Mitko.TButton')

        self.logout = ttk.Button(self.container, text="Logout")

        self.username_label = ttk.Label(self.container, text=self.username_label_text)

        self.role_label = ttk.Label(self.container, text=self.role_label_text)

        self.tv = ttk.Treeview(self.frame1, columns=(1, 2, 3, 4), show='headings')


    def setup_layout(self):
        self.username_label.grid(column=2, row=6, sticky=(N, W), pady=2, padx=10)
        self.role_label.grid(column=3, row=6, sticky=(N, W), pady=2, padx=10)

        self.container.grid(column=0, row=0, sticky=(N, S, E, W))
        self.frame1.grid(column=2, row=0, columnspan=4, rowspan=6, sticky=(N, S, E, W))
        self.users.grid(column=0, row=0, columnspan=2, sticky=(N, E, W), pady=5, padx=5)
        self.inbounds.grid(column=0, row=1, columnspan=2, sticky=(N, E, W), pady=5, padx=5)
        self.outbounds.grid(column=0, row=2, columnspan=2, sticky=(N, E, W), pady=5, padx=5)
        self.products.grid(column=0, row=3, columnspan=2, sticky=(N, E, W), pady=5, padx=5)
        self.locations.grid(column=0, row=5, columnspan=2, sticky=(N, E, W), pady=5, padx=5)

        self.tv.grid(column=0, row=0, columnspan=4, rowspan=6, sticky=(N, S, E, W))

        # self.ok.grid(column=0, row=6)
        self.logout.grid(column=1, row=6, sticky=(W))

        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

#=========================================================================
# =================== ADMIN USERS VIEWS ==================================
class AdminUsersWindow(ttk.Frame):
    def __init__(self, parent, ctrl):
        super().__init__()
        self.root = parent
        self.ctrl = ctrl

    def clear_frame_forget(self):
        for widgets in self.root.frame1.winfo_children():
            widgets.forget()

    def clear_frame_destroy(self):
        for widgets in self.root.winfo_children():
            widgets.destroy()

    def setup(self):
        # self.clear_frame_destroy()
        self.create_widgets()
        self.setup_layout()

    def create_widgets(self):
        # self.clear_frame_destroy()
        self.lst_all_users = ttk.Button(self.root.frame1, text='List All Users')
        self.add_user = ttk.Button(self.root.frame1, text='Add User')
        self.delete_user = ttk.Button(self.root.frame1, text='Delete User')
        self.update_user = ttk.Button(self.root.frame1, text='Update User')

    def setup_layout(self):
        self.lst_all_users.grid(row=6, column=0, sticky=(S, W))
        self.add_user.grid(row=6, column=1, sticky=(S, W))
        self.delete_user.grid(row=6, column=2, sticky=(S, W))
        self.update_user.grid(row=6, column=3, sticky=(S, W))

# ==================================================================================
class ListAllUsersFrame(ttk.Frame,Tk):
    def __init__(self, parent, ctrl):
        super().__init__()
        self.root = parent
        self.ctrl = ctrl

    def clear_frame(self):
        for widgets in self.root.frame1.winfo_children():
            widgets.destroy()

    def setup(self):
        self.create_widgets()
        self.setup_layout()

    def create_widgets(self):
        self.tv = ttk.Treeview(self.root.frame1, columns=(1, 2, 3, 4), show='headings')
        self.ybar = ttk.Scrollbar(self.root.frame1, orient='vertical', command=self.tv.yview)
        self.tv.configure(yscroll=self.ybar.set)

        self.tv['columns'] = ('username', 'password', 'role', 'code')
        self.tv.column('#0', width=0, stretch=NO)
        self.tv.column('username', width=180)
        self.tv.column('password', width=180)
        self.tv.column('role', width=180)
        self.tv.column('code', width=180)

        self.tv.heading('#0', text='', anchor=CENTER)
        self.tv.heading('username', text='USERNAME', anchor=CENTER)
        self.tv.heading('password', text='PASSWORD', anchor=CENTER)
        self.tv.heading('role', text='ROLE', anchor=CENTER)
        self.tv.heading('code', text='CODE', anchor=CENTER)

        self.ybar.configure(command=self.tv.yview)

        for i in self.tv.get_children():
            self.tv.delete(i)

    def setup_layout(self):
        self.tv.grid(column=0, row=0, columnspan=4, sticky=(N, S, E, W))
        self.ybar.grid(column=5, row=0, sticky='nse')

    def insert_in_treeview(self, users):
        for index, user in enumerate(users):
            self.tv.insert('', index, values=(user['username'], user['password'], user['role'], user['code']))

# ==================================================================================
class AddUserFrame(ttk.Frame, Tk):
    def __init__(self, parent, ctrl):
        super().__init__()
        self.root = parent
        self.ctrl = ctrl

    def clear_frame(self):
        for widgets in self.root.frame1.winfo_children():
            widgets.destroy()

    def setup(self):
        self.create_widgets()
        self.setup_layout()

    def create_widgets(self):
        self.username_label = ttk.Label(self.root.frame1, text='USERNAME')
        self.password_label = ttk.Label(self.root.frame1, text='PASSWORD')
        self.role_label = ttk.Label(self.root.frame1, text='ROLE')
        self.code_label = ttk.Label(self.root.frame1, text='CODE(s)')

        self.username_entry_var = StringVar()
        self.password_entry_var = StringVar()
        self.role_entry_var = StringVar()
        self.code_entry_var = StringVar()

        self.username_entry = ttk.Entry(self.root.frame1, textvariable=self.username_entry_var, width=15)
        self.password_entry = ttk.Entry(self.root.frame1, textvariable=self.password_entry_var, width=15)
        self.role_entry = ttk.Entry(self.root.frame1, textvariable=self.role_entry_var, width=15)
        self.code_entry = ttk.Entry(self.root.frame1, textvariable=self.code_entry_var, width=15)

        self.add_btn = ttk.Button(self.root.frame1, text='SUBMIT', width=15)


    def setup_layout(self):
        self.username_label.grid(column=0, row=1, sticky=(N, W), pady=2, padx=10)
        self.password_label.grid(column=0, row=2, sticky=(N, W), pady=2, padx=10)
        self.role_label.grid(column=0, row=3, sticky=(N, W), pady=2, padx=10)
        self.code_label.grid(column=0, row=4, sticky=(N, W), pady=2, padx=10)
        self.username_entry.grid(column=1, row=1, sticky=(N,))
        self.password_entry.grid(column=1, row=2, sticky=(N,))
        self.role_entry.grid(column=1, row=3, sticky=(N,))

        self.code_entry.grid(column=1, row=4, sticky=(N,))
        self.add_btn.grid(column=1, row=5, sticky=(N,))

# ==================================================================================
class DeleteUserFrame(ttk.Frame, Tk):
    def __init__(self, parent, ctrl):
        super().__init__()
        self.root = parent
        self.ctrl = ctrl

    def clear_frame(self):
        for widgets in self.root.frame1.winfo_children():
            widgets.destroy()

    def setup(self):
        self.create_widgets()
        self.setup_layout()

    def create_widgets(self):
        self.username_label = ttk.Label(self.root.frame1, text='USERNAME')
        self.username_entry_var = StringVar()
        self.username_entry = ttk.Entry(self.root.frame1, textvariable=self.username_entry_var, width=15)
        self.delete_btn = ttk.Button(self.root.frame1, text='DELETE', width=15)

    def setup_layout(self):
        self.username_label.grid(column=0, row=1, sticky=(N, W), pady=2, padx=10)
        self.username_entry.grid(column=1, row=1, sticky=(N))
        self.delete_btn.grid(column=1, row=2, sticky=(N))

# ==================================================================================
class UpdateUserFrame(ttk.Frame, Tk):
    def __init__(self, parent, ctrl):
        super().__init__()
        self.root = parent
        self.ctrl = ctrl

    def clear_frame(self):
        for widgets in self.root.frame1.winfo_children():
            widgets.destroy()

    def setup(self):
        self.create_widgets()
        self.setup_layout()

    def create_widgets(self):
        self.username_label = ttk.Label(self.root.frame1, text='USERNAME')
        self.username_entry_var = StringVar()
        self.username_entry = ttk.Entry(self.root.frame1, textvariable=self.username_entry_var, width=15)

        self.update_btn = ttk.Button(self.root.frame1, text='UPDATE', width=15)

    def setup_layout(self):
        self.username_label.grid(column=0, row=1, sticky=(N, W), pady=2, padx=10)
        self.username_entry.grid(column=1, row=1, sticky=(N))
        self.update_btn.grid(column=1, row=2, sticky=(N))

class SaveUpdatedUserFrame(ttk.Frame, Tk):
    def __init__(self, parent, ctrl):
        super().__init__()
        self.root = parent
        self.ctrl = ctrl

    def clear_frame(self):
        for widgets in self.root.frame1.winfo_children():
            widgets.destroy()

    def setup(self):
        self.create_widgets()
        self.setup_layout()

    def create_widgets(self):
        self.username_label = ttk.Label(self.root.frame1, text='USERNAME')
        self.password_label = ttk.Label(self.root.frame1, text='PASSWORD')
        self.role_label = ttk.Label(self.root.frame1, text='ROLE')
        self.code_label = ttk.Label(self.root.frame1, text='CODE(s)')

        self.username_entry_var = StringVar()
        self.password_entry_var = StringVar()
        self.role_entry_var = StringVar()
        self.code_entry_var = StringVar()

        self.username_entry = ttk.Entry(self.root.frame1, textvariable=self.username_entry_var, width=15)
        self.password_entry = ttk.Entry(self.root.frame1, textvariable=self.password_entry_var, width=15)
        self.role_entry = ttk.Entry(self.root.frame1, textvariable=self.role_entry_var, width=15)
        self.code_entry = ttk.Entry(self.root.frame1, textvariable=self.code_entry_var, width=15)

        self.save_btn = ttk.Button(self.root.frame1, text='SAVE', width=15)

    def setup_layout(self):
        self.username_label.grid(column=0, row=1, sticky=(N, W), pady=2, padx=10)
        self.password_label.grid(column=0, row=2, sticky=(N, W), pady=2, padx=10)
        self.role_label.grid(column=0, row=3, sticky=(N, W), pady=2, padx=10)
        self.code_label.grid(column=0, row=4, sticky=(N, W), pady=2, padx=10)

        self.username_entry.grid(column=1, row=1, sticky=(N))
        self.password_entry.grid(column=1, row=2, sticky=(N))
        self.role_entry.grid(column=1, row=3, sticky=(N))
        self.code_entry.grid(column=1, row=4, sticky=(N))

        self.save_btn.grid(column=1, row=5, sticky=(N))

# ==================================================================================
# =========================ADMIN INBOUNDS VIEWS=====================================
class AdminInboundsWindow(ttk.Frame):
    def __init__(self, parent, ctrl):
        super().__init__()
        self.root = parent
        self.ctrl = ctrl

    def clear_frame(self):
        for widgets in self.root.winfo_children():
            widgets.destroy()

    def setup(self):
        self.create_widgets()
        self.setup_layout()

    def create_widgets(self):
        self.list_all_inbounds_frame = ttk.Button(self.root.frame1, text='List All Inbounds')
        self.specific_inbound_frame = ttk.Button(self.root.frame1, text='Inbound by ID')
        self.list_inbounds_by_clients_frame = ttk.Button(self.root.frame1, text='Inbound by Client')
        self.list_inbounds_by_time_frame = ttk.Button(self.root.frame1, text='Inbound by Date')

    def setup_layout(self):
       self.list_all_inbounds_frame.grid(row=6, column=0, sticky=(S, W))
       self.specific_inbound_frame.grid(row=6, column=1, sticky=(S, W))
       self.list_inbounds_by_clients_frame.grid(row=6, column=2, sticky=(S, W))
       self.list_inbounds_by_time_frame.grid(row=6, column=3, sticky=(S, W))

# ==================================================================
class ListAllInboundsView(ttk.Frame,Tk):
    def __init__(self, parent, ctrl):
        super().__init__()
        self.root = parent
        self.ctrl = ctrl

    def setup(self):
        self.create_widgets()
        self.setup_layout()

    def create_widgets(self):
        self.tv = ttk.Treeview(self.root.frame1, columns=(1, 2, 3, 4, 5, 6, 7), show='headings')
        self.ybar = ttk.Scrollbar(self.root.frame1, orient="vertical", command=self.tv.yview)
        self.tv.configure(yscroll=self.ybar.set)
        self.tv['columns'] = ('INBOUND/PRODUCT', 'ID', 'CLIENT_CODE', 'QUANTITY', 'DATE', 'STATUS', 'LOCATION')
        self.tv.column('#0', width=0, stretch=NO)
        self.tv.column('INBOUND/PRODUCT', anchor=CENTER, width=180)
        self.tv.column('ID', anchor=CENTER, width=100)
        self.tv.column('CLIENT_CODE', anchor=CENTER, width=100)
        self.tv.column('QUANTITY', anchor=CENTER, width=100)
        self.tv.column('DATE', anchor=CENTER, width=100)
        self.tv.column('STATUS', anchor=CENTER, width=100)
        self.tv.column('LOCATION', anchor=CENTER, width=100)

        self.tv.heading('#0', text='', anchor=CENTER)
        self.tv.heading('INBOUND/PRODUCT', text='INBOUND/PRODUCT', anchor=CENTER)
        self.tv.heading('ID', text='ID')
        self.tv.heading('CLIENT_CODE', text='CLIENT CODE')
        self.tv.heading('QUANTITY', text='QUANTITY')
        self.tv.heading('DATE', text='DATE')
        self.tv.heading('STATUS', text='STATUS')
        self.tv.heading('LOCATION', text='LOCATION')

        for i in self.tv.get_children():
            self.tv.delete(i)

    def setup_layout(self):
        self.tv.grid(column=0, row=0, columnspan=7, sticky=(N, S, E, W))
        self.ybar.grid(column=8, row=0, sticky='nse')
        self.ybar.configure(command=self.tv.yview)

    def insert_in_treeview(self, inbounds, quantities):
        tv_index = -1
        for i,inbound in enumerate(inbounds):
            tv_index += 1
            parent = self.tv.insert('', tv_index,
                                    values=('INBOUND', inbound['id'], inbound['client_code'], quantities[i],
                                            inbound['time'],inbound['status'], inbound['location']))
            for item in inbound['products']:
                tv_index += 1
                self.tv.insert(parent, tv_index,
                               values=('Product', item['code'], item['name'], item['quantity']))

# ==================================================================
class InboundByIdView(ttk.Frame,Tk):
    def __init__(self, parent, ctrl):
        super().__init__()
        self.root = parent
        self.ctrl = ctrl

    def setup(self):
        self.create_widgets()
        self.setup_layout()

    def create_widgets(self):
        self.id_inbound_label = ttk.Label(self.root.frame1, text='ID')
        self.id_inbound_entry_var = StringVar()
        self.id_inbound_entry = ttk.Entry(self.root.frame1, textvariable=self.id_inbound_entry_var)
        self.search_btn = ttk.Button(self.root.frame1, text='SEARCH', width=15)

    def setup_layout(self):
        self.id_inbound_label.grid(column=0, row=1, sticky=(N, W, E))
        self.id_inbound_entry.grid(column=1, row=1, sticky=N)
        self.search_btn.grid(column=1, row=3, sticky=N)

class InboundByIdTreeview(ttk.Frame,Tk):
    def __init__(self, parent, ctrl):
        super().__init__()
        self.root = parent
        self.ctrl = ctrl

    def setup(self):
        self.create_widgets()
        self.setup_layout()

    def create_widgets(self):
        self.tv = ttk.Treeview(self.root.frame1, columns=(1, 2, 3, 4, 5, 6, 7), show='headings')
        self.ybar = ttk.Scrollbar(self.root.frame1, orient='vertical', command=self.tv.yview)
        self.tv.configure(yscroll=self.ybar.set)
        self.tv['columns'] = ('INBOUND/PRODUCT', 'ID', 'CLIENT_CODE', 'QUANTITY', 'DATE', 'STATUS', 'LOCATION')
        self.tv.column('#0', width=0, stretch=NO)
        self.tv.column('INBOUND/PRODUCT', anchor=CENTER, width=180)
        self.tv.column('ID', anchor=CENTER, width=100)
        self.tv.column('CLIENT_CODE', anchor=CENTER, width=100)
        self.tv.column('QUANTITY', anchor=CENTER, width=100)
        self.tv.column('DATE', anchor=CENTER, width=100)
        self.tv.column('STATUS', anchor=CENTER, width=100)
        self.tv.column('LOCATION', anchor=CENTER, width=100)

        self.tv.heading('#0', text='', anchor=CENTER)
        self.tv.heading('INBOUND/PRODUCT', text='INBOUND/PRODUCT', anchor=CENTER)
        self.tv.heading('ID', text='ID')
        self.tv.heading('CLIENT_CODE', text='CLIENT CODE')
        self.tv.heading('QUANTITY', text='QUANTITY')
        self.tv.heading('DATE', text='DATE')
        self.tv.heading('STATUS', text='STATUS')
        self.tv.heading('LOCATION', text='LOCATION')
        self.ybar.configure(command=self.tv.yview)
        for i in self.tv.get_children():
            self.tv.delete(i)

    def setup_layout(self):
        self.tv.grid(column=0, row=0, columnspan=7, sticky=(N, S, E, W))
        self.ybar.grid(column=8, row=0, sticky='nse')


    def insert_in_treeview(self, inbound, p_in_inbound):
        parent = self.tv.insert('', 'end', text='Item_0',
                                values=('INBOUND', inbound['id'], inbound['client_code'], p_in_inbound, inbound['time'],
                                        inbound['status'], inbound['location']))
        for item in inbound['products']:
            self.tv.insert(parent, 'end',
                           values=('Product', item['code'], item['name'], item['quantity']))

# ===================================================================
class InboundByClient(ttk.Frame,Tk):
    def __init__(self, parent, ctrl):
        super().__init__()
        self.root = parent
        self.ctrl = ctrl

    def setup(self):
        self.create_widgets()
        self.setup_layout()

    def create_widgets(self):
        # self.inbounds_frame()
        self.client_inbound_label = ttk.Label(self.root.frame1, text='CLIENT CODE')

        self.client_inbound_entry_var = StringVar()
        self.client_inbound_entry = ttk.Entry(self.root.frame1, textvariable=self.client_inbound_entry_var)

        self.search_btn = ttk.Button(self.root.frame1, text='SEARCH', width=15)


    def setup_layout(self):
        self.client_inbound_label.grid(column=0, row=1, sticky=(N, W, E))
        self.client_inbound_entry.grid(column=1, row=1, sticky=(N))
        self.search_btn.grid(column=1, row=3, sticky=(N))

class InboundByClientTreeview(ttk.Frame,Tk):
    def __init__(self, parent, ctrl):
        super().__init__()
        self.root = parent
        self.ctrl = ctrl

    def setup(self):
        self.create_widgets()
        self.setup_layout()

    def create_widgets(self):
        self.tv = ttk.Treeview(self.root.frame1, columns=(1, 2, 3, 4, 5, 6, 7), show='headings')
        self.ybar = ttk.Scrollbar(self.root.frame1, orient='vertical', command=self.tv.yview)
        self.tv.configure(yscroll=self.ybar.set)
        self.tv['columns'] = ('INBOUND/PRODUCT', 'ID', 'CLIENT_CODE', 'QUANTITY', 'DATE', 'STATUS', 'LOCATION')
        self.tv.column('#0', width=0, stretch=NO)
        self.tv.column('INBOUND/PRODUCT', anchor=CENTER, width=180)
        self.tv.column('ID', anchor=CENTER, width=100)
        self.tv.column('CLIENT_CODE', anchor=CENTER, width=100)
        self.tv.column('QUANTITY', anchor=CENTER, width=100)
        self.tv.column('DATE', anchor=CENTER, width=100)
        self.tv.column('STATUS', anchor=CENTER, width=100)
        self.tv.column('LOCATION', anchor=CENTER, width=100)

        self.tv.heading('#0', text='', anchor=CENTER)
        self.tv.heading('INBOUND/PRODUCT', text='INBOUND/PRODUCT', anchor=CENTER)
        self.tv.heading('ID', text='ID')
        self.tv.heading('CLIENT_CODE', text='CLIENT CODE')
        self.tv.heading('QUANTITY', text='QUANTITY')
        self.tv.heading('DATE', text='DATE')
        self.tv.heading('STATUS', text='STATUS')
        self.tv.heading('LOCATION', text='LOCATION')
        self.ybar.configure(command=self.tv.yview)
        for i in self.tv.get_children():
            self.tv.delete(i)

    def setup_layout(self):
        self.tv.grid(column=0, row=0, columnspan=7, sticky=(N, S, E, W))
        self.ybar.grid(column=8, row=0, sticky='nse')


    def insert_in_treeview(self, indexes, inbounds, p_in_inbound):
        tv_index = -1
        for i in indexes:
            tv_index += 1
            parent = self.tv.insert('', tv_index,
                                    values=('INBOUND', inbounds[i]['id'], inbounds[i]['client_code'], p_in_inbound[i],
                                            inbounds[i]['time'], inbounds[i]['status'], inbounds[i]['location']))
            for item in inbounds[i]['products']:
                tv_index += 1
                self.tv.insert(parent, tv_index,
                           values=('Product', item['code'], item['name'], item['quantity']))

# ===================================================================
class InboundByTime(ttk.Frame,Tk):
    def __init__(self, parent, ctrl):
        super().__init__()
        self.root = parent
        self.ctrl = ctrl

    def setup(self):
        self.create_widgets()
        self.setup_layout()

    def create_widgets(self):
        self.time_inbound_label = ttk.Label(self.root.frame1, text='DATE')
        self.time_inbound_entry_var = StringVar()
        self.time_inbound_entry = ttk.Entry(self.root.frame1, textvariable=self.time_inbound_entry_var)
        self.search_btn = ttk.Button(self.root.frame1, text='SEARCH', width=15)

    def setup_layout(self):
        self.time_inbound_label.grid(column=0, row=1, sticky=(N, W, E))
        self.time_inbound_entry.grid(column=1, row=1, sticky=(N))
        self.search_btn.grid(column=1, row=3, sticky=(N))

class InboundByTimeTreeview(ttk.Frame,Tk):
    def __init__(self, parent, ctrl):
        super().__init__()
        self.root = parent
        self.ctrl = ctrl

    def setup(self):
        self.create_widgets()
        self.setup_layout()

    def create_widgets(self):
        self.tv = ttk.Treeview(self.root.frame1, columns=(1, 2, 3, 4, 5, 6, 7), show='headings')
        self.ybar = ttk.Scrollbar(self.root.frame1, orient='vertical', command=self.tv.yview)
        self.tv.configure(yscroll=self.ybar.set)
        self.tv['columns'] = ('INBOUND/PRODUCT', 'ID', 'CLIENT_CODE', 'QUANTITY', 'DATE', 'STATUS', 'LOCATION')
        self.tv.column('#0', width=0, stretch=NO)
        self.tv.column('INBOUND/PRODUCT', anchor=CENTER, width=180)
        self.tv.column('ID', anchor=CENTER, width=100)
        self.tv.column('CLIENT_CODE', anchor=CENTER, width=100)
        self.tv.column('QUANTITY', anchor=CENTER, width=100)
        self.tv.column('DATE', anchor=CENTER, width=100)
        self.tv.column('STATUS', anchor=CENTER, width=100)
        self.tv.column('LOCATION', anchor=CENTER, width=100)

        self.tv.heading('#0', text='', anchor=CENTER)
        self.tv.heading('INBOUND/PRODUCT', text='INBOUND/PRODUCT', anchor=CENTER)
        self.tv.heading('ID', text='ID')
        self.tv.heading('CLIENT_CODE', text='CLIENT CODE')
        self.tv.heading('QUANTITY', text='QUANTITY')
        self.tv.heading('DATE', text='DATE')
        self.tv.heading('STATUS', text='STATUS')
        self.tv.heading('LOCATION', text='LOCATION')
        self.ybar.configure(command=self.tv.yview)
        for i in self.tv.get_children():
            self.tv.delete(i)

    def setup_layout(self):
        self.tv.grid(column=0, row=0, columnspan=7, sticky=(N, S, E, W))
        self.ybar.grid(column=8, row=0, sticky='nse')

    def insert_in_treeview(self, indexes, inbounds, p_in_inbound):
        tv_index = -1
        for i in indexes:
            tv_index += 1
            parent = self.tv.insert('', tv_index,
                                    values=('INBOUND', inbounds[i]['id'], inbounds[i]['client_code'], p_in_inbound[i],
                                            inbounds[i]['time'], inbounds[i]['status'], inbounds[i]['location']))
            for item in inbounds[i]['products']:
                tv_index += 1
                self.tv.insert(parent, tv_index,
                               values=('Product', item['code'], item['name'], item['quantity']))

# ==================================================================================
# =========================ADMIN OUTBOUNDS VIEWS=====================================
class AdminOutboundsWindow(ttk.Frame):
    def __init__(self, parent, ctrl):
        super().__init__()
        self.root = parent
        self.ctrl = ctrl

    def setup(self):
        self.create_widgets()
        self.setup_layout()

    def create_widgets(self):
        self.list_all_outbounds_frame = ttk.Button(self.root.frame1, text='List All Outbounds')
        self.specific_outbound_frame = ttk.Button(self.root.frame1, text='Outbound by ID')
        self.list_outbounds_by_clients_frame = ttk.Button(self.root.frame1, text='Outbound by Client')
        self.list_outbounds_by_time_frame = ttk.Button(self.root.frame1, text='Outbound by Date')

    def setup_layout(self):
        self.list_all_outbounds_frame.grid(row=6, column=0, sticky=(S, W))
        self.specific_outbound_frame.grid(row=6, column=1, sticky=(S, W))
        self.list_outbounds_by_clients_frame.grid(row=6, column=2, sticky=(S, W))
        self.list_outbounds_by_time_frame.grid(row=6, column=3, sticky=(S, W))

# ==================================================================
class ListAllOutboundsView(ttk.Frame,Tk):
    def __init__(self, parent, ctrl):
        super().__init__()
        self.root = parent
        self.ctrl = ctrl

    def setup(self):
        self.create_widgets()
        self.setup_layout()

    def create_widgets(self):
        self.tv = ttk.Treeview(self.root.frame1, columns=(1, 2, 3, 4, 5, 6, 7), show='headings')
        self.ybar = ttk.Scrollbar(self.root.frame1, orient="vertical", command=self.tv.yview)
        self.tv.configure(yscroll=self.ybar.set)
        self.tv['columns'] = ('OUTBOUND/PRODUCT', 'ID', 'CLIENT_CODE', 'QUANTITY', 'DATE', 'STATUS', 'LOCATION')
        self.tv.column('#0', width=0, stretch=NO)
        self.tv.column('OUTBOUND/PRODUCT', anchor=CENTER, width=180)
        self.tv.column('ID', anchor=CENTER, width=100)
        self.tv.column('CLIENT_CODE', anchor=CENTER, width=100)
        self.tv.column('QUANTITY', anchor=CENTER, width=100)
        self.tv.column('DATE', anchor=CENTER, width=100)
        self.tv.column('STATUS', anchor=CENTER, width=100)
        self.tv.column('LOCATION', anchor=CENTER, width=100)

        self.tv.heading('#0', text='', anchor=CENTER)
        self.tv.heading('OUTBOUND/PRODUCT', text='INBOUND/PRODUCT', anchor=CENTER)
        self.tv.heading('ID', text='ID')
        self.tv.heading('CLIENT_CODE', text='CLIENT CODE')
        self.tv.heading('QUANTITY', text='QUANTITY')
        self.tv.heading('DATE', text='DATE')
        self.tv.heading('STATUS', text='STATUS')
        self.tv.heading('LOCATION', text='LOCATION')
        for i in self.tv.get_children():
            self.tv.delete(i)

    def setup_layout(self):
        self.tv.grid(column=0, row=0, columnspan=7, sticky=(N, S, E, W))
        self.ybar.grid(column=8, row=0, sticky='nse')
        self.ybar.configure(command=self.tv.yview)

    def insert_in_treeview(self, outbounds, quantities):
        self.id = 0
        self.iid = 0

        for outbound in outbounds:
            parent = self.tv.insert('', 'end', iid=self.iid, text='Item_' + str(self.id),
                                    values=('OUTBOUND', outbound['id'], outbound['client_code'], quantities, outbound['time'],
                                    outbound['status'], outbound['location']))
            self.iid = self.iid + 1
            self.id = self.id + 1
            for item in outbound['products']:
                self.tv.insert(parent, 'end', iid=self.iid,
                               values=('Product', item['code'], item['name'], item['quantity']))
                self.iid = self.iid + 1
                self.id = self.id + 1

# ==================================================================
class OutboundByIdView(ttk.Frame,Tk):
    def __init__(self, parent, ctrl):
        super().__init__()
        self.root = parent
        self.ctrl = ctrl

    def setup(self):
        self.create_widgets()
        self.setup_layout()

    def create_widgets(self):
        self.id_outbound_label = ttk.Label(self.root.frame1, text='ID')
        self.id_outbound_entry_var = StringVar()
        self.id_outbound_entry = ttk.Entry(self.root.frame1, textvariable=self.id_outbound_entry_var)
        self.search_btn = ttk.Button(self.root.frame1, text='SEARCH', width=15)

    def setup_layout(self):
        self.id_outbound_label.grid(column=0, row=1, sticky=(N, W, E))
        self.id_outbound_entry.grid(column=1, row=1, sticky=N)
        self.search_btn.grid(column=1, row=3, sticky=N)

class OutboundByIdTreeview(ttk.Frame,Tk):
    def __init__(self, parent, ctrl):
        super().__init__()
        self.root = parent
        self.ctrl = ctrl

    def setup(self):
        self.create_widgets()
        self.setup_layout()

    def create_widgets(self):
        self.tv = ttk.Treeview(self.root.frame1, columns=(1, 2, 3, 4, 5, 6, 7), show='headings')
        self.ybar = ttk.Scrollbar(self.root.frame1, orient='vertical', command=self.tv.yview)
        self.tv.configure(yscroll=self.ybar.set)
        self.tv['columns'] = ('OUTBOUND/PRODUCT', 'ID', 'CLIENT_CODE', 'QUANTITY', 'DATE', 'STATUS', 'LOCATION')
        self.tv.column('#0', width=0, stretch=NO)
        self.tv.column('OUTBOUND/PRODUCT', anchor=CENTER, width=180)
        self.tv.column('ID', anchor=CENTER, width=100)
        self.tv.column('CLIENT_CODE', anchor=CENTER, width=100)
        self.tv.column('QUANTITY', anchor=CENTER, width=100)
        self.tv.column('DATE', anchor=CENTER, width=100)
        self.tv.column('STATUS', anchor=CENTER, width=100)
        self.tv.column('LOCATION', anchor=CENTER, width=100)

        self.tv.heading('#0', text='', anchor=CENTER)
        self.tv.heading('OUTBOUND/PRODUCT', text='INBOUND/PRODUCT', anchor=CENTER)
        self.tv.heading('ID', text='ID')
        self.tv.heading('CLIENT_CODE', text='CLIENT CODE')
        self.tv.heading('QUANTITY', text='QUANTITY')
        self.tv.heading('DATE', text='DATE')
        self.tv.heading('STATUS', text='STATUS')
        self.tv.heading('LOCATION', text='LOCATION')

        self.ybar.configure(command=self.tv.yview)
        for i in self.tv.get_children():
            self.tv.delete(i)

    def setup_layout(self):
        self.tv.grid(column=0, row=0, columnspan=7, sticky=(N, S, E, W))
        self.ybar.grid(column=8, row=0, sticky='nse')


    def insert_in_treeview(self, outbound, p_in_outbound):
        parent = self.tv.insert('', 'end', text='Item_0',
                                values=('OUTBOUND', outbound['id'], outbound['client_code'], p_in_outbound, outbound['time'],
                                        outbound['status'], outbound['location']))
        for item in outbound['products']:
            self.tv.insert(parent, 'end',
                           values=('Product', item['code'], item['name'], item['quantity']))

# ===================================================================
class OutboundsByClient(ttk.Frame,Tk):
    def __init__(self, parent, ctrl):
        super().__init__()
        self.root = parent
        self.ctrl = ctrl

    def setup(self):
        self.create_widgets()
        self.setup_layout()

    def create_widgets(self):
        # self.inbounds_frame()
        self.client_outbound_label = ttk.Label(self.root.frame1, text='CLIENT CODE')
        self.client_outbound_entry_var = StringVar()
        self.client_outbound_entry = ttk.Entry(self.root.frame1, textvariable=self.client_outbound_entry_var)

        self.search_btn = ttk.Button(self.root.frame1, text='SEARCH', width=15)


    def setup_layout(self):
        self.client_outbound_label.grid(column=0, row=1, sticky=(N, W, E))
        self.client_outbound_entry.grid(column=1, row=1, sticky=N)
        self.search_btn.grid(column=1, row=3, sticky=(N))

class OutboundsByClientTreeview(ttk.Frame,Tk):
    def __init__(self, parent, ctrl):
        super().__init__()
        self.root = parent
        self.ctrl = ctrl

    def setup(self):
        self.create_widgets()
        self.setup_layout()

    def create_widgets(self):
        self.tv = ttk.Treeview(self.root.frame1, columns=(1, 2, 3, 4, 5, 6, 7), show='headings')
        self.ybar = ttk.Scrollbar(self.root.frame1, orient='vertical', command=self.tv.yview)
        self.tv.configure(yscroll=self.ybar.set)
        self.tv['columns'] = ('OUTBOUND/PRODUCT', 'ID', 'CLIENT_CODE', 'QUANTITY', 'DATE', 'STATUS', 'LOCATION')
        self.tv.column('#0', width=0, stretch=NO)
        self.tv.column('OUTBOUND/PRODUCT', anchor=CENTER, width=180)
        self.tv.column('ID', anchor=CENTER, width=100)
        self.tv.column('CLIENT_CODE', anchor=CENTER, width=100)
        self.tv.column('QUANTITY', anchor=CENTER, width=100)
        self.tv.column('DATE', anchor=CENTER, width=100)
        self.tv.column('STATUS', anchor=CENTER, width=100)
        self.tv.column('LOCATION', anchor=CENTER, width=100)

        self.tv.heading('#0', text='', anchor=CENTER)
        self.tv.heading('OUTBOUND/PRODUCT', text='INBOUND/PRODUCT', anchor=CENTER)
        self.tv.heading('ID', text='ID')
        self.tv.heading('CLIENT_CODE', text='CLIENT CODE')
        self.tv.heading('QUANTITY', text='QUANTITY')
        self.tv.heading('DATE', text='DATE')
        self.tv.heading('STATUS', text='STATUS')
        self.tv.heading('LOCATION', text='LOCATION')
        self.ybar.grid(column=8, row=0, sticky='nse')
        self.ybar.configure(command=self.tv.yview)
        for i in self.tv.get_children():
            self.tv.delete(i)

    def setup_layout(self):
        self.tv.grid(column=0, row=0, columnspan=7, sticky=(N, S, E, W))
        self.ybar.grid(column=8, row=0, sticky='nse')

    def insert_in_treeview(self, indexes, outbounds, p_in_outbound):
        tv_index = -1
        for i in indexes:
            tv_index += 1
            parent = self.tv.insert('', tv_index,
                                    values=('OUTBOUND', outbounds[i]['id'], outbounds[i]['client_code'], p_in_outbound[i],
                                            outbounds[i]['time'], outbounds[i]['status'], outbounds[i]['location']))
            for item in outbounds[i]['products']:
                tv_index += 1
                self.tv.insert(parent, tv_index,
                           values=('Product', item['code'], item['name'], item['quantity']))

# ===================================================================
class OutboundsByTime(ttk.Frame,Tk):
    def __init__(self, parent, ctrl):
        super().__init__()
        self.root = parent
        self.ctrl = ctrl

    def setup(self):
        self.create_widgets()
        self.setup_layout()

    def create_widgets(self):
        self.time_outbound_label = ttk.Label(self.root.frame1, text='DATE')
        self.time_outbound_entry_var = StringVar()
        self.time_outbound_entry = ttk.Entry(self.root.frame1, textvariable=self.time_outbound_entry_var)
        self.search_btn = ttk.Button(self.root.frame1, text='SEARCH', width=15)

    def setup_layout(self):
        self.time_outbound_label.grid(column=0, row=1, sticky=(N, W, E))
        self.time_outbound_entry.grid(column=1, row=1, sticky=(N))
        self.search_btn.grid(column=1, row=3, sticky=(N))

class OutboundsByTimeTreeview(ttk.Frame,Tk):
    def __init__(self, parent, ctrl):
        super().__init__()
        self.root = parent
        self.ctrl = ctrl

    def setup(self):
        self.create_widgets()
        self.setup_layout()

    def create_widgets(self):
        self.tv = ttk.Treeview(self.root.frame1, columns=(1, 2, 3, 4, 5, 6, 7), show='headings')
        self.ybar = ttk.Scrollbar(self.root.frame1, orient='vertical', command=self.tv.yview)
        self.tv.configure(yscroll=self.ybar.set)
        self.tv['columns'] = ('OUTBOUND/PRODUCT', 'ID', 'CLIENT_CODE', 'QUANTITY', 'DATE', 'STATUS', 'LOCATION')
        self.tv.column('#0', width=0, stretch=NO)
        self.tv.column('OUTBOUND/PRODUCT', anchor=CENTER, width=180)
        self.tv.column('ID', anchor=CENTER, width=100)
        self.tv.column('CLIENT_CODE', anchor=CENTER, width=100)
        self.tv.column('QUANTITY', anchor=CENTER, width=100)
        self.tv.column('DATE', anchor=CENTER, width=100)
        self.tv.column('STATUS', anchor=CENTER, width=100)
        self.tv.column('LOCATION', anchor=CENTER, width=100)

        self.tv.heading('#0', text='', anchor=CENTER)
        self.tv.heading('OUTBOUND/PRODUCT', text='INBOUND/PRODUCT', anchor=CENTER)
        self.tv.heading('ID', text='ID')
        self.tv.heading('CLIENT_CODE', text='CLIENT CODE')
        self.tv.heading('QUANTITY', text='QUANTITY')
        self.tv.heading('DATE', text='DATE')
        self.tv.heading('STATUS', text='STATUS')
        self.tv.heading('LOCATION', text='LOCATION')
        self.ybar.configure(command=self.tv.yview)
        for i in self.tv.get_children():
            self.tv.delete(i)

    def setup_layout(self):
        self.tv.grid(column=0, row=0, columnspan=7, sticky=(N, S, E, W))
        self.ybar.grid(column=8, row=0, sticky='nse')

    def insert_in_treeview(self, indexes, outbounds, p_in_outbound):
        tv_index = -1
        for i in indexes:
            tv_index += 1
            parent = self.tv.insert('', tv_index,
                                    values=('OUTBOUND', outbounds[i]['id'], outbounds[i]['client_code'], p_in_outbound[i],
                                            outbounds[i]['time'], outbounds[i]['status'], outbounds[i]['location']))
            for item in outbounds[i]['products']:
                tv_index += 1
                self.tv.insert(parent, tv_index,
                           values=('Product', item['code'], item['name'], item['quantity']))


# ===================================================================
# =========================ADMIN PRODUCTS VIEWS======================
class AdminProductsWindow(ttk.Frame):
    def __init__(self, parent, ctrl):
        super().__init__()
        self.root = parent
        self.ctrl = ctrl

    def setup(self):
        self.create_widgets()
        self.setup_layout()

    def create_widgets(self):
        self.lst_all_products = ttk.Button(self.root.frame1, text='List All Products')
        self.lst_products_by_client = ttk.Button(self.root.frame1, text='Products By Client')
        self.add_product = ttk.Button(self.root.frame1, text='Add Products')
        self.delete_product = ttk.Button(self.root.frame1, text='Delete Products')
        self.update_product = ttk.Button(self.root.frame1, text='Update Products')

    def setup_layout(self):
        self.lst_all_products.grid(row=8, column=0, sticky=(S, W))
        self.lst_products_by_client.grid(row=8, column=1, sticky=(S, W))
        self.add_product.grid(row=8, column=2, sticky=(S, W))
        self.delete_product.grid(row=8, column=3, sticky=(S, W))
        self.update_product.grid(row=8, column=4, sticky=(S, W))

#======================================================================
class ListAllProductsView(ttk.Frame,Tk):
    def __init__(self, parent, ctrl):
        super().__init__()
        self.root = parent
        self.ctrl = ctrl

    def setup(self):
        self.create_widgets()
        self.setup_layout()

    def create_widgets(self):
        self.tv = ttk.Treeview(self.root.frame1, columns=(1, 2, 3, 4, 5, 6), show='headings')
        self.ybar = ttk.Scrollbar(self.root.frame1, orient='vertical', command=self.tv.yview)
        self.tv.configure(yscroll=self.ybar.set)
        self.tv['columns'] = ('code', 'name', 'client_code', 'quantity', 'volume', 'weight')
        self.tv.column('#0', width=0, stretch=NO)
        self.tv.column('code', anchor=CENTER, width=180)
        self.tv.column('name', anchor=CENTER, width=180)
        self.tv.column('client_code', anchor=CENTER, width=180)
        self.tv.column('quantity', anchor=CENTER, width=180)
        self.tv.column('volume', anchor=CENTER, width=180)
        self.tv.column('weight', anchor=CENTER, width=180)

        self.tv.heading('#0', text='', anchor=CENTER)
        self.tv.heading('code', text='CODE', anchor=CENTER)
        self.tv.heading('name', text='NAME', anchor=CENTER)
        self.tv.heading('client_code', text='CLIENT CODE', anchor=CENTER)
        self.tv.heading('quantity', text='QUANTITY', anchor=CENTER)
        self.tv.heading('volume', text='VOLUME', anchor=CENTER)
        self.tv.heading('weight', text='WEIGHT', anchor=CENTER)
        self.ybar.configure(command=self.tv.yview)

        for i in self.tv.get_children():
            self.tv.delete(i)

    def setup_layout(self):
        self.tv.grid(column=0, row=0, columnspan=6, sticky=(N, S, E, W))
        self.ybar.grid(column=7, row=0, sticky='nse')

    def insert_in_treeview(self, products):
        for index, prod in enumerate(products):
            self.tv.insert('', index, values=(prod['code'], prod['name'], prod['client_code'], prod['quantity'],
                                              prod['volume'], prod['weight']))

#======================================================================
class ProductsByClientView(ttk.Frame,Tk):
    def __init__(self, parent, ctrl):
        super().__init__()
        self.root = parent
        self.ctrl = ctrl

    def setup(self):
        self.create_widgets()
        self.setup_layout()

    def create_widgets(self):
        self.client_code_products_label = ttk.Label(self.root.frame1, text='CLIENT CODE')
        self.client_code_products_entry_var = StringVar()
        self.client_code_products_entry = ttk.Entry(self.root.frame1, textvariable=self.client_code_products_entry_var,
                                                    width=15)
        self.find_btn = ttk.Button(self.root.frame1, text='FIND', width=15)

    def setup_layout(self):
        self.client_code_products_label.grid(column=0, row=1, sticky=(N, W), pady=2, padx=10)
        self.client_code_products_entry.grid(column=1, row=1, sticky=(N))
        self.find_btn.grid(column=1, row=2, sticky=(N))

class ProductsByClientTreeview(ttk.Frame,Tk):
    def __init__(self, parent, ctrl):
        super().__init__()
        self.root = parent
        self.ctrl = ctrl

    def setup(self):
        self.create_widgets()
        self.setup_layout()

    def create_widgets(self):
        self.tv = ttk.Treeview(self.root.frame1, columns=(1, 2, 3, 4, 5, 6), show='headings')
        self.ybar = ttk.Scrollbar(self.root.frame1, orient='vertical', command=self.tv.yview)
        self.tv.configure(yscroll=self.ybar.set)
        self.tv['columns'] = ('code', 'name', 'client_code', 'quantity', 'volume', 'weight')
        self.tv.column('#0', width=0, stretch=NO)
        self.tv.column('code', anchor=CENTER, width=180)
        self.tv.column('name', anchor=CENTER, width=180)
        self.tv.column('client_code', anchor=CENTER, width=180)
        self.tv.column('quantity', anchor=CENTER, width=180)
        self.tv.column('volume', anchor=CENTER, width=180)
        self.tv.column('weight', anchor=CENTER, width=180)

        self.tv.heading('#0', text='', anchor=CENTER)
        self.tv.heading('code', text='CODE', anchor=CENTER)
        self.tv.heading('name', text='NAME', anchor=CENTER)
        self.tv.heading('client_code', text='CLIENT CODE', anchor=CENTER)
        self.tv.heading('quantity', text='QUANTITY', anchor=CENTER)
        self.tv.heading('volume', text='VOLUME', anchor=CENTER)
        self.tv.heading('weight', text='WEIGHT', anchor=CENTER)

        self.ybar.configure(command=self.tv.yview)

        for i in self.tv.get_children():
            self.tv.delete(i)

    def setup_layout(self):
        self.tv.grid(column=0, row=0, columnspan=6, sticky=(N, S, E, W))
        self.ybar.grid(column=7, row=0, sticky='nse')

    def insert_in_treeview(self, indexes, products):
        tv_index = -1
        for i in indexes:
            tv_index += 1
            prod = products[i]
            self.tv.insert('', tv_index, values=(products[i]['code'], products[i]['name'], products[i]['client_code'],
                                                 products[i]['quantity'], products[i]['volume'], products[i]['weight']))

#======================================================================
class AddProductView(ttk.Frame,Tk):
    def __init__(self, parent, ctrl):
        super().__init__()
        self.root = parent
        self.ctrl = ctrl

    def setup(self):
        self.create_widgets()
        self.setup_layout()

    def create_widgets(self):
        self.code_label = ttk.Label(self.root.frame1, text='PRODUCT CODE')
        self.name_label = ttk.Label(self.root.frame1, text='NAME')
        self.client_code_label = ttk.Label(self.root.frame1, text='CLIENT CODE')
        self.quantity_label = ttk.Label(self.root.frame1, text='QUANTITY')
        self.volume_label = ttk.Label(self.root.frame1, text='VOLUME')
        self.weight_label = ttk.Label(self.root.frame1, text='WEIGHT')

        self.code_entry_var = StringVar()
        self.name_entry_var = StringVar()
        self.client_code_entry_var = StringVar()
        self.quantity_entry_var = StringVar()
        self.volume_entry_var = StringVar()
        self.weight_entry_var = StringVar()

        self.code_entry = ttk.Entry(self.root.frame1, textvariable=self.code_entry_var)
        self.name_entry = ttk.Entry(self.root.frame1, textvariable=self.name_entry_var)
        self.client_code_entry = ttk.Entry(self.root.frame1, textvariable=self.client_code_entry_var)
        self.quantity_entry = ttk.Entry(self.root.frame1, textvariable=self.quantity_entry_var)
        self.volume_entry = ttk.Entry(self.root.frame1, textvariable=self.volume_entry_var)
        self.weight_entry = ttk.Entry(self.root.frame1, textvariable=self.weight_entry_var)

        self.add_btn = ttk.Button(self.root.frame1, text='SUBMIT', width=15)


    def setup_layout(self):
        self.code_label.grid(column=0, row=1, sticky=(N, W))
        self.name_label.grid(column=0, row=2, sticky=(N, W))
        self.client_code_label.grid(column=0, row=3, sticky=(N, W), )
        self.quantity_label.grid(column=0, row=4, sticky=(N, W))
        self.volume_label.grid(column=0, row=5, sticky=(N, W))
        self.weight_label.grid(column=0, row=6, sticky=(N, W))
        self.code_entry.grid(column=1, row=1, sticky=(N))
        self.name_entry.grid(column=1, row=2, sticky=(N))
        self.client_code_entry.grid(column=1, row=3, sticky=(N))
        self.quantity_entry.grid(column=1, row=4, sticky=(N))
        self.volume_entry.grid(column=1, row=5, sticky=(N))
        self.weight_entry.grid(column=1, row=6, sticky=(N))
        self.add_btn.grid(column=1, row=7, sticky=(N))

#======================================================================
class DeleteProductView(ttk.Frame,Tk):
    def __init__(self, parent, ctrl):
        super().__init__()
        self.root = parent
        self.ctrl = ctrl

    def setup(self):
        self.create_widgets()
        self.setup_layout()

    def create_widgets(self):
        self.product_code_label = ttk.Label(self.root.frame1, text='PRODUCT CODE')
        self.product_code_entry_var = StringVar()
        self.product_code_entry = ttk.Entry(self.root.frame1, textvariable=self.product_code_entry_var, width=15)

        self.delete_btn = ttk.Button(self.root.frame1, text='DELETE', width=15)


    def setup_layout(self):
        self.product_code_label.grid(column=0, row=1, sticky=(N, W), pady=2, padx=10)
        self.product_code_entry.grid(column=1, row=1, sticky=(N))
        self.delete_btn.grid(column=1, row=2, sticky=(N))

#======================================================================
class UpdateProductView(ttk.Frame,Tk):
    def __init__(self, parent, ctrl):
        super().__init__()
        self.root = parent
        self.ctrl = ctrl


    def setup(self):
        self.create_widgets()
        self.setup_layout()

    def create_widgets(self):
        self.code_label = ttk.Label(self.root.frame1, text='PRODUCT CODE')
        self.update_code_entry_var = StringVar()
        self.code_entry = ttk.Entry(self.root.frame1, textvariable=self.update_code_entry_var)
        self.update_btn = ttk.Button(self.root.frame1, text='UPDATE', width=15)

    def setup_layout(self):
        self.code_label.grid(column=0, row=1, sticky=(N, W))
        self.code_entry.grid(column=1, row=1, sticky=(N))
        self.update_btn.grid(column=1, row=2, sticky=(N))

class UpdateProductDataView(ttk.Frame,Tk):
    def __init__(self, parent, ctrl):
        super().__init__()
        self.root = parent
        self.ctrl = ctrl

    def setup(self):
        self.create_widgets()
        self.setup_layout()

    def create_widgets(self):
        # self.update_btn.destroy()
        self.code_label = ttk.Label(self.root.frame1, text='PRODUCT CODE')
        self.name_label = ttk.Label(self.root.frame1, text='NAME')
        self.client_code_label = ttk.Label(self.root.frame1, text='CLIENT CODE')
        self.quantity_label = ttk.Label(self.root.frame1, text='QUANTITY')
        self.volume_label = ttk.Label(self.root.frame1, text='VOLUME')
        self.weight_label = ttk.Label(self.root.frame1, text='WEIGHT')

        self.update_code_entry_var = StringVar()
        self.update_name_entry_var = StringVar()
        self.update_client_code_entry_var = StringVar()
        self.update_quantity_entry_var = StringVar()
        self.update_volume_entry_var = StringVar()
        self.update_weight_entry_var = StringVar()

        self.update_code_entry = ttk.Entry(self.root.frame1, textvariable=self.update_code_entry_var)
        self.update_name_entry = ttk.Entry(self.root.frame1, textvariable=self.update_name_entry_var)
        self.update_client_code_entry = ttk.Entry(self.root.frame1, textvariable=self.update_client_code_entry_var)
        self.update_quantity_entry = ttk.Entry(self.root.frame1, textvariable=self.update_quantity_entry_var)
        self.update_volume_entry = ttk.Entry(self.root.frame1, textvariable=self.update_volume_entry_var)
        self.update_weight_entry = ttk.Entry(self.root.frame1, textvariable=self.update_weight_entry_var)
        self.save_btn = ttk.Button(self.root.frame1, text='SAVE', width=15)

    def setup_layout(self):
        self.code_label.grid(column=0, row=1, sticky=(N, W))
        self.update_code_entry.grid(column=1, row=1, sticky=(N))
        self.name_label.grid(column=0, row=2, sticky=(N, W))
        self.client_code_label.grid(column=0, row=3, sticky=(N, W), )
        self.quantity_label.grid(column=0, row=4, sticky=(N, W))
        self.volume_label.grid(column=0, row=5, sticky=(N, W))
        self.weight_label.grid(column=0, row=6, sticky=(N, W))
        self.update_name_entry.grid(column=1, row=2, sticky=(N))
        self.update_client_code_entry.grid(column=1, row=3, sticky=(N))
        self.update_quantity_entry.grid(column=1, row=4, sticky=(N))
        self.update_volume_entry.grid(column=1, row=5, sticky=(N))
        self.update_weight_entry.grid(column=1, row=6, sticky=(N))
        self.save_btn.grid(column=1, row=7, sticky=(N))

#======================================================================
# ========================= ADMIN LOCATIONS VIEWS =====================
class AdminLocationsWindow(ttk.Frame):
    def __init__(self, parent, ctrl):
        super().__init__()
        self.root = parent
        self.ctrl = ctrl

    def setup(self):
        self.create_widgets()
        self.setup_layout()

    def create_widgets(self):

        self.lst_all_locations = ttk.Button(self.root.frame1, text='List All Locations')
        self.add_location = ttk.Button(self.root.frame1, text='Add Location')
        self.delete_location = ttk.Button(self.root.frame1, text='Delete Location')
        self.update_location = ttk.Button(self.root.frame1, text='Update Location')

    def setup_layout(self):
        self.lst_all_locations.grid(row=8, column=0, sticky=(S, W))
        self.add_location.grid(row=8, column=1, sticky=(S, W))
        self.delete_location.grid(row=8, column=2, sticky=(S, W))
        self.update_location.grid(row=8, column=3, sticky=(S, W))

#======================================================================
class ListAllLocationsView(ttk.Frame,Tk):
    def __init__(self, parent, ctrl):
        super().__init__()
        self.root = parent
        self.ctrl = ctrl

    def setup(self):
        self.create_widgets()
        self.setup_layout()

    def create_widgets(self):
        self.tv = ttk.Treeview(self.root.frame1, columns=(1, 2, 3), show='headings')
        self.ybar = ttk.Scrollbar(self.root.frame1, orient='vertical', command=self.tv.yview)
        self.tv.configure(yscroll=self.ybar.set)

        self.tv['columns'] = ('ID', 'WAREHOUSE', 'REGAL')
        self.tv.column('#0', width=0, stretch=NO)
        self.tv.column('ID', anchor=CENTER, width=180)
        self.tv.column('WAREHOUSE', anchor=CENTER, width=180)
        self.tv.column('REGAL', anchor=CENTER, width=180)

        self.tv.heading('#0', text='', anchor=CENTER)
        self.tv.heading('ID', text='ID', anchor=CENTER)
        self.tv.heading('WAREHOUSE', text='CLIENT CODE', anchor=CENTER)
        self.tv.heading('REGAL', text='PRODUCT CODE')


        self.ybar.configure(command=self.tv.yview)
        for i in self.tv.get_children():
            self.tv.delete(i)

    def setup_layout(self):
        self.tv.grid(column=0, row=0, columnspan=4, sticky=(N, S, E, W))
        self.ybar.grid(column=4, row=0, sticky='nse')

    def insert_in_treeview(self, locations):
        for index, loc in enumerate(locations):  # loc = location
            self.tv.insert('', index, values=(loc['id'], loc['warehouse'], loc['regal']))

#======================================================================
class AddLocationView(ttk.Frame,Tk):
    def __init__(self, parent, ctrl):
        super().__init__()
        self.root = parent
        self.ctrl = ctrl

    def setup(self):
        self.create_widgets()
        self.setup_layout()

    def create_widgets(self):
        self.warehouse_label_add = ttk.Label(self.root.frame1, text='WAREHOUSE')
        self.regal_label_add = ttk.Label(self.root.frame1, text='REGAL')
        self.warehouse_entry_var = StringVar()
        self.regal_entry_var = StringVar()
        self.warehouse_entry = ttk.Entry(self.root.frame1, textvariable=self.warehouse_entry_var)
        self.regal_entry = ttk.Entry(self.root.frame1, textvariable=self.regal_entry_var)

        self.add_btn = ttk.Button(self.root.frame1, text='SUBMIT', width=15)

    def setup_layout(self):
        self.warehouse_label_add.grid(column=0, row=1, sticky=(N, W))
        self.regal_label_add.grid(column=0, row=2, sticky=(N, W))
        self.warehouse_entry.grid(column=1, row=1, sticky=(N))
        self.regal_entry.grid(column=1, row=2, sticky=(N))
        self.add_btn.grid(column=1, row=3, sticky=(N))

#======================================================================
class DeleteLocation(ttk.Frame,Tk):
    def __init__(self, parent, ctrl):
        super().__init__()
        self.root = parent
        self.ctrl = ctrl

    def setup(self):
        self.create_widgets()
        self.setup_layout()

    def create_widgets(self):
        self.id_location_label = ttk.Label(self.root.frame1, text='ID')
        self.id_location_entry_var = StringVar()
        self.id_location_entry = ttk.Entry(self.root.frame1, textvariable=self.id_location_entry_var)
        self.delete_btn = ttk.Button(self.root.frame1, text='DELETE', width=15)


    def setup_layout(self):
        self.id_location_label.grid(column=0, row=1, sticky=(N, W, E))
        self.id_location_entry.grid(column=1, row=1, sticky=(N))
        self.delete_btn.grid(column=1, row=3, sticky=(N))

#======================================================================
class UpdateLocationView(ttk.Frame,Tk):
    def __init__(self, parent, ctrl):
        super().__init__()
        self.root = parent
        self.ctrl = ctrl

    def setup(self):
        self.create_widgets()
        self.setup_layout()

    def create_widgets(self):
        self.id_location_label = ttk.Label(self.root.frame1, text='ID')
        self.id_location_entry_var = StringVar()
        self.id_location_entry = ttk.Entry(self.root.frame1, textvariable=self.id_location_entry_var)
        self.update_btn = ttk.Button(self.root.frame1, text='UPDATE', width=15)

    def setup_layout(self):
        self.id_location_label.grid(column=0, row=1, sticky=(N, W, E))
        self.id_location_entry.grid(column=1, row=1, sticky=(N))
        self.update_btn.grid(column=1, row=3, sticky=(N))

class UpdateLocationDataView(ttk.Frame,Tk):
    def __init__(self, parent, ctrl):
        super().__init__()
        self.root = parent
        self.ctrl = ctrl

    def setup(self):
        self.create_widgets()
        self.setup_layout()

    def create_widgets(self):
        self.warehouse_label_add = ttk.Label(self.root.frame1, text='WAREHOUSE')
        self.regal_label_add = ttk.Label(self.root.frame1, text='REGAL')
        self.warehouse_entry_var = StringVar()
        self.regal_entry_var = StringVar()
        self.warehouse_entry = ttk.Entry(self.root.frame1, textvariable=self.warehouse_entry_var)
        self.regal_entry = ttk.Entry(self.root.frame1, textvariable=self.regal_entry_var)
        self.add_btn = ttk.Button(self.root.frame1, text='SAVE', width=15)

    def setup_layout(self):
        self.warehouse_label_add.grid(column=0, row=1, sticky=(N, W))
        self.regal_label_add.grid(column=0, row=2, sticky=(N, W))
        self.warehouse_entry.grid(column=1, row=1, sticky=(N))
        self.regal_entry.grid(column=1, row=2, sticky=(N))
        self.add_btn.grid(column=1, row=3, sticky=(N))
