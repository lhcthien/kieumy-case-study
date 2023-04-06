from functools import reduce
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from data_files.DbContext import DbContext


class AdministratorModel:
    def __init__(self, parent, user):
        self.parent = parent
        self.user = user


    def clean_entries(self, view):
        pass

    # ======================= USERS =============================
    def list_all_users_c(self):
        users = DbContext.load_from_json_file(DbContext.USERS_DB)
        return users
        # users = Administrator.list_all_users(self)

    def add_user_c(self,view):
        username = view.username_entry.get()
        password = view.password_entry.get()
        role = view.role_entry.get()
        code = view.code_entry.get()
        users = DbContext.load_from_json_file(DbContext.USERS_DB)
        usernames = DbContext.values_from_dictionary(users, 'username')
        if username in usernames:
            print('Username already exists. Enter another one')
            messagebox.showerror('FAILED', 'Username already exists!')
        else:
            if role == 'ww':
                new_user = {'username': username,
                            'password': password,
                            'role': role,
                            'code': [x for x in code.split(',')]}
                users.append(new_user)
            else:
                new_user = {'username': username,
                            'password': password,
                            'role': role,
                            'code': code}
                users.append(new_user)
        view.username_entry.delete(0, END)
        view.password_entry.delete(0, END)
        view.role_entry.delete(0, END)
        view.code_entry.delete(0, END)
        DbContext.save_in_json_file(DbContext.USERS_DB, users)
        messagebox.showinfo('SUCCESS', f'Username {username} added successfully!')

    def delete_user_c(self, view):
        username = view.username_entry.get()
        users = DbContext.load_from_json_file(DbContext.USERS_DB)
        usernames = DbContext.values_from_dictionary(users, 'username')
        if username in usernames:
            index = usernames.index(username)
            users.remove(users[index])
            DbContext.save_in_json_file(DbContext.USERS_DB, users)
            messagebox.showinfo('SUCCESS', f'Username {username} deleted successfully!')
        else:
            messagebox.showinfo('FAILED', f'Username {username} does not exist!')

        view.username_entry.delete(0, END)

    def update_user_c(self, view):
        username = view.username_entry.get()
        users = DbContext.load_from_json_file(DbContext.USERS_DB)
        usernames = DbContext.values_from_dictionary(users, 'username')
        index = 0
        if username in usernames:
            index = usernames.index(username)
            view.username_entry = users[index]['username']
            view.password_entry = users[index]['password']
            view.role_entry = users[index]['role']
            view.code_entry = users[index]['code']
            return index
        else:
            messagebox.showinfo('FAILED', f'Username {username} does not exist!')
            view.username_entry.delete(0, END)
            return -1

    def save_updated_user_c(self, view, index):
        u = view.username_entry.get()
        p = view.password_entry.get()
        r = view.role_entry.get()
        c = view.code_entry.get()
        users = DbContext.load_from_json_file(DbContext.USERS_DB)
        users[index]['username'] = u
        users[index]['password'] = p
        users[index]['role'] = r
        if r == 'ww':
            users[index]['code'] = \
                list(''.join(list(filter(lambda x: x.isdigit() or x == ' ', c))).split(' '))
        else:
            users[index]['code'] = c

        DbContext.save_in_json_file(DbContext.USERS_DB, users)
        messagebox.showinfo('UPDATE USER', f'USER {u} was updated successfully!')
        view.username_entry.delete(0, END)
        view.password_entry.delete(0, END)
        view.role_entry.delete(0, END)
        view.code_entry.delete(0, END)

    # ====================== INBOUNDS ===========================
    def list_all_inbounds_c(self):
        inbounds = DbContext.load_from_json_file(DbContext.INBOUNDS_DB)
        return inbounds

    def products_in_inbound(self):
        inbounds = self.list_all_inbounds_c()
        res = []
        for inbound in inbounds:
            quantities = DbContext.values_from_dictionary(inbound['products'], 'quantity')
            p_in_inbound = int(reduce(lambda x, y: int(x) + int(y), quantities))
            res.append(p_in_inbound)
        return res
    # ============================================================
    def inbound_by_id_c(self, view):
        id_inbound = view.id_inbound_entry_var.get()
        inbounds = DbContext.load_from_json_file(DbContext.INBOUNDS_DB)
        ids = DbContext.values_from_dictionary(inbounds, 'id')
        if id_inbound not in ids:
            messagebox.showerror('FAIL', 'There is no such ID!')
            view.id_inbound_entry.delete(0, END)
            return -1, -1
        else:
            index = ids.index(id_inbound)
            inbound = inbounds[index]
            quantities = DbContext.values_from_dictionary(inbound['products'], 'quantity')
            p_in_inbound = int(reduce(lambda x, y: int(x) + int(y), quantities))
            return inbound, p_in_inbound

    # ============================================================
    def inbounds_by_client_c(self, view):
        inbounds = DbContext.load_from_json_file(DbContext.INBOUNDS_DB)
        client_codes = DbContext.values_from_dictionary(inbounds, 'client_code')
        client_code_inbound_entry_var = view.client_inbound_entry_var.get()
        if len(client_code_inbound_entry_var) == 0:
            return -1, -1, -1
        if client_code_inbound_entry_var not in client_codes:
            messagebox.showerror('FAIL', 'There is no such Client Code!')
            view.client_code_inbound_entry.delete(0, END)
            return -1, -1, -1
        else:
            indexes = [index for index, x in enumerate(client_codes) if x == client_code_inbound_entry_var]
            p_in_inbound = {}
            for i in indexes:
                quantities = DbContext.values_from_dictionary(inbounds[i]['products'], 'quantity')
                p_in_inbound[i] = int(reduce(lambda x, y: int(x) + int(y), quantities))
            return indexes, inbounds, p_in_inbound

    # ============================================================
    def inbounds_by_time_c(self, view):
        inbounds = DbContext.load_from_json_file(DbContext.INBOUNDS_DB)
        time_inbound_entry_var = view.time_inbound_entry_var.get()
        dates = DbContext.values_from_dictionary(inbounds, 'time')
        if len(time_inbound_entry_var) == 0:
            return -1, -1, -1
        if time_inbound_entry_var not in dates:
            messagebox.showerror('FAIL', 'There is no such Date!')
            view.time_inbound_entry.delete(0, END)
            return -1, -1, -1
        else:
            indexes = [index for index, x in enumerate(dates) if x == time_inbound_entry_var]
            p_in_inbound = {}
            for i in indexes:
                quantities = DbContext.values_from_dictionary(inbounds[i]['products'], 'quantity')
                p_in_inbound[i] = int(reduce(lambda x, y: int(x) + int(y), quantities))
            return indexes, inbounds, p_in_inbound

    # ============================================================
    # ====================== OUTBOUNDS ===========================
    def list_all_outbounds_c(self):
        outbounds = DbContext.load_from_json_file(DbContext.OUTBOUNDS_DB)
        return outbounds

    def products_in_outbound(self):
        outbounds = self.list_all_inbounds_c()
        res = []
        for outbound in outbounds:
            quantities = DbContext.values_from_dictionary(outbound['products'], 'quantity')
            p_in_outbound = int(reduce(lambda x, y: int(x) + int(y), quantities))
            res.append(p_in_outbound)
        return res
    # ============================================================
    def outbound_by_id_c(self, view):
        id_outbounds = view.id_outbound_entry_var.get()
        outbounds = DbContext.load_from_json_file(DbContext.OUTBOUNDS_DB)
        ids = DbContext.values_from_dictionary(outbounds, 'id')
        if id_outbounds not in ids:
            messagebox.showerror('FAIL', 'There is no such ID!')
            view.id_outbound_entry.delete(0, END)
            return -1, -1
        else:
            index = ids.index(id_outbounds)
            outbound = outbounds[index]
            quantities = DbContext.values_from_dictionary(outbound['products'], 'quantity')
            p_in_outbound = int(reduce(lambda x, y: int(x) + int(y), quantities))
            return outbound, p_in_outbound

    # ============================================================
    def outbound_by_client_c(self, view):
        outbounds = DbContext.load_from_json_file(DbContext.OUTBOUNDS_DB)
        client_codes = DbContext.values_from_dictionary(outbounds, 'client_code')
        client_code_outbound_entry_var = view.client_outbound_entry_var.get()
        if client_code_outbound_entry_var not in client_codes:
            messagebox.showerror('FAIL', 'There is no such Client Code!')
            view.client_outbound_entry.delete(0, END)
            return -1, -1, -1
        else:
            indexes = [index for index, x in enumerate(client_codes) if x == client_code_outbound_entry_var]
            p_in_outbound = {}
            for i in indexes:
                quantities = DbContext.values_from_dictionary(outbounds[i]['products'], 'quantity')
                p_in_outbound[i] = int(reduce(lambda x, y: int(x) + int(y), quantities))
            return indexes, outbounds, p_in_outbound

    # ============================================================
    def outbound_by_time_c(self, view):
        outbounds = DbContext.load_from_json_file(DbContext.OUTBOUNDS_DB)
        time_outbound_entry_var = view.time_outbound_entry_var.get()
        dates = DbContext.values_from_dictionary(outbounds, 'time')
        if view.time_outbound_entry_var not in dates:
            messagebox.showerror('FAIL', 'There is no such Date!')
            view.time_outbound_entry.delete(0, END)
            return -1, -1, -1
        else:
            indexes = [index for index, x in enumerate(dates) if x == time_outbound_entry_var]
            p_in_outbound = {}
            for i in indexes:
                quantities = DbContext.values_from_dictionary(outbounds[i]['products'], 'quantity')
                p_in_outbound[i] = int(reduce(lambda x, y: int(x) + int(y), quantities))
            return indexes, outbounds, p_in_outbound

    # ============================================================
    # ====================== PRODUCTS ============================
    def list_all_products_c(self):
        products = DbContext.load_from_json_file(DbContext.PRODUCTS_DB)
        return products

    # ============================================================
    def products_by_client_c(self, view):
        products = DbContext.load_from_json_file(DbContext.PRODUCTS_DB)
        client_codes = DbContext.values_from_dictionary(products, 'client_code')
        pr_codes = DbContext.values_from_dictionary(products, 'code')
        client_code_entry_var = view.client_code_products_entry_var.get()
        if client_code_entry_var not in client_codes:
            messagebox.showerror('FAIL', 'There is no such Client Code!')
            view.client_code_products_entry.delete(0, END)
            return -1, -1,
        else:
            indexes = [index for index, x in enumerate(client_codes) if x == client_code_entry_var]
            return indexes, products

    # ============================================================
    def add_product_c(self, view):
        code = view.code_entry_var.get()
        name = view.name_entry_var.get()
        client_code = view.client_code_entry_var.get()
        quantity = view.quantity_entry_var.get()
        volume = view.volume_entry_var.get()
        weight = view.weight_entry_var.get()
        new_product = {
            "code": code,
            "name": name,
            "client_code": client_code,
            "quantity": quantity,
            "volume": volume,
            "weight": weight
        }
        products = DbContext.load_from_json_file(DbContext.PRODUCTS_DB)
        codes = DbContext.values_from_dictionary(products, 'code')
        if code in codes:
            print('Product already exists. Enter valid one')
            messagebox.showerror('FAILED', 'Product already exists!')
            view.code_entry.delete(0,END)
            view.name_entry.delete(0,END)
            view.client_code.delete(0,END)
            view.quantity_entry.delete(0,END)
            view.volume_entry.delete(0,END)
            view.weight_entry.delete(0,END)
            return -1
        else:
            products.append(new_product)

            DbContext.save_in_json_file(DbContext.PRODUCTS_DB, products)
            messagebox.showinfo('SUCCESS', f'Product {new_product["name"]} added successfully!')
            messagebox.showerror('FAILED', 'Product already exists!')
            view.code_entry.delete(0, END)
            view.name_entry.delete(0, END)
            view.client_code.delete(0, END)
            view.quantity_entry.delete(0, END)
            view.volume_entry.delete(0, END)
            view.weight_entry.delete(0, END)
            return 1

    # ============================================================
    def delete_product_c(self, view):
        products = DbContext.load_from_json_file(DbContext.PRODUCTS_DB)
        codes = DbContext.values_from_dictionary(products, 'code')
        code_input = view.product_code_entry_var.get()
        if code_input not in codes:
            messagebox.showerror('FAIL', 'Enter Valid Product Code')
            view.product_code_entry.delete(0,END)
            return -1
            # return view.delete_product()
        else:
            index = codes.index(code_input)
            product_about_to_be_deleted = products[index]
            ask = messagebox.askokcancel('DELETION', f'Do you want to delete this product? \n'
                                                     f'{product_about_to_be_deleted["code"]} - {product_about_to_be_deleted["name"]}')
            if ask == True:
                products.pop(index)
                DbContext.save_in_json_file(DbContext.PRODUCTS_DB, products)
                messagebox.showinfo('DELETION', f'{product_about_to_be_deleted["code"]} - '
                                                f'{product_about_to_be_deleted["name"]} was deleted')
                view.product_code_entry.delete(0,END)
                return 1
            else:
                view.product_code_entry.delete(0, END)
                return -1

    # ============================================================
    def update_product_c(self, view):
        products_update = DbContext.load_from_json_file(DbContext.PRODUCTS_DB)
        codes = DbContext.values_from_dictionary(products_update, 'code')
        index = 0
        # update_name_entry_var = view.update_name_entry_var.get()
        if view.update_code_entry_var.get() in codes:
            index = codes.index(view.update_code_entry_var.get())
            view.update_code_entry_var.set(products_update[index]['code'])
            return products_update, index
        else:
            messagebox.showinfo('FAILED', f'Product with code {view.update_code_entry_var.get()} does not exist!')
            view.update_code_entry_var = "" # .delete(0,END)
            # view.update_name_entry.delete(0,END)
            # view.update_client_code_entry.delete(0,END)
            # view.update_quantity_entry.delete(0,END)
            # view.update_volume_entry.delete(0,END)
            # view.update_weight_entry.delete(0,END)
            return -1, -1

    def save_product_item_c(self, view, products_update, index):
        code = view.update_code_entry_var.get()
        name = view.update_name_entry_var.get()
        client_code = view.update_client_code_entry_var.get()
        quantity = view.update_quantity_entry_var.get()
        volume = view.update_volume_entry_var.get()
        weight = view.update_weight_entry_var.get()

        products_update[index]['code'] = code
        products_update[index]['name'] = name
        products_update[index]['client_code'] = client_code
        products_update[index]['quantity'] = quantity
        products_update[index]['volume'] = volume
        products_update[index]['weight'] = weight

        DbContext.save_in_json_file(DbContext.PRODUCTS_DB, products_update)
        messagebox.showinfo('UPDATE PRODUCT', f'Product {code} - {name} was updated successfully!')
        view.update_code_entry.delete(0,END)
        view.update_name_entry.delete(0,END)
        view.update_client_code_entry.delete(0,END)
        view.update_quantity_entry.delete(0,END)
        view.update_volume_entry.delete(0,END)
        view.update_weight_entry.delete(0,END)

    # ============================================================
    # ====================== LOCATIONS ===========================
    def list_all_locations_c(self):
        locations = DbContext.load_from_json_file(DbContext.LOCATIONS_DB)
        return locations

    # ============================================================
    def add_location_c(self, view):
        warehouse = view.warehouse_entry_var.get()
        regal = view.regal_entry_var.get()
        locations = DbContext.load_from_json_file(DbContext.LOCATIONS_DB)
        ids = DbContext.values_from_dictionary(locations, 'id')

        new_location = {
            "id": f"{int(max(map(lambda x: int(x), ids))) + 1}",
            "warehouse": warehouse,
            "regal": regal
        }

        locations = DbContext.load_from_json_file(DbContext.LOCATIONS_DB)
        warehouses = DbContext.values_from_dictionary(locations, 'warehouse')
        regals = DbContext.values_from_dictionary(locations, 'regal')
        if warehouse in warehouses:
            if regal in regals:
                messagebox.showerror('FAILED', f'Regal {regal} in Warehouse {warehouse} already exists!')
                view.warehouse_entry_var = view.regal_entry_var = ''
                return -1
                # view.warehouse_entry_var = view.regal_entry_var = ''
            else:
                locations.append(new_location)

                DbContext.save_in_json_file(DbContext.LOCATIONS_DB, locations)
                messagebox.showinfo('SUCCESS', f'Location {warehouse} - {regal} added successfully!')
                view.warehouse_entry_var = view.regal_entry_var = ''
                return 1
        else:
            locations.append(new_location)

            DbContext.save_in_json_file(DbContext.LOCATIONS_DB, locations)
            messagebox.showinfo('SUCCESS', f'Location {warehouse} - {regal} added successfully!')
            view.warehouse_entry_var = view.regal_entry_var = ''
            return 1


    # ============================================================
    def delete_location_c(self, view):
        id_location = view.id_location_entry_var.get()
        locations = DbContext.load_from_json_file(DbContext.LOCATIONS_DB)
        ids = DbContext.values_from_dictionary(locations, 'id')

        if id_location in ids:
            index = ids.index(id_location)
            location_about_to_be_deleted = locations[index]
            ask = messagebox.askokcancel('DELETION', f'Do you want to delete this location? \n'
                                                     f'{location_about_to_be_deleted["warehouse"]} - '
                                                     f'{location_about_to_be_deleted["regal"]}')
            if ask == True:
                locations.pop(index)
                DbContext.save_in_json_file(DbContext.LOCATIONS_DB, locations)
                messagebox.showinfo('DELETION', f'{location_about_to_be_deleted["warehouse"]} - '
                                                f'{location_about_to_be_deleted["regal"]} was deleted')
                view.id_location_entry_var = ''
                return 1
            else:
                view.id_location_entry_var = ''
                return -1
        else:
            messagebox.showerror('FAILED', f'ID {id_location} does not exist!')
            view.id_location_entry_var = ''
            return -1

    # ============================================================
    def update_location_c(self, view):
        locations_update = DbContext.load_from_json_file(DbContext.LOCATIONS_DB)
        ids = DbContext.values_from_dictionary(locations_update, 'id')
        # we_var = view.warehouse_entry_var.get()
        # re_var = view.regal_entry_var.get()
        # print(we_var, re_var)
        index = 0
        if view.id_location_entry_var.get() in ids:
            index = ids.index(view.id_location_entry_var.get())
            # view.warehouse_entry_var.set(locations_update[index]['warehouse'])
            # view.regal_entry_var.set(locations_update[index]['regal'])
            return locations_update, index
        else:
            messagebox.showinfo('FAILED', f'Location with id {view.id_location_entry_var.get()} does not exist!')
            return -1, -1

    def save_updated_location_c(self, view, locations_update, index):
        warehouse = view.warehouse_entry_var.get()
        regal = view.regal_entry_var.get()

        locations_update[index]['warehouse'] = warehouse
        locations_update[index]['regal'] = regal

        DbContext.save_in_json_file(DbContext.LOCATIONS_DB, locations_update)
        messagebox.showinfo('UPDATE LOCATION', f'Location was updated successfully!')
        view.warehouse_entry.delete(0,END)
        view.regal_entry.delete(0,END)
    # ============================================================