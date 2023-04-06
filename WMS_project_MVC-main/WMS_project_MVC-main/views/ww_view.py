from tkinter import ttk

# import tk as tk
from PIL import ImageTk
from tkinter import *


class WarehouseWorkerMainView(ttk.Frame):
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
        self.container = ttk.Frame(self.root, padding=(3, 3, 12, 12))
        self.frame1 = ttk.Frame(self.container, borderwidth=5, relief="ridge",width=1200)

    def setup(self):
        self.container = ttk.Frame(self.root, padding=(3, 3, 12, 12))
        self.frame1 = ttk.Frame(self.container, borderwidth=5, relief="ridge")
        self.create_widgets()
        self.setup_layout()

    def create_widgets(self):
        self.placed_inbounds_btn = ttk.Button(self.container, text="PLACED INBOUNDS", style='Mitko.TButton')

        self.placed_outbounds_btn = ttk.Button(self.container, text="PLACED OUTBOUNDS", style='Mitko.TButton')

        self.accepted_inbounds_btn = ttk.Button(self.container, text="ACCEPTED INBOUNDS", style='Mitko.TButton')

        self.accepted_outbounds_btn = ttk.Button(self.container, text="ACCEPTED OUTBOUNDS", style='Mitko.TButton')

        self.change_location_btn = ttk.Button(self.container, text="CHANGE LOCATION", style='Mitko.TButton')

        self.logout = ttk.Button(self.container, text="Logout")
        self.username_label = ttk.Label(self.container, text=self.username_label_text)
        self.role_label = ttk.Label(self.container, text=self.role_label_text)

        self.tv = ttk.Treeview(self.frame1, columns=(1, 2, 3, 4, 5, 6), show='headings')

    def setup_layout(self):
        self.username_label.grid(column=2, row=6, sticky=(N, W), pady=2, padx=10)
        self.role_label.grid(column=3, row=6, sticky=(N, W), pady=2, padx=10)
        self.container.grid(column=0, row=0, sticky=(N, S, E, W))
        self.frame1.grid(column=2, row=0, columnspan=4, rowspan=6, sticky=(N, S, E, W))
        self.placed_inbounds_btn.grid(column=0, row=0, columnspan=2, sticky=(N, E, W), pady=5, padx=5)
        self.placed_outbounds_btn.grid(column=0, row=1, columnspan=2, sticky=(N, E, W), pady=5, padx=5)
        self.accepted_inbounds_btn.grid(column=0, row=2, columnspan=2, sticky=(N, E, W), pady=5, padx=5)
        self.accepted_outbounds_btn.grid(column=0, row=3, columnspan=2, sticky=(N, E, W), pady=5, padx=5)
        self.change_location_btn.grid(column=0, row=5, columnspan=2, sticky=(N, E, W), pady=5, padx=5)
        self.tv.grid(column=0, row=0, columnspan=6, rowspan=6, sticky=(N, S, E, W))
        self.logout.grid(column=1, row=6, sticky=(W))

        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

    def clear_frame(self):
        for widgets in self.frame1.winfo_children():
            widgets.destroy()


# ============================== PLACED INBOUNDS VIEW =======================
class PlacedInboundOrderView(ttk.Frame, Tk):
    def __init__(self, parent, ctrl):
        super().__init__()
        self.root = parent
        self.ctrl = ctrl
        self.selected_item_id = 0

    def clear_frame(self):
        for widgets in self.root.winfo_children():
            widgets.destroy()

    def setup(self):
        # self.clear_frame_destroy()
        self.create_widgets()
        self.setup_layout()

    def create_widgets(self):
        self.tv = ttk.Treeview(self.root.frame1, columns=(1, 2, 3, 4, 5, 6, 7), show='headings')
        self.tv['columns'] = ('INBOUND/PRODUCT','ID','CLIENT_CODE','QUANTITY','DATE','STATUS','LOCATION')
        self.tv.column('#0',width=0,stretch=NO)
        self.tv.column('INBOUND/PRODUCT', anchor=CENTER, width=180)
        self.tv.column('ID', anchor=CENTER, width=100)
        self.tv.column('CLIENT_CODE', anchor=CENTER, width=100)
        self.tv.column('QUANTITY', anchor=CENTER, width=100)
        self.tv.column('DATE', anchor=CENTER, width=100)
        self.tv.column('STATUS', anchor=CENTER, width=100)
        self.tv.column('LOCATION', anchor=CENTER, width=100)

        self.tv.heading('#0',text='',anchor=CENTER)
        self.tv.heading('INBOUND/PRODUCT',text='INBOUND/PRODUCT', anchor=CENTER)
        self.tv.heading('ID', text='ID')
        self.tv.heading('CLIENT_CODE', text='CLIENT CODE')
        self.tv.heading('QUANTITY', text='QUANTITY')
        self.tv.heading('DATE', text='DATE')
        self.tv.heading('STATUS', text='STATUS')
        self.tv.heading('LOCATION', text='LOCATION')


        self.ybar = ttk.Scrollbar(self.root.frame1, orient='vertical', command=self.tv.yview)
        self.tv.configure(yscroll=self.ybar.set)
        self.ybar.configure(command=self.tv.yview)
        self.tv.bind('<<TreeviewSelect>>', self.item_selected_inbound)
        for i in self.tv.get_children():
            self.tv.delete(i)
        self.lst_all_locations = ttk.Button(self.root.frame1, text='ACCEPT')

    def get_id_of_the_selected_item(self):
        id = 0
        for selected_item in self.tv.selection():
            item = self.tv.item(selected_item)
            record = item['values']
            product = record[3]
            id = record[1] - 1
        return id

    def setup_layout(self):
        self.tv.grid(column=0, row=0, sticky='nsew')
        self.ybar.grid(column=9, row=0, sticky='nse')
        self.lst_all_locations.grid(row=8, column=0, sticky=(S, W))

    def item_selected_inbound(self, event):
        self.selected_item_id = self.get_id_of_the_selected_item() - 1
        print(self.selected_item_id)

    def insert_in_treeview(self, new_inbounds, p_in_inbound):
        id = 0
        iid = 0
        tv_index = -1
        for i,inbound in enumerate(new_inbounds):
            tv_index += 1
            parent = self.tv.insert('', tv_index,
                                    values=('INBOUND', inbound['id'], inbound['client_code'], p_in_inbound[i],
                                            inbound['time'],inbound['status'], inbound['location']))
            # self.iid = self.iid + 1
            # self.id = self.id + 1
            for item in inbound['products']:
                tv_index += 1
                self.tv.insert(parent, tv_index, values=('Product', item['code'], item['name'], item['quantity']))
                # self.iid = self.iid + 1
                # self.id = self.id + 1

# ============================== PLACED OUTBOUNDS VIEW =======================
class PlacedOutboundOrderView(ttk.Frame, Tk):
    def __init__(self, parent, ctrl):
        super().__init__()
        self.root = parent
        self.ctrl = ctrl
        self.selected_item_id = 0

    def clear_frame(self):
        for widgets in self.root.winfo_children():
            widgets.destroy()

    def setup(self):
        # self.clear_frame_destroy()
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
        self.tv.bind('<<TreeviewSelect>>', self.item_selected_outbound)
        for i in self.tv.get_children():
            self.tv.delete(i)
        self.lst_all_locations = ttk.Button(self.root.frame1, text='HAND OVER')

    def get_id_of_the_selected_item(self):
        id = 0
        for selected_item in self.tv.selection():
            item = self.tv.item(selected_item)
            record = item['values']
            product = record[3]
            id = record[1] - 1
        return id

    def setup_layout(self):
        self.tv.grid(column=0, row=0, sticky='nsew')
        self.ybar.grid(column=8, row=0, sticky='nse')
        self.lst_all_locations.grid(row=8, column=0, sticky=(S, W))

    def item_selected_outbound(self, event):
        self.selected_item_id = self.get_id_of_the_selected_item()

    def insert_in_treeview(self, new_outbounds, p_in_outbound):
        id = 0
        iid = 0
        tv_index = -1
        for i,outbound in enumerate(new_outbounds):
            tv_index += 1
            parent = self.tv.insert('', tv_index,
                                    values=('OUTBOUND', outbound['id'], outbound['client_code'], p_in_outbound[i],
                                            outbound['time'],outbound['status'], outbound['location']))
            # self.iid = self.iid + 1
            # self.id = self.id + 1
            for item in outbound['products']:
                tv_index += 1
                self.tv.insert(parent, tv_index, values=('Product', item['code'], item['name'], item['quantity']))

# ============================ ACCEPTED INBOUNDS VIEW ========================
class AcceptedInboundsView(ttk.Frame, Tk):
    def __init__(self, parent, ctrl):
        super().__init__()
        self.root = parent
        self.ctrl = ctrl

    def clear_frame(self):
        for widgets in self.root.winfo_children():
            widgets.destroy()

    def setup(self):
        # self.clear_frame_destroy()
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

    def insert_in_treeview(self, acc_inbounds, p_in_inbound):
        # self.id = 0
        # self.iid = 0
        tv_index = -1
        for i,inbound in enumerate(acc_inbounds):
            tv_index += 1
            parent = self.tv.insert('', tv_index,
                                    values=('INBOUND', inbound['id'], inbound['client_code'], p_in_inbound[i],
                                            inbound['time'], inbound['status'], inbound['location']))
            # self.iid = self.iid + 1
            # self.id = self.id + 1
            for item in inbound['products']:
                tv_index += 1
                self.tv.insert(parent, tv_index,
                               values=('Product', item['code'], item['name'], item['quantity']))
                # self.iid = self.iid + 1
                # self.id = self.id + 1

# ============================ ACCEPTED OUTBOUNDS VIEW ========================
class AcceptedOutboundsView(ttk.Frame, Tk):
    def __init__(self, parent, ctrl):
        super().__init__()
        self.root = parent
        self.ctrl = ctrl

    def clear_frame(self):
        for widgets in self.root.winfo_children():
            widgets.destroy()

    def setup(self):
        # self.clear_frame_destroy()
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
        # self.tv.bind('<<TreeviewSelect>>', self.item_selected_outbound)
        for i in self.tv.get_children():
            self.tv.delete(i)

    def setup_layout(self):
        self.tv.grid(column=0, row=0, columnspan=7, sticky=(N, S, E, W))
        self.ybar.grid(column=8, row=0, sticky='nse')

    def insert_in_treeview(self, acc_outbounds, p_in_outbound):
        # self.id = 0
        # self.iid = 0
        tv_index = -1
        for i,outbound in enumerate(acc_outbounds):
            tv_index += 1
            parent = self.tv.insert('', tv_index,
                                    values=('OUTBOUND', outbound['id'], outbound['client_code'], p_in_outbound[i],
                                            outbound['time'], outbound['status'], outbound['location']))
            # self.iid = self.iid + 1
            # self.id = self.id + 1
            for item in outbound['products']:
                tv_index += 1
                self.tv.insert(parent, 'end', iid=self.iid,
                               values=('Product', item['code'], item['name'], item['quantity']))

# ============================ CHANGE LOCATION VIEW ==========================
class ChangeLocationView(ttk.Frame, Tk):
    def __init__(self, parent, ctrl):
        super().__init__()
        self.root = parent
        self.ctrl = ctrl
        self.selected_item_id = 0

    def clear_frame(self):
        for widgets in self.root.winfo_children():
            widgets.destroy()

    def setup(self):
        # self.clear_frame_destroy()
        self.create_widgets()
        self.setup_layout()

    def create_widgets(self):
        self.tv = ttk.Treeview(self.root.frame1, columns=(1, 2, 3, 4, 5, 6, 7), show='headings')
        self.ybar = ttk.Scrollbar(self.root.frame1, orient='vertical', command=self.tv.yview)
        self.tv.configure(yscroll=self.ybar.set)

        self.tv['columns'] = ('ID', 'CLIENT_CODE','PR_CODE','PR_NAME','PR_QUANTITY','WAREHOUSE','REGAL')
        self.tv.column('#0', width=0, stretch=NO)
        self.tv.column('ID', anchor=CENTER, width=100)
        self.tv.column('CLIENT_CODE', anchor=CENTER, width=100)
        self.tv.column('PR_CODE', anchor=CENTER, width=150)
        self.tv.column('PR_NAME', anchor=CENTER, width=150)
        self.tv.column('PR_QUANTITY', anchor=CENTER, width=150)
        self.tv.column('WAREHOUSE', anchor=CENTER, width=100)
        self.tv.column('REGAL', anchor=CENTER, width=100)

        self.tv.heading('#0', text='', anchor=CENTER)
        self.tv.heading('ID', text='ID', anchor=CENTER)
        self.tv.heading('CLIENT_CODE', text='CLIENT CODE', anchor=CENTER)
        self.tv.heading('PR_CODE', text='PRODUCT CODE')
        self.tv.heading('PR_NAME', text='PRODUCT NAME')
        self.tv.heading('PR_QUANTITY', text='PRODUCT QUANTITY')
        self.tv.heading('WAREHOUSE', text='WAREHOUSE')
        self.tv.heading('REGAL', text='REGAL')

        self.ybar.configure(command=self.tv.yview)
        self.tv.bind('<<TreeviewSelect>>', self.item_selected_location)
        for i in self.tv.get_children():
            self.tv.delete(i)
        self.change_loc = ttk.Button(self.root.frame1, text='CHANGE LOCATION')

    def id_check(self):
        for selected_item in self.tv.selection():
           item = self.tv.item(selected_item)
           record = item['values']
           product = record[3]
           self.selected_item_id = record[0] - 1

    def setup_layout(self):
        self.tv.grid(column=0, row=0, sticky='nsew')
        self.ybar.grid(column=8, row=0, sticky='nse')
        self.change_loc.grid(row=8, column=0, sticky=(S, W))

    def item_selected_location(self, event):
        self.id_check()

    def insert_in_treeview(self, available_stock, locations):
        tv_index = -1
        for st in available_stock:
            tv_index += 1
            st_loc = locations[int(st['location_id'])]
            parent = self.tv.insert('', tv_index,
                                    values=(st['id'], st['client_code'], st['product']['code'], st['product']['name'],
                                            st['product']['quantity'], st_loc['warehouse'], st_loc['regal']))


class ChangeLocationActionView(ttk.Frame, Tk):
    def __init__(self, parent, ctrl):
        super().__init__()
        self.root = parent
        self.ctrl = ctrl

    def clear_frame(self):
        for widgets in self.root.winfo_children():
            widgets.destroy()

    def setup(self):
        # self.clear_frame_destroy()
        self.create_widgets()
        self.setup_layout()

    def create_widgets(self):
        # self.clear_frame()
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
        self.tv.heading('REGAL', text='PRODUCT CODE',anchor=CENTER)

        self.ybar.configure(command=self.tv.yview)

        for i in self.tv.get_children():
            self.tv.delete(i)

        self.loc_label_msg = ttk.Label(self.root.frame1, text='CHOOSE LOCATION ID AND ENTER IT IN THE ENTRY')
        self.loc_label = ttk.Label(self.root.frame1, text='ID')
        self.loc_entry_var = StringVar()
        self.loc_entry = ttk.Entry(self.root.frame1, textvariable=self.loc_entry_var)
        self.save_btn = ttk.Button(self.root.frame1, text='SAVE', width=15)

    def insert_in_treeview(self, locations):
        for index, loc in enumerate(locations):  # loc = location
            self.tv.insert('', index, values=(loc['id'], loc['warehouse'], loc['regal']))

    def setup_layout(self):
        self.tv.grid(column=0, row=0, columnspan=4, sticky=(N, S, E, W))
        self.ybar.grid(column=8, row=0, sticky='nse')
        self.loc_label_msg.grid(column=0, row=8, columnspan=2, sticky=(N, W))
        self.loc_label.grid(column=0, row=9, sticky=(N, W))
        self.loc_entry.grid(column=1, row=9, sticky=(N, W))
        self.save_btn.grid(column=1, row=10, sticky=(S, W))











