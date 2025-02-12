from python_files import database


class DeviceHistory:

    def __init__(self):
        self.device_id = 1
        self.null_device_ids = []
        self.table = {}

    def __add__(self, device):
        current_device_id = self.device_id
        if not len(self.null_device_ids) == 0:
            current_device_id = self.null_device_ids[0]
            del self.null_device_ids[0]
        else:
            self.device_id += 1

        self.table[current_device_id] = device

    def __remove__(self, device_id):
        if device_id in self.null_device_ids:
            del self.table[device_id]
        self.null_device_ids.append(device_id)

    def __get__(self, device_id):
        return self.table[device_id]

    def __load_devices__(self):
        database.__create_connection__()



        database.__close_connection__()
