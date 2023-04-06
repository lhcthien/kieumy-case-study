import json


class DbContext:
    USERS_DB = 'D:\\kieumy-case-study\\WMS_project_MVC-main\\WMS_project_MVC-main\\data_files\\users.json'
    INBOUNDS_DB = 'D:\\kieumy-case-study\\WMS_project_MVC-main\\WMS_project_MVC-main\\data_files\\inbounds.json'
    OUTBOUNDS_DB = 'D:\\kieumy-case-study\\WMS_project_MVC-main\\WMS_project_MVC-main\\data_files\\outbounds.json'
    PRODUCTS_DB = 'D:\\kieumy-case-study\\WMS_project_MVC-main\\WMS_project_MVC-main\\data_files\\products.json'
    STOCK_DB = 'D:\\kieumy-case-study\\WMS_project_MVC-main\\WMS_project_MVC-main\\data_files\\stock.json'
    LOCATIONS_DB = 'D:\\kieumy-case-study\\WMS_project_MVC-main\\WMS_project_MVC-main\\data_files\\locations.json'

    @staticmethod
    def load_from_json_file(filename):
        data_list = []
        with open(filename, 'r') as f:
            data = json.load(f)
            for i in data:
                data_list.append(i)
        return data_list


    @staticmethod
    def save_in_json_file(filename, collection):
        with open(filename, 'w+') as f:
            json.dump(collection, f, indent=4)


    @staticmethod
    def values_from_dictionary(outside_dict, key):
        dict_values = []
        for i in range(0, len(outside_dict)):
            dict_values.append(outside_dict[i].get(key))
        return dict_values