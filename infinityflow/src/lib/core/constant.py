from enum import Enum
class Os(Enum):
    Linux= 'linux'
    Windows= 'windows'
    Darwin= 'darwin'


class HostAttributes(Enum):
    HostPath = {
        Os.Linux.value: r'/opt/Automation',
        Os.Windows.value: r'C:\Automation',
        Os.Darwin.value: r'/opt/Automation'
    }
    


