from business_logic.admin_bl import AdministratorModel
from main import AppStart
from views.admin_view import *


class AdminController:
    def __init__(self, parent, user):
        self.parent = parent

        # models
        self.admin_model = AdministratorModel(parent, user)

        # ADMIN MAIN VIEW
        self.admin_main_view = AdminMainView(parent,self)
        self.admin_main_view.username_label_text = user.username
        self.admin_main_view.role_label_text = user.role

        # Panels/Frames
        self.users_panel = AdminUsersWindow(self.admin_main_view, self)
        self.inbounds_panel = AdminInboundsWindow(self.admin_main_view, self)
        self.outbounds_panel = AdminOutboundsWindow(self.admin_main_view, self)
        self.products_panel = AdminProductsWindow(self.admin_main_view, self)
        self.locations_panel = AdminLocationsWindow(self.admin_main_view, self)

        # USER VIEWS
        self.lst_all_users_view = ListAllUsersFrame(self.admin_main_view, self)
        self.add_user_view = AddUserFrame(self.admin_main_view, self)
        self.delete_user_view = DeleteUserFrame(self.admin_main_view, self)
        self.update_user_view = UpdateUserFrame(self.admin_main_view, self)
        self.save_updated_user_view = SaveUpdatedUserFrame(self.admin_main_view, self)

        # INBOUNDS VIEWS
        self.lst_all_inbounds_view = ListAllInboundsView(self.admin_main_view, self)
        self.inbound_by_id_view = InboundByIdView(self.admin_main_view, self)
        self.inbound_by_id_treeview = InboundByIdTreeview(self.admin_main_view, self)
        self.inbound_by_clients_view = InboundByClient(self.admin_main_view, self)
        self.inbound_by_clients_treeview = InboundByClientTreeview(self.admin_main_view, self)
        self.inbound_by_time_view = InboundByTime(self.admin_main_view, self)
        self.inbound_by_time_treeview = InboundByTimeTreeview(self.admin_main_view, self)

        # OUTBOUNDS VIEWS
        self.lst_all_outbounds_view = ListAllOutboundsView(self.admin_main_view, self)
        self.outbound_by_id_view = OutboundByIdView(self.admin_main_view, self)
        self.outbound_by_id_treeview = OutboundByIdTreeview(self.admin_main_view, self)
        self.outbounds_by_client_view = OutboundsByClient(self.admin_main_view, self)
        self.outbounds_by_client_treeview = OutboundsByClientTreeview(self.admin_main_view, self)
        self.outbounds_by_time_view = OutboundsByTime(self.admin_main_view, self)
        self.outbounds_by_time_treeview = OutboundsByTimeTreeview(self.admin_main_view, self)

        # PRODUCTS VIEWS
        self.lst_all_products_view = ListAllProductsView(self.admin_main_view, self)
        self.products_by_client_view = ProductsByClientView(self.admin_main_view, self)
        self.products_by_client_treeview = ProductsByClientTreeview(self.admin_main_view, self)
        self.add_product_view = AddProductView(self.admin_main_view, self)
        self.delete_product_view = DeleteProductView(self.admin_main_view, self)
        self.update_product_view = UpdateProductView(self.admin_main_view, self)
        self.update_product_data_view = UpdateProductDataView(self.admin_main_view, self)

        # LOCATIONS VIEWS
        self.lst_all_locations_view = ListAllLocationsView(self.admin_main_view, self)
        self.add_location_view = AddLocationView(self.admin_main_view, self)
        self.delete_location_view = DeleteLocation(self.admin_main_view, self)
        self.update_location_view = UpdateLocationView(self.admin_main_view, self)
        self.update_location_data_view = UpdateLocationDataView(self.admin_main_view, self)

    def clear_frame(self):
        for widgets in self.admin_main_view.frame1.winfo_children():
            widgets.destroy()

    def show_admin_panel(self):
        print("admin_panel")
        self.admin_main_view.setup()
        self.admin_main_view.users.config(command=self.show_users_frame) # users button
        self.admin_main_view.inbounds.config(command=self.show_inbounds_frame) # inbounds button
        self.admin_main_view.outbounds.config(command=self.show_outbounds_frame) # outbounds button
        self.admin_main_view.products.config(command=self.show_products_frame) # products button
        self.admin_main_view.locations.config(command=self.show_locations_frame) # locations button
        self.admin_main_view.logout.config(command=self.logout_command)


    def logout_command(self):
        self.parent.destroy()
        AppStart()

    # ======================== USERS ACTIONS ========================================
    def show_users_frame(self):
        print('users frame')
        self.clear_frame()
        self.users_panel.setup()
        self.users_panel.lst_all_users.config(command=self.list_all_users)
        self.users_panel.add_user.config(command=self.add_user)
        self.users_panel.delete_user.config(command=self.delete_user)
        self.users_panel.update_user.config(command=self.update_user)

    #=============================================================================
    def list_all_users(self):
        print('all users')
        # self.clear_frame()
        self.show_users_frame()
        self.lst_all_users_view.setup()
        users = self.admin_model.list_all_users_c()
        self.lst_all_users_view.insert_in_treeview(users)

    # =============================================================================
    def add_user(self):
        print('add user')
        self.show_users_frame()
        self.add_user_view.setup()
        self.add_user_view.add_btn.config(command=self.submit_new_user)

    def submit_new_user(self):
        self.admin_model.add_user_c(self.add_user_view)

    # =============================================================================
    def delete_user(self):
        print('delete user')
        self.show_users_frame()
        self.delete_user_view.setup()
        self.delete_user_view.delete_btn.config(command=self.delete_selected_user)

    def delete_selected_user(self):
        self.admin_model.delete_user_c(self.delete_user_view)

    #==================================================================================
    def update_user(self):
        print('update user')
        self.show_users_frame()
        self.update_user_view.setup()
        self.update_user_view.update_btn.config(command=self.show_user_to_update)

    def update_user_check(self):
        self.index = self.admin_model.update_user_c(self.update_user_view)
        return self.index

    def show_user_to_update(self):
        self.marker = self.update_user_check()
        if self.marker == -1:
            return self.update_user()
        self.show_users_frame()
        self.save_updated_user_view.setup()
        self.save_updated_user_view.save_btn.config(command=self.save_updated_user)

    def save_updated_user(self):
        print('save_updated_user')
        self.admin_model.save_updated_user_c(self.save_updated_user_view, self.marker)

    # ==================================================================================
    # ========================INBOUNDS ACTIONS==========================================
    def show_inbounds_frame(self):
        print("inbound panel")
        self.clear_frame()
        self.inbounds_panel.setup()
        self.inbounds_panel.list_all_inbounds_frame.config(command=self.list_all_inbounds)
        self.inbounds_panel.specific_inbound_frame.config(command=self.inbound_by_id)
        self.inbounds_panel.list_inbounds_by_clients_frame.config(command=self.list_inbounds_by_clients)
        self.inbounds_panel.list_inbounds_by_time_frame.config(command=self.list_inbounds_by_time)

    # =============================================================================
    def list_all_inbounds(self):
        self.show_inbounds_frame()
        inbounds = self.admin_model.list_all_inbounds_c()
        quantities = self.admin_model.products_in_inbound()
        self.lst_all_inbounds_view.setup()
        self.lst_all_inbounds_view.insert_in_treeview(inbounds,quantities)
        # self.lst_all_inbounds_view.

    # =============================================================================
    def inbound_by_id(self):
        self.show_inbounds_frame()
        self.inbound_by_id_view.setup()
        self.inbound_by_id_view.search_btn.config(command=self.inbound_by_id_treeview_sec)

    def check_inbound_by_id_c(self):
        self.inbound, self.p_in_inbound = self.admin_model.inbound_by_id_c(self.inbound_by_id_view)
        return self.inbound, self.p_in_inbound

    def inbound_by_id_treeview_sec(self):
        inbound, p_in_inbound = self.check_inbound_by_id_c()
        if inbound == -1 and p_in_inbound == -1:
            return self.inbound_by_id()
        self.inbound_by_id_treeview.setup()
        self.inbound_by_id_treeview.insert_in_treeview(inbound,p_in_inbound)

    # =============================================================================
    def list_inbounds_by_clients(self):
        print("inbounds_by_clients")
        self.show_inbounds_frame()
        self.inbound_by_clients_view.setup()
        self.inbound_by_clients_view.search_btn.config(command=self.inbound_by_client_treeview_sec)

    def check_inbound_by_client_c(self):
        self.indexes, self.inbounds, self.p_in_inbound = self.admin_model.inbounds_by_client_c(self.inbound_by_clients_view)
        return self.indexes,self.inbounds, self.p_in_inbound

    def inbound_by_client_treeview_sec(self):
        indexes, inbounds, p_in_inbound = self.check_inbound_by_client_c()
        if indexes == -1 and inbounds == -1 and p_in_inbound == -1:
            return self.list_inbounds_by_clients()
        self.inbound_by_clients_treeview.setup()
        self.inbound_by_clients_treeview.insert_in_treeview(indexes,inbounds, p_in_inbound)

    # =============================================================================
    def list_inbounds_by_time(self):
        print("inbounds_by_time")
        self.show_inbounds_frame()
        self.inbound_by_time_view.setup()
        self.inbound_by_time_view.search_btn.config(command=self.inbound_by_time_treeview_sec)

    def check_inbound_by_time_c(self):
        self.indexes, self.inbounds, self.p_in_inbound = self.admin_model.inbounds_by_time_c(self.inbound_by_time_view)
        return self.indexes, self.inbounds, self.p_in_inbound

    def inbound_by_time_treeview_sec(self):
        indexes, inbounds, p_in_inbound = self.check_inbound_by_time_c()
        if indexes == -1 and inbounds == -1 and p_in_inbound == -1:
            return self.list_inbounds_by_clients()
        self.inbound_by_time_treeview.setup()
        self.inbound_by_time_treeview.insert_in_treeview(indexes, inbounds, p_in_inbound)

    # =============================================================================
    # ======================== OUTBOUND ACTIONS====================================
    def show_outbounds_frame(self):
        print("OUTBOUNDS")
        self.clear_frame()
        self.outbounds_panel.setup()
        # views
        self.outbounds_panel.list_all_outbounds_frame.config(command=self.list_all_outbounds)
        self.outbounds_panel.specific_outbound_frame.config(command=self.outbound_by_id)
        self.outbounds_panel.list_outbounds_by_clients_frame.config(command=self.list_outbounds_by_clients)
        self.outbounds_panel.list_outbounds_by_time_frame.config(command=self.list_outbounds_by_time)

    # =============================================================================
    def list_all_outbounds(self):
        print('list_all_outbounds')
        self.show_outbounds_frame()
        outbounds = self.admin_model.list_all_outbounds_c()
        quantities = self.admin_model.products_in_outbound()
        self.lst_all_outbounds_view.setup()
        self.lst_all_outbounds_view.insert_in_treeview(outbounds,quantities)

    # =============================================================================
    def outbound_by_id(self):
        print('outbound_by_id')
        self.show_outbounds_frame()
        self.outbound_by_id_view.setup()
        self.outbound_by_id_view.search_btn.config(command=self.outbound_by_id_treeview_sec)

    def check_outbound_by_id_c(self):
        self.outbound, self.p_in_outbound = self.admin_model.outbound_by_id_c(self.outbound_by_id_view)
        return self.outbound, self.p_in_outbound

    def outbound_by_id_treeview_sec(self):
        outbound, p_in_outbound = self.check_outbound_by_id_c()
        if outbound == -1 and p_in_outbound == -1:
            return self.outbound_by_id()
        self.outbound_by_id_treeview.setup()
        self.outbound_by_id_treeview.insert_in_treeview(outbound, p_in_outbound)

    # =============================================================================
    def list_outbounds_by_clients(self):
        print('list_outbounds_by_clients')
        self.show_outbounds_frame()
        self.outbounds_by_client_view.setup()
        self.outbounds_by_client_view.search_btn.config(command=self.outbound_by_client_treeview_sec)

    def check_outbound_by_client_c(self):
        self.indexes, self.outbounds, self.p_in_outbound = self.admin_model.outbound_by_client_c(
            self.outbounds_by_client_view)
        return self.indexes, self.outbounds, self.p_in_outbound

    def outbound_by_client_treeview_sec(self):
        indexes, outbounds, p_in_outbound = self.check_outbound_by_client_c()
        if indexes == -1 and outbounds == -1 and p_in_outbound == -1:
            return self.list_outbounds_by_clients()
        self.outbounds_by_client_treeview.setup()
        self.outbounds_by_client_treeview.insert_in_treeview(indexes, outbounds, p_in_outbound)

    # =============================================================================

    def list_outbounds_by_time(self):
        print('list_outbounds_by_time')
        self.show_outbounds_frame()
        self.outbounds_by_time_view.setup()
        self.outbounds_by_time_view.search_btn.config(command=self.outbound_by_time_treeview_sec)

    def check_outbound_by_time_c(self):
        self.indexes, self.outbounds, self.p_in_outbound = self.admin_model.outbound_by_time_c(
            self.outbounds_by_time_view)
        return self.indexes, self.outbounds, self.p_in_outbound

    def outbound_by_time_treeview_sec(self):
        indexes, outbounds, p_in_outbound = self.check_outbound_by_time_c()
        if indexes == -1 and outbounds == -1 and p_in_outbound == -1:
            return self.list_outbounds_by_time()
        self.outbounds_by_time_treeview.setup()
        self.outbounds_by_time_treeview.insert_in_treeview(indexes, outbounds, p_in_outbound)

    # =============================================================================
    # ======================== PRODUCT ACTIONS ====================================
    def show_products_frame(self):
        print("PRODUCTS")
        self.clear_frame()
        self.products_panel.setup()
        self.products_panel.lst_all_products.config(command=self.lst_all_products)
        self.products_panel.lst_products_by_client.config(command=self.lst_products_by_client)
        self.products_panel.add_product.config(command=self.add_product)
        self.products_panel.delete_product.config(command=self.delete_product)
        self.products_panel.update_product.config(command=self.update_product)

    # =============================================================================
    def lst_all_products(self):
        print("lst_all_products")
        self.show_products_frame()
        self.lst_all_products_view.setup()
        products = self.admin_model.list_all_products_c()
        self.lst_all_products_view.insert_in_treeview(products)

    # =============================================================================
    def lst_products_by_client(self):
        print('lst_products_by_client')
        self.show_products_frame()
        self.products_by_client_view.setup()
        self.products_by_client_view.find_btn.config(command=self.lst_product_by_client_treeview)

    # def check_client_code_pr(self):
    #     indexes, products = self.admin_model.products_by_client_c(self.products_by_client_view)
    #     return indexes, products

    def lst_product_by_client_treeview(self):
        indexes, products = self.admin_model.products_by_client_c(self.products_by_client_view)
        if indexes == -1 and products -1:
            return self.lst_products_by_client()
        self.products_by_client_treeview.setup()
        self.products_by_client_treeview.insert_in_treeview(indexes, products)

    # =============================================================================
    def add_product(self):
        print('add_product')
        self.show_products_frame()
        self.add_product_view.setup()
        self.add_product_view.add_btn.config(command=self.submit_new_product_c)

    def submit_new_product_c(self):
        res = self.admin_model.add_product_c(self.add_product_view)
        if res == -1:
            self.add_product()

    # =============================================================================
    def delete_product(self):
        print('delete_product')
        self.show_products_frame()
        self.delete_product_view.setup()
        self.delete_product_view.delete_btn.config(command=self.delete_product_ac)

    def delete_product_ac(self):
        res = self.admin_model.delete_product_c(self.delete_product_view)
        if res == -1:
            self.add_product()

    # =============================================================================
    def update_product(self):
        print('update_product')
        self.show_products_frame()
        self.update_product_view.setup()
        self.update_product_view.update_btn.config(command=self.update_product_data)

    def update_product_data(self):
        print('update_product_data')
        self.products_update, self.index = self.admin_model.update_product_c(self.update_product_view)
        if self.products_update == -1 and self.index == -1:
            return self.update_product()
        self.show_products_frame()
        self.update_product_data_view.setup()
        self.update_product_data_view.save_btn.config(command=self.save_updated_product)

    def save_updated_product(self):
        self.admin_model.save_product_item_c(self.update_product_data_view,self.products_update,self.index)


    # =============================================================================
    # ======================== LOCATION ACTIONS====================================
    def show_locations_frame(self):
        print("LOCATIONS")
        self.clear_frame()
        self.locations_panel.setup()
        self.locations_panel.lst_all_locations.config(command=self.lst_all_locations_v)
        self.locations_panel.add_location.config(command=self.add_location_v)
        self.locations_panel.delete_location.config(command=self.delete_location_v)
        self.locations_panel.update_location.config(command=self.update_location_v)

    # =============================================================================
    def lst_all_locations_v(self):
        print('lst_all_locations_v')
        self.show_locations_frame()
        self.lst_all_locations_view.setup()
        locations = self.admin_model.list_all_locations_c()
        self.lst_all_locations_view.insert_in_treeview(locations)

    # =============================================================================
    def add_location_v(self):
        print('lst_all_locations_v')
        self.show_locations_frame()
        self.add_location_view.setup()
        self.add_location_view.add_btn.config(command=self.add_location_c)

    def add_location_c(self):
        res = self.admin_model.add_location_c(self.add_location_view)
        if res == -1:
            return self.add_location_v()

    # =============================================================================
    def delete_location_v(self):
        print('delete_location_v')
        self.show_locations_frame()
        self.delete_location_view.setup()
        self.delete_location_view.delete_btn.config(command=self.delete_location_c)

    def delete_location_c(self):
        res = self.admin_model.delete_location_c(self.delete_location_view)
        if res == -1:
            return self.delete_location_v

    # =============================================================================
    def update_location_v(self):
        print('update_location_v')
        self.show_locations_frame()
        self.update_location_view.setup()
        self.update_location_view.update_btn.config(command=self.update_location_data_v)

    def update_location_data_v(self):
        self.locations_update, self.index = self.admin_model.update_location_c(self.update_location_view)
        if self.locations_update == -1 and self.index == -1:
            return self.update_location_v()
        self.update_location_data_view.setup()
        self.update_location_data_view.add_btn.config(command=self.save_updated_location)

    def save_updated_location(self):
        self.admin_model.save_updated_location_c(self.update_location_data_view, self.locations_update, self.index)

