import json
import os
import time


def check_file():
    appdata = os.path.join(os.environ['APPDATA'])

    folder = os.path.join(appdata, "JRCustomsExpressions")
    file = os.path.join(folder, "user.json")

    if os.path.exists(folder) and os.path.exists(file):
        with open(file, "r") as f:
            data = json.load(f)["account"]

            timestamp_now = int(time.time() / 60)
            timestamp_current = data["timestamp"]
            remember = data["remember"]

            if timestamp_current and (not remember and timestamp_now - timestamp_current < 60) \
                or (remember and timestamp_now - timestamp_current < 43_200):
                return True

        return False

    if not os.path.exists(folder):
        os.mkdir(folder)

    if not os.path.exists(file):
        user = {
            "account": {
                "username": None,
                "timestamp": None,
                "remember": False
            }
        }

        with open(file, "w") as f:
            json.dump(user, f, indent=4)
            os.startfile(folder)

    return False

