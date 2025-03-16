import platform
import requests
import wmi


class Device:

    def __get_device__(self, name, model, operating_system, ip_address):
        self.name = name
        self.model = model
        self.operating_system = operating_system
        self.ip_address = ip_address

    def __new_device__(self, ID):
        self.ID = ID
        sys_info = platform.uname()
        self.name = sys_info.node
        c = wmi.WMI()
        my_system = c.Win32_ComputerSystem()[0]
        self.model = my_system.Manufacturer
        self.operating_system = f"{sys_info.system} {sys_info.release}"
        self.ip_address = requests.get('https://api.ipify.org').text
