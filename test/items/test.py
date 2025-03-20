import time
import json

from api.database import oracle
from api.database import db_items
from api import items


oracle.__run__()

db_items.__drop_table__()
db_items.__create_table__()

data = {
    "example": "abcd1234"
}
data_json = json.dumps(data)
db_items.__insert__(int(time.time()), "Test", "$6.64", 4, data_json)
select_all = items.__select_all__(0, 5, "te")

print(select_all)

oracle.__stop__()