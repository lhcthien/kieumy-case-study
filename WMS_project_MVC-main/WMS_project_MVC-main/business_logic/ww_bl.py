import json
from functools import reduce
from tkinter import messagebox, END, Tk
from data_files.DbContext import DbContext
# import adminModel
# from User import *
# from adminController import AdminController
# from adminModel import *


class WwModel:
    def __init__(self, parent, user):
        self.parent = parent
        self.user = user

# =============================================================================================
    def placed_inbound_orders_c(self, view, user):
        inbounds = DbContext.load_from_json_file(DbContext.INBOUNDS_DB)
        client_codes = DbContext.values_from_dictionary(inbounds, 'client_code')
        users_clients = user.code  # ['100','103']
        indexes = [index for index, x in enumerate(client_codes) if x in users_clients]

        new_inbounds = [inbounds[x] for x in indexes if inbounds[x]['status'] == 'sent']
        p_in_inbound = {}
        for i,inbound in enumerate(new_inbounds):
            quantities = DbContext.values_from_dictionary(inbound['products'], 'quantity')
            p_in_inbound[i] = int(reduce(lambda x, y: int(x) + int(y), quantities))
        return new_inbounds, p_in_inbound

    def accept_inbound_c(self, selected_item_id, inbounds):
        stock = DbContext.load_from_json_file(DbContext.STOCK_DB)
        products_to_stock = inbounds[selected_item_id]['products']
        print(products_to_stock)
        not_existing_products = []

        for index, i in enumerate(products_to_stock):
            if i['code'] in stock[index]['product']['code']:
                stock[index]['product']['quantity'] = int(stock[index]['product']['quantity']) + int(i['quantity'])
            else:
                not_existing_products.append(i)

        if len(not_existing_products) != 0:
            for x in not_existing_products:
                messagebox.showinfo('FAIL', f'Product with code {x["code"]} not exist!')
            return False
        else:
            inbounds[selected_item_id]['status'] = 'accepted'
            DbContext.save_in_json_file(DbContext.STOCK_DB, stock)
            DbContext.save_in_json_file(DbContext.INBOUNDS_DB, inbounds)
            messagebox.showinfo('SUCCESS', f'INBOUND ACCEPTED!')
            return True

# =============================================================================================
    def placed_outbound_orders_c(self, view, user):
        outbounds = DbContext.load_from_json_file(DbContext.OUTBOUNDS_DB)
        client_codes = DbContext.values_from_dictionary(outbounds, 'client_code')
        users_clients = user.code  # ['100','103']
        indexes = [index for index, x in enumerate(client_codes) if x in users_clients]
        new_outbounds = [outbounds[x] for x in indexes if outbounds[x]['status'] == 'sent']
        p_in_outbound = {}
        for i,outbound in enumerate(new_outbounds):
            quantities = DbContext.values_from_dictionary(outbound['products'], 'quantity')
            p_in_outbound[i] = int(reduce(lambda x, y: int(x) + int(y), quantities))
        return new_outbounds, p_in_outbound

    def accept_outbound_c(self, selected_item_id, outbounds):
        stock = DbContext.load_from_json_file(DbContext.STOCK_DB)
        products_to_stock = outbounds[selected_item_id]['products']
        print(products_to_stock)
        not_existing_products = []

        for index, i in enumerate(products_to_stock):
            if i['code'] in stock[index]['product']['code']:
                stock[index]['product']['quantity'] = int(stock[index]['product']['quantity']) + int(i['quantity'])
            else:
                not_existing_products.append(i)

        if len(not_existing_products) != 0:
            for x in not_existing_products:
                messagebox.showinfo('FAIL', f'Product with code {x["code"]} not exist!')
                return False
        else:
            outbounds[selected_item_id]['status'] = 'accepted'
            DbContext.save_in_json_file(DbContext.STOCK_DB, stock)
            DbContext.save_in_json_file(DbContext.OUTBOUNDS_DB, outbounds)
            messagebox.showinfo('SUCCESS', f'OUTBOUND ACCEPTED!')
            return True

# ===============================================================================================
    def accepted_inbounds_c(self,view,user):
        inbounds = DbContext.load_from_json_file(DbContext.INBOUNDS_DB)
        client_codes = DbContext.values_from_dictionary(inbounds, 'client_code')
        users_clients = user.code  # ['100', '103']
        indexes = [index for index, x in enumerate(client_codes) if x in users_clients]

        acc_inbounds = [inbounds[x] for x in indexes if inbounds[x]['status'] == 'accepted']
        p_in_inbound = {}
        for i,inbound in enumerate(acc_inbounds):
            quantities = DbContext.values_from_dictionary(inbound['products'], 'quantity')
            p_in_inbound[i] = int(reduce(lambda x, y: int(x) + int(y), quantities))

        return acc_inbounds, p_in_inbound

# ===============================================================================================
    def accepted_outbounds_c(self,view,user):
        outbounds = DbContext.load_from_json_file(DbContext.OUTBOUNDS_DB)
        client_codes = DbContext.values_from_dictionary(outbounds, 'client_code')
        users_clients = user.code  # ['100', '103']
        indexes = [index for index, x in enumerate(client_codes) if x in users_clients]

        acc_outbounds = [outbounds[x] for x in indexes if outbounds[x]['status'] == 'accepted']
        p_in_outbound = {}
        for i, outbound in enumerate(acc_outbounds):
            quantities = DbContext.values_from_dictionary(outbound['products'], 'quantity')
            p_in_outbound[i] = int(reduce(lambda x, y: int(x) + int(y), quantities))
        return acc_outbounds, p_in_outbound

 # ==================== CHANGE LOCATION ================================
    def change_location_c(self, view, user):
        stock = DbContext.load_from_json_file(DbContext.STOCK_DB)
        client_codes = DbContext.values_from_dictionary(stock, 'client_code')
        users_clients = user.code  # ['100', '103']
        indexes = [index for index, x in enumerate(client_codes) if x in users_clients]
        available_stock = [stock[x] for x in indexes]
        locations = DbContext.load_from_json_file(DbContext.LOCATIONS_DB)
        return available_stock, locations, stock

    def save_location_to_item_c(self, view, user, stock, selected_item_id):
        loc_id = view.loc_entry_var.get()
        stock[int(selected_item_id)]['location_id'] = int(loc_id) - 1
        DbContext.save_in_json_file(DbContext.STOCK_DB, stock)
        messagebox.showinfo('SUCCESS', 'You updated the location successfully!')










