# from warehouseWorkerView import *
# from adminController import AppStart
# from wwModel import WwModel
from business_logic.ww_bl import WwModel
from main import AppStart
from views.ww_view import *


class WwController:
    def __init__(self, parent, user):
        self.parent = parent

        # model
        self.ww_model = WwModel(self.parent, user)

        # Client Main View
        self.ww_main_view = WarehouseWorkerMainView(self.parent, self)
        self.ww_main_view.username_label_text = user.username
        self.ww_main_view.role_label_text = user.role

        # Panel/Frames/Views
        self.placed_inbound_view = PlacedInboundOrderView(self.ww_main_view, self)
        self.placed_outbound_view = PlacedOutboundOrderView(self.ww_main_view, self)
        self.accepted_inbounds_view = AcceptedInboundsView(self.ww_main_view, self)
        self.accepted_outbounds_view = AcceptedOutboundsView(self.ww_main_view, self)
        self.change_location_view = ChangeLocationView(self.ww_main_view, self)
        self.change_location_action_view = ChangeLocationActionView(self.ww_main_view, self)


    def logout_command(self):
        self.parent.destroy()
        AppStart()

    def clear_frame(self):
        for widgets in self.ww_main_view.frame1.winfo_children():
            widgets.destroy()

# ==============================================================================
    def show_ww_main_view(self):
        print("WarehouseWorker")
        self.ww_main_view.setup()
        self.ww_main_view.placed_inbounds_btn.config(command=self.show_placed_inbounds_view)
        self.ww_main_view.placed_outbounds_btn.config(command=self.show_placed_outbounds_view)
        self.ww_main_view.accepted_inbounds_btn.config(command=self.show_accepted_inbounds_view)
        self.ww_main_view.accepted_outbounds_btn.config(command=self.show_accepted_outbounds_view)
        self.ww_main_view.change_location_btn.config(command=self.show_change_location_view)
        self.ww_main_view.logout.config(command=self.logout_command)


    def show_placed_inbounds_view(self):
        print('placed inbounds')
        self.clear_frame()
        self.placed_inbound_view.setup()
        self.new_inbounds, self.p_in_inbound = \
            self.ww_model.placed_inbound_orders_c(self.placed_inbound_view, self.ww_model.user)
        self.placed_inbound_view.insert_in_treeview(self.new_inbounds, self.p_in_inbound)
        self.placed_inbound_view.lst_all_locations.config(command=self.accept_inbound)

    def accept_inbound(self):
        res = self.ww_model.accept_inbound_c(self.placed_inbound_view.selected_item_id,self.new_inbounds)
        if res:
            # self.placed_inbound_view.selected_item_id = 0
            self.show_placed_inbounds_view()


    def show_placed_outbounds_view(self):
        print('placed outbounds')
        self.clear_frame()
        self.placed_outbound_view.setup()
        self.new_outbounds, self.p_in_outbound = \
            self.ww_model.placed_outbound_orders_c(self.placed_outbound_view, self.ww_model.user)
        self.placed_outbound_view.insert_in_treeview(self.new_outbounds, self.p_in_outbound)
        self.placed_outbound_view.lst_all_locations.config(command=self.accept_outbound)

    def accept_outbound(self):
        res = self.ww_model.accept_outbound_c(self.placed_outbound_view.selected_item_id,self.new_outbounds)
        if res:
            self.show_placed_outbounds_view()

# =====================================================================================
    def show_accepted_inbounds_view(self):
        print('accepted inbounds')
        self.clear_frame()
        self.accepted_inbounds_view.setup()
        acc_inbounds, p_in_inbound = self.ww_model.accepted_inbounds_c(self.accepted_inbounds_view, self.ww_model.user)
        self.accepted_inbounds_view.insert_in_treeview(acc_inbounds,p_in_inbound)

# ========================================================================================
    def show_accepted_outbounds_view(self):
        print('accepted outbounds')
        self.clear_frame()
        self.accepted_outbounds_view.setup()
        acc_outbounds, p_in_outbound = self.ww_model.accepted_outbounds_c(self.accepted_outbounds_view, self.ww_model.user)
        self.accepted_outbounds_view.insert_in_treeview(acc_outbounds, p_in_outbound)

# =======================================================================================

    def show_change_location_view(self):
        print('change location')
        self.clear_frame()
        self.change_location_view.setup()
        available_stock, self.locations , self.stock = \
            self.ww_model.change_location_c(self.change_location_view,self.ww_model.user)
        self.change_location_view.insert_in_treeview(available_stock, self.locations)
        self.change_location_view.change_loc.config(command=self.show_change_location_action_view)

    def show_change_location_action_view(self):
        print('location action view')
        self.clear_frame()
        self.change_location_action_view.setup()
        self.change_location_action_view.insert_in_treeview(self.locations)
        self.change_location_action_view.save_btn.config(command=self.save_location_c)

    def save_location_c(self):
        self.ww_model.save_location_to_item_c(self.change_location_action_view, self.ww_model.user, self.stock,
                                              self.change_location_view.selected_item_id)
        self.show_change_location_view()


