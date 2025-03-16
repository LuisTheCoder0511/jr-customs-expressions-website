import time

from scripts.database import db_items
from scripts.database.oracle import database
import json

db_items.__drop_table__()
db_items.__create_table__()
data = json.dumps({})
db_items.__insert__(int(time.time()), "Item", "6.49", 14, data)
data = db_items.__select_all__(0, 10)
print(data)
database.__close__()
