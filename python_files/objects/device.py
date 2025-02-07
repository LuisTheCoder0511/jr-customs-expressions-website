import platform
import requests
import wmi

from python_files.codegen import CodeGenerator


class Device:

    def __get_device__(self, device_blueprint):
        self.device_id = device_blueprint[0]
        self.name = device_blueprint[1]
        self.model = device_blueprint[2]
        self.operating_system = device_blueprint[3]
        self.ip_address = device_blueprint[4]

    def __new_device__(self, codegen: CodeGenerator):
        self.device_id = codegen.__generate__()
        sys_info = platform.uname()
        self.name = sys_info.node
        c = wmi.WMI()
        my_system = c.Win32_ComputerSystem()[0]
        self.model = my_system.Manufacturer
        self.operating_system = f"{sys_info.system} {sys_info.release}"
        self.ip_address = requests.get('https://api.ipify.org').text

