from business_logic.client_bl import ClientModel
from main import AppStart
from views.client_view import *


class ClientController:
    def __init__(self, parent, user):
        self.parent = parent

        # model
        self.client_model = ClientModel(self.parent,user)

        # Client Main View
        self.client_main_view = ClientMainView(self.parent, self)
        self.client_main_view.username_label_text = user.username
        self.client_main_view.role_label_text = user.role

        # Panel/Frames/Views
        self.place_inbound_panel = ClientPlaceInboundOrderView(self.client_main_view, self)
        self.add_products_to_inbound_view = AddProductsToInboundOrderView(self.client_main_view, self)
        self.place_outbound_panel = ClientPlaceOutboundOrderView(self.client_main_view, self)
        self.add_products_to_outbound_view = AddProductsToOutboundOrderView(self.client_main_view, self)
        self.placed_inbounds_view = PlacedInboundsView(self.client_main_view, self)
        self.placed_outbounds_view = PlacedOutboundsView(self.client_main_view, self)
        self.lst_all_products_view = ListAllProductsView(self.client_main_view, self)


    def logout_command(self):
        self.parent.destroy()
        AppStart()

    def clear_frame(self):
        for widgets in self.client_main_view.frame1.winfo_children():
            widgets.destroy()

    def show_client_main_view(self):
        print("client_main_view")
        self.client_main_view.setup()
        self.client_main_view.place_inbound_order_btn.config(command=self.place_inbound_frame)
        self.client_main_view.place_outbound_order_btn.config(command=self.place_outbound_frame)
        self.client_main_view.placed_inbounds_btn.config(command=self.placed_inbounds_frame)
        self.client_main_view.placed_outbounds_btn.config(command=self.placed_outbounds_frame)
        self.client_main_view.list_all_products_btn.config(command=self.lst_all_products_frame)
        self.client_main_view.logout.config(command=self.logout_command)


# ===============================================================================================
# =========================== INBOUND PLACE ORDER===============================================
    def place_inbound_frame(self):
        print("place_inbound_frame")
        self.clear_frame()
        self.place_inbound_panel.setup()
        self.place_inbound_panel.product_entry_btn.config(command=self.add_products_to_inbound_frame)

    def add_products_to_inbound_frame(self):
        print("add_products_to_inbound_frame")
        self.inbound_products_lst = []
        self.add_products_to_inbound_view.setup()
        self.add_products_to_inbound_view.save_btn_add.config(command=self.add_products_to_inbound_c)
        self.add_products_to_inbound_view.save_btn.config(command=self.submit_inbound_to_db)

    def add_products_to_inbound_c(self):
        self.client_model.add_products_to_inbound_c(self.add_products_to_inbound_view,self.inbound_products_lst)

    def submit_inbound_to_db(self):
        self.client_model.submit_inbound_c(self.place_inbound_panel, self.client_model.user,self.inbound_products_lst)

# ===============================================================================================
# =========================== OUTBOUND PLACE ORDER===============================================
    def place_outbound_frame(self):
        print("place_outbound_frame")
        self.clear_frame()
        self.place_outbound_panel.setup()
        self.place_outbound_panel.product_entry_btn.config(command=self.add_products_to_outbound_frame)

    def add_products_to_outbound_frame(self):
        print("add_products_to_inbound_frame")
        self.outbound_products_lst = []
        self.add_products_to_outbound_view.setup()
        self.add_products_to_outbound_view.save_btn_add.config(command=self.add_products_to_outbound_c)
        self.add_products_to_outbound_view.save_btn.config(command=self.submit_outbound_to_db)

    def add_products_to_outbound_c(self):
        self.client_model.add_products_to_outbound_c(self.add_products_to_outbound_view,self.outbound_products_lst)

    def submit_outbound_to_db(self):
        self.client_model.submit_outbound_c(self.place_outbound_panel,self.client_model.user,self.outbound_products_lst)

# ===============================================================================================
# =========================== INBOUND PLACED ORDERS =============================================

    def placed_inbounds_frame(self):
        print("placed_inbounds_frame")
        self.clear_frame()
        self.placed_inbounds_view.setup()
        indexes, inbounds,p_in_inbound = \
            self.client_model.placed_inbounds_c(self.placed_inbounds_view,self.client_model.user)
        self.placed_inbounds_view.insert_in_treeview(indexes,inbounds,p_in_inbound)

# ===============================================================================================
# =========================== OUTBOUND PLACED ORDERS ============================================
    def placed_outbounds_frame(self):
        print("placed_outbounds_frame")
        self.clear_frame()
        self.placed_outbounds_view.setup()
        indexes, outbounds, p_in_outbound = \
            self.client_model.placed_outbounds_c(self.placed_outbounds_view,self.client_model.user)
        self.placed_outbounds_view.insert_in_treeview(indexes, outbounds, p_in_outbound)

# ===============================================================================================
# =========================== LIST ALL PRODUCTS =================================================
    def lst_all_products_frame(self):
        print("lst_all_products_frame")
        self.clear_frame()
        self.lst_all_products_view.setup()
        indexes, products = self.client_model.list_all_products_c(self.client_model.user)
        self.lst_all_products_view.insert_in_treeview(indexes,products)