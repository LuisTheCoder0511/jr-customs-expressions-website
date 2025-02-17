from python_files import database
from python_files.tables import items
from python_files.objects.item import Item


database.__create_connection__()
items.__create_table__()
current_item = Item("blip", "", None, 0, 9.99, 1, "")
if not items.__retrieve_id__(current_item):
    result = items.__insert__(current_item)
    print(f"Insert... {result}")
    items.__retrieve_id__(current_item)

print(current_item.__dict__)
current_item = items.__get_item__("name")
items.__select_all__()
items.__select_list__("categoryID", 0)
database.__close_connection__()
