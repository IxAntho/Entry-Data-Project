from zillow_data_manager import ZillowDataManager
from form_data_entry import FormDataEntry

data_manager = ZillowDataManager()
data_manager.property_data()
form_manager = FormDataEntry()
form_manager.type_values(data_manager.links, data_manager.prices, data_manager.addresses)
