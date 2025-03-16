from python_files.tables import items
from python_files.objects.item import Item


items.__connect_to_db__()
# print(f"Table: {items.__create_table__()}")

print(items.__select_all__(10, 0))

# new_item = Item("Name",
#                 "Description",
#                 None,
#                 [],
#                 9.99,
#                 2,
#                 "{}")
#
#
# result = items.__insert__(new_item)
# print(result)
#
# print(new_item.__dict__)
#
# data = items.__select_all__(10, 0)
# print(data)

items.__disconnect_from_db__()
