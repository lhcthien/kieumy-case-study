from tkinter import ttk

# import tk as tk
from PIL import ImageTk
from tkinter import *


class ClientMainView(ttk.Frame):
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
        self.frame1 = ttk.Frame(self.container, borderwidth=5, relief="ridge")

    def setup(self):
        self.container = ttk.Frame(self.root, padding=(3, 3, 12, 12))
        self.frame1 = ttk.Frame(self.container, borderwidth=5, relief="ridge")
        self.create_widgets()
        self.setup_layout()

    def create_widgets(self):
        # self.container = ttk.Frame(self.root, padding=(3, 3, 12, 12))
        # self.frame1 = ttk.Frame(self.container, borderwidth=5, relief="ridge")
        self.place_inbound_order_btn = ttk.Button(self.container, text="PLACE INBOUND", style='Mitko.TButton')

        self.place_outbound_order_btn = ttk.Button(self.container, text="PLACE OUTBOUND", style='Mitko.TButton')

        self.placed_inbounds_btn = ttk.Button(self.container, text="PLACED INBOUNDS", style='Mitko.TButton')

        self.placed_outbounds_btn = ttk.Button(self.container, text="PLACED OUTBOUNDS", style='Mitko.TButton')

        self.list_all_products_btn = ttk.Button(self.container, text="ALL PRODUCTS", style='Mitko.TButton')

        self.logout = ttk.Button(self.container, text="Logout")
        self.username_label = ttk.Label(self.container, text=self.username_label_text)
        self.role_label = ttk.Label(self.container, text=self.role_label_text)

        self.tv = ttk.Treeview(self.frame1, columns=(1, 2, 3, 4, 5, 6), show='headings')

    def setup_layout(self):
        self.username_label.grid(column=2, row=7, sticky=(N, W), pady=2, padx=10)
        self.role_label.grid(column=3, row=7, sticky=(N, W), pady=2, padx=10)
        self.container.grid(column=0, row=0, sticky=(N, S, E, W))
        self.frame1.grid(column=2, row=0, columnspan=4, rowspan=6, sticky=(N, S, E, W))
        self.place_inbound_order_btn.grid(column=0, row=0, columnspan=2, sticky=(N, E, W), pady=5, padx=5)
        self.place_outbound_order_btn.grid(column=0, row=1, columnspan=2, sticky=(N, E, W), pady=5, padx=5)
        self.placed_inbounds_btn.grid(column=0, row=2, columnspan=2, sticky=(N, E, W), pady=5, padx=5)
        self.placed_outbounds_btn.grid(column=0, row=3, columnspan=2, sticky=(N, E, W), pady=5, padx=5)
        self.list_all_products_btn.grid(column=0, row=5, columnspan=2, sticky=(N, E, W), pady=5, padx=5)
        self.tv.grid(column=0, row=0, columnspan=6, rowspan=6, sticky=(N, S, E, W))
        self.logout.grid(column=1, row=7, sticky=W)

        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

    def clear_frame(self):
        for widgets in self.frame1.winfo_children():
            widgets.destroy()


# ======================== CLIENT PLACE INBOUND ORDER ===========================
class ClientPlaceInboundOrderView(ttk.Frame, Tk):
    def __init__(self, parent, ctrl):
        super().__init__()
        self.root = parent
        self.ctrl = ctrl
        # self.frame = frame
        self.inbound_products_lst = []

    # def clear_frame_forget(self):
    #     for widgets in self.root.frame1.winfo_children():
    #         widgets.forget()

    def clear_frame(self):
        for widgets in self.root.frame1.winfo_children():
            widgets.destroy()

    def setup(self):
        # self.clear_frame()
        self.create_widgets()
        self.setup_layout()

    def create_widgets(self):
        # self.clear_frame()
        self.client_code_label = ttk.Label(self.root.frame1, text='CLIENT CODE')
        self.time_label = ttk.Label( self.root.frame1, text='DATE DD.MM.YYYY')
        self.status_label = ttk.Label(self.root.frame1, text='STATUS')
        self.location_label = ttk.Label(self.root.frame1, text='LOCATION')
        self.product_label = ttk.Label(self.root.frame1, text='PRODUCT')

        self.client_code_entry_var = StringVar()
        self.time_entry_var = StringVar()
        self.status_entry_var = StringVar()
        self.location_entry_var = StringVar()
        self.product_entry_var = StringVar()
        # self.product_entry_var.set('code/name/quantity')

        self.client_code_entry = ttk.Entry(self.root.frame1, textvariable=self.client_code_entry_var)
        self.time_entry = ttk.Entry(self.root.frame1, textvariable=self.time_entry_var)
        self.status_entry = ttk.Entry(self.root.frame1, textvariable=self.status_entry_var)
        self.location_entry = ttk.Entry(self.root.frame1, textvariable=self.location_entry_var)
        self.product_entry_btn = ttk.Button(self.root.frame1, text='ADD PRODUCTS', width=20)

    def setup_layout(self):
        self.client_code_label.grid(column=0, row=1, sticky=(N, W))
        self.time_label.grid(column=0, row=2, sticky=(N, W))
        self.status_label.grid(column=0, row=3, sticky=(N, W))
        self.location_label.grid(column=0, row=4, sticky=(N, W))
        self.product_label.grid(column=0, row=5, sticky=(N, W))
        self.client_code_entry.grid(column=1, row=1, sticky=(N))
        self.time_entry.grid(column=1, row=2, sticky=(N))
        self.status_entry.grid(column=1, row=3, sticky=(N))
        self.location_entry.grid(column=1, row=4, sticky=(N))
        # self.product_entry.grid(column=1, row=5, sticky=(N))
        self.product_entry_btn.grid(column=1, row=5, sticky=(N))
        self.root.frame1.grid(column=2,row=0, columnspan=8, sticky=(N, S, E, W))

        self.root.frame1.columnconfigure(0,weight=1)


class AddProductsToInboundOrderView(ttk.Frame, Tk):
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
        for i in self.root.frame1.winfo_children():
            if str(i) == '.!frame2.!frame.!button':
                i['state'] = "disabled"
            # print(i)

        # self.root.frame1[10]['state'] = "disabled"
        self.product_code_label = ttk.Label(self.root.frame1, text='PRODUCT CODE')
        self.product_name_label = ttk.Label(self.root.frame1, text='PRODUCT NAME')
        self.product_quantity_label = ttk.Label(self.root.frame1, text='QUANTITY')

        self.product_code_var = StringVar()
        self.product_name_var = StringVar()
        self.product_quantity_var = StringVar()

        self.product_code_entry = ttk.Entry(self.root.frame1, textvariable=self.product_code_var)
        self.product_name_entry = ttk.Entry(self.root.frame1, textvariable=self.product_name_var)
        self.product_quantity_entry = ttk.Entry(self.root.frame1, textvariable=self.product_quantity_var)

        self.save_btn_add = ttk.Button(self.root.frame1, text='ADD TO INBOUND', width=20)

        self.save_btn = ttk.Button(self.root.frame1, text='SUBMIT', width=20)

    def setup_layout(self):
        self.product_code_label.grid(column=0, row=7, sticky=(N, W))
        self.product_name_label.grid(column=0, row=8, sticky=(N, W))
        self.product_quantity_label.grid(column=0, row=9, sticky=(N, W), )
        self.product_code_entry.grid(column=1, row=7, sticky=N)
        self.product_name_entry.grid(column=1, row=8, sticky=N)
        self.product_quantity_entry.grid(column=1, row=9, sticky=N)
        self.save_btn_add.grid(column=1, row=10, sticky=N)
        self.save_btn.grid(column=1, row=11, sticky=N)

# ======================== CLIENT PLACE OUTBOUND ORDER ===========================
class ClientPlaceOutboundOrderView(ttk.Frame, Tk):
    def __init__(self, parent, ctrl):
        super().__init__()
        self.root = parent
        self.ctrl = ctrl
        self.outbound_products_lst = []

    def clear_frame(self):
        for widgets in self.root.winfo_children():
            widgets.destroy()

    def setup(self):
        # self.clear_frame_destroy()
        self.create_widgets()
        self.setup_layout()

    def create_widgets(self):
        self.client_code_label = ttk.Label(self.root.frame1, text='CLIENT CODE')
        self.time_label = ttk.Label(self.root.frame1, text='DATE DD.MM.YYYY')
        self.status_label = ttk.Label(self.root.frame1, text='STATUS')
        self.location_label = ttk.Label(self.root.frame1, text='LOCATION')
        self.product_label = ttk.Label(self.root.frame1, text='PRODUCT')

        self.client_code_entry_var = StringVar()
        self.time_entry_var = StringVar()
        self.status_entry_var = StringVar()
        self.location_entry_var = StringVar()
        self.product_entry_var = StringVar()
        # self.product_entry_var.set('code/name/quantity')

        self.client_code_entry = ttk.Entry(self.root.frame1, textvariable=self.client_code_entry_var)
        self.time_entry = ttk.Entry(self.root.frame1, textvariable=self.time_entry_var)
        self.status_entry = ttk.Entry(self.root.frame1, textvariable=self.status_entry_var)
        self.location_entry = ttk.Entry(self.root.frame1, textvariable=self.location_entry_var)
        self.product_entry_btn = ttk.Button(self.root.frame1, text='ADD PRODUCTS', width=20)

    def setup_layout(self):
        self.client_code_label.grid(column=0, row=1, sticky=(N, W))
        self.time_label.grid(column=0, row=2, sticky=(N, W))
        self.status_label.grid(column=0, row=3, sticky=(N, W))
        self.location_label.grid(column=0, row=4, sticky=(N, W))
        self.product_label.grid(column=0, row=5, sticky=(N, W))
        self.client_code_entry.grid(column=1, row=1, sticky=(N))
        self.time_entry.grid(column=1, row=2, sticky=(N))
        self.status_entry.grid(column=1, row=3, sticky=(N))
        self.location_entry.grid(column=1, row=4, sticky=(N))
        # self.product_entry.grid(column=1, row=5, sticky=(N))
        self.product_entry_btn.grid(column=1, row=5, sticky=(N))

class AddProductsToOutboundOrderView(ttk.Frame, Tk):
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
        for i in self.root.frame1.winfo_children():
            if str(i) == '.!frame2.!frame.!button':
                i['state'] = "disabled"
            print(i)
        # self.product_entry_btn['state'] = "disabled"
        self.product_code_label = ttk.Label(self.root.frame1, text='PRODUCT CODE')
        self.product_name_label = ttk.Label(self.root.frame1, text='PRODUCT NAME')
        self.product_quantity_label = ttk.Label(self.root.frame1, text='QUANTITY')

        self.product_code_var = StringVar()
        self.product_name_var = StringVar()
        self.product_quantity_var = StringVar()

        self.product_code_entry = ttk.Entry(self.root.frame1, textvariable=self.product_code_var)
        self.product_name_entry = ttk.Entry(self.root.frame1, textvariable=self.product_name_var)
        self.product_quantity_entry = ttk.Entry(self.root.frame1, textvariable=self.product_quantity_var)

        self.save_btn_add = ttk.Button(self.root.frame1, text='ADD TO OUTBOUND', width=20)

        self.save_btn = ttk.Button(self.root.frame1, text='SUBMIT', width=20)

    def setup_layout(self):
        self.product_code_label.grid(column=0, row=6, sticky=(N, W))
        self.product_name_label.grid(column=0, row=7, sticky=(N, W))
        self.product_quantity_label.grid(column=0, row=8, sticky=(N, W), )
        self.product_code_entry.grid(column=1, row=6, sticky=N)
        self.product_name_entry.grid(column=1, row=7, sticky=N)
        self.product_quantity_entry.grid(column=1, row=8, sticky=N)
        self.save_btn_add.grid(column=1, row=9, sticky=N)
        self.save_btn.grid(column=1, row=10, sticky=N)

# ======================== CLIENT PLACED INBOUNDS ===========================
class PlacedInboundsView(ttk.Frame, Tk):
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
        self.ybar.grid(column=7, row=0, sticky='nse')

    def insert_in_treeview(self,indexes, inbounds, p_in_inbound):
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

# ======================== CLIENT PLACED OUTBOUNDS ===========================
class PlacedOutboundsView(ttk.Frame, Tk):
    def __init__(self, parent, ctrl):
        super().__init__()
        self.root = parent
        self.ctrl = ctrl
        self.outbound_products_lst = []

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
        for i in self.tv.get_children():
            self.tv.delete(i)

    def setup_layout(self):
        self.tv.grid(column=0, row=0, columnspan=7, sticky=(N, S, E, W))
        self.ybar.grid(column=7, row=0, sticky='nse')

    def insert_in_treeview(self,indexes, outbounds, p_in_outbound):
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

# ======================== CLIENT PLACED OUTBOUNDS ===========================
class ListAllProductsView(ttk.Frame, Tk):
    def __init__(self, parent, ctrl):
        super().__init__()
        self.root = parent
        self.ctrl = ctrl
        self.outbound_products_lst = []

    def clear_frame(self):
        for widgets in self.root.frame1.winfo_children():
            widgets.destroy()

    def setup(self):
        # self.clear_frame_destroy()
        self.create_widgets()
        self.setup_layout()

    def create_widgets(self):
        # self.clear_frame()
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
            self.tv.insert('', tv_index, values=(products[i]['code'], products[i]['name'], products[i]['client_code'],
                                                 products[i]['quantity'], products[i]['volume'], products[i]['weight']))




