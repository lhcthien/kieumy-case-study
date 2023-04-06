import json
from functools import reduce
from tkinter import messagebox, END, Tk

from models.user_model import *
from data_files.DbContext import DbContext

class ClientModel:
    def __init__(self, parent, user):
        self.parent = parent
        self.user = user

    def add_products_to_inbound_c(self, view, inbound_products_lst):
        try:
            # TODO Validation for empty strings and digits
            product_code = view.product_code_var.get()
            product_name = view.product_name_var.get()
            product_qty = view.product_quantity_var.get()
            pr = {'code': product_code, 'name': product_name, 'quantity': product_qty}
            inbound_products_lst.append(pr)
            view.product_code_var.set(' '.strip())
            view.product_name_var.set(' '.strip())
            view.product_quantity_var.set(' '.strip())
            return inbound_products_lst
        except AttributeError:
            pass


    def submit_inbound_c(self,view,user,inbound_products_lst):
        inbound_orders = DbContext.load_from_json_file(DbContext.INBOUNDS_DB)
        ids = DbContext.values_from_dictionary(inbound_orders, 'id')
        # indexes = [index for index, x in enumerate(client_codes) if x == 100]
        ee = view.time_entry_var.get()
        new_inbound = {
            "id": f"{int(max(map(lambda x: int(x), ids))) + 1}",
            "client_code": user.code,
            "products": inbound_products_lst,
            "time": view.time_entry_var.get(),
            "status": view.status_entry_var.get(),
            "location": view.location_entry.get()
        }

        inbound_orders.append(new_inbound)

        DbContext.save_in_json_file(DbContext.INBOUNDS_DB, inbound_orders)
        messagebox.showinfo('SUCCESS', 'Successfully add new Inbound Order')
        view.client_code_entry.delete(0, END)
        view.time_entry.delete(0, END)
        view.status_entry.delete(0, END)
        view.location_entry.delete(0, END)
        # self.place_inbound_order_frame()

    # =================================================================
    def add_products_to_outbound_c(self, view, outbound_products_lst):
        try:
            # TODO Validation for empty strings and digits
            product_code = view.product_code_var.get()
            product_name = view.product_name_var.get()
            product_qty = view.product_quantity_var.get()
            pr = {'code': product_code, 'name': product_name, 'quantity': product_qty}
            outbound_products_lst.append(pr)
            view.product_code_var.set(' '.strip())
            view.product_name_var.set(' '.strip())
            view.product_quantity_var.set(' '.strip())
            return outbound_products_lst
        except AttributeError:
            pass

    def submit_outbound_c(self,view,user,outbound_products_lst):
        outbound_orders = DbContext.load_from_json_file(DbContext.OUTBOUNDS_DB)
        ids = DbContext.values_from_dictionary(outbound_orders, 'id')
        # indexes = [index for index, x in enumerate(client_codes) if x == 100]
        new_inbound = {
            "id": f"{int(max(map(lambda x: int(x), ids))) + 1}",
            "client_code": user.code,
            "products": outbound_products_lst,
            "time": view.time_entry_var.get(),
            "status": view.status_entry_var.get(),
            "location": view.location_entry_var.get()
        }
        outbound_orders.append(new_inbound)
        DbContext.save_in_json_file(DbContext.OUTBOUNDS_DB, outbound_orders)
        messagebox.showinfo('SUCCESS', 'Successfully add new Outbound Order')
        view.client_code_entry.delete(0, END)
        view.time_entry.delete(0, END)
        view.status_entry.delete(0, END)
        view.location_entry.delete(0, END)
        # self.place_inbound_order_frame()

    # =============================================================
    def placed_inbounds_c(self,view, user):
        inbounds = DbContext.load_from_json_file(DbContext.INBOUNDS_DB)
        client_codes = DbContext.values_from_dictionary(inbounds, 'client_code')
        # '100' = user username
        indexes = [index for index, x in enumerate(client_codes) if x == user.code]
        p_in_inbound = {}
        for i in indexes:
            quantities = DbContext.values_from_dictionary(inbounds[i]['products'], 'quantity')
            p_in_inbound[i] = int(reduce(lambda x, y: int(x) + int(y), quantities))
        return indexes, inbounds, p_in_inbound

    # =============================================================
    def placed_outbounds_c(self,view, user):
        outbounds = DbContext.load_from_json_file(DbContext.OUTBOUNDS_DB)
        client_codes = DbContext.values_from_dictionary(outbounds, 'client_code')
        # '100' = user username
        indexes = [index for index, x in enumerate(client_codes) if x == user.code]
        p_in_outbound = {}
        for i in indexes:
            quantities = DbContext.values_from_dictionary(outbounds[i]['products'], 'quantity')
            p_in_outbound[i] = int(reduce(lambda x, y: int(x) + int(y), quantities))
        return indexes, outbounds, p_in_outbound

    # =============================================================
    def list_all_products_c(self, user):
        products = DbContext.load_from_json_file(DbContext.PRODUCTS_DB)
        client_codes = DbContext.values_from_dictionary(products, 'client_code')
        indexes = [index for index, x in enumerate(client_codes) if x == user.code]
        return indexes, products

