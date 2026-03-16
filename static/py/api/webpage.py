import json

from static.py.api.database import db_webpage

def __select__():
    return db_webpage.__select__()


def api(request_form, name):
    json_data = json.loads(request_form.get("data"))
    if db_webpage.__create_table__():
        temp_data = {
            "data": {
                "about": "This is temporary data for about",
                "policies": {
                    "Policy 1": "This is temporary data for Policy 1",
                    "Policy 2": "This is temporary data for Policy 2",
                    "Policy 3": "This is temporary data for Policy 3"
                }
            }
        }
        str_json = json.dumps(temp_data, indent=4)
        db_webpage.__insert__(str_json)

    if name == "select":
        return __select__()

    elif name == "update":
        webpage_data = json_data["data"]
        result = db_webpage.__update__(webpage_data)
        if not result:
            return result

        return True
