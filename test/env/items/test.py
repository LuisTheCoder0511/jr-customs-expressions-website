import time
import json

from env_files import env_load

from api.bucket.backblaze import backblaze
from api.database import oracle
from api.database import db_items
from api import items

env_load.load()
backblaze.__authenticate__()

oracle.__run__()

db_items.__drop_table__()
db_items.__create_table__()

data = {
    "example": "abcd1234"
}
data_json = json.dumps(data)
timestamp = int(time.time())

db_items.__insert__(timestamp, "Facebook", "$69.69", 69, 1, data_json)

filename = "static/assets/images/facebook.png"
if backblaze.__upload__(filename, f"{timestamp}.png"):
    url = backblaze.__get_url__(f"{timestamp}.png")
    print(url)

select_all = items.__select_all__(0, 5, "face")

print(select_all)

oracle.__stop__()