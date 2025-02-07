from python_files import codegen
from python_files import database
from python_files.tables import device_history_table
from python_files.objects.device import Device


def create_table():
    device_history_table.__create_table__()


def add_device(device: Device):
    device_history_table.__insert__(device)


def remove_device(device_id):
    device_history_table.__delete__(device_id)


def select_all():
    return database.__select_all__("device_history", "device_id")


def select_one(device_id):
    return database.__select_one__("device_history", "device_id", device_id)


def code_generator(device_ids):
    return codegen.CodeGenerator(device_ids)


ids = select_all()
code_gen = code_generator(ids)
my_device_blueprint = select_one(ids[0])
print(my_device_blueprint)
my_device = Device()
my_device.__get_device__(my_device_blueprint)
print(my_device.__dict__)
# my_device = Device(code_gen)
# add_device(my_device)
