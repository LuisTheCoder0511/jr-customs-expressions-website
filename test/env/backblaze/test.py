from api.bucket.backblaze import backblaze
import time
from env_files import env_load

env_load.load()

backblaze.__authenticate__()

filename = "static/assets/images/Image_Test_Template.png"
timestamp = int(time.time())
global_filename = f"{timestamp}.png"
if backblaze.__upload__(filename, global_filename):
    url = backblaze.__get_url__(global_filename)
    print(url)

    time.sleep(10)

    backblaze.__delete__(global_filename)

