import time
import json

from api.bucket.aws import aws
from api.database import oracle
from api.database import db_items
from api import items


oracle.__run__()

# db_items.__drop_table__()
# db_items.__create_table__()

data = {
    "example": "abcd1234"
}
data_json = json.dumps(data)
timestamp = int(time.time())

db_items.__insert__(timestamp, "Facebook", "$69.69", 69, 1, data_json)

filename = "static/assets/images/facebook.png"
if aws.__upload__(filename, timestamp):
    url = aws.__get_url__(timestamp)
    print(url)

select_all = items.__select_all__(0, 5, "te")

print(select_all)

oracle.__stop__()