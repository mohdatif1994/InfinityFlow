"""Host Info Lib"""
from __future__ import annotations

import platform
import socket


class HostInfo:
    """Host Info Class."""

    @staticmethod
    def get_hostname():
        """
        Gets the hostname of the current machine.

        :return: The hostname as a string.
        """
        return socket.gethostname()

    @staticmethod
    def get_ip_address():
        """
        Gets the IP address of the current machine.

        :return: The IP address as a string.
        """
        hostname = HostInfo.get_hostname()
        return socket.gethostbyname(hostname)

    @staticmethod
    def get_fqdn():
        """
        Gets the Fully Qualified Domain Name (FQDN) of the current machine.

        :return: The FQDN as a string.
        """
        return socket.getfqdn()

    @staticmethod
    def get_os_name():
        """
        Gets the name of the operating system.

        :return: The OS name as a string.
        """
        return platform.system()

    @staticmethod
    def get_os_version():
        """
        Gets the version of the operating system.

        :return: The OS version as a string.
        """
        return platform.version()

    @staticmethod
    def get_os_release():
        """
        Gets the release of the operating system.

        :return: The OS release as a string.
        """
        return platform.release()

    @staticmethod
    def get_machine():
        """
        Gets the machine type, e.g., 'i386'.

        :return: The machine type as a string.
        """
        return platform.machine()

    @staticmethod
    def get_processor():
        """
        Gets the processor type, e.g., 'i386'.

        :return: The processor type as a string.
        """
        return platform.processor()

    @staticmethod
    def get_platform():
        """
        Gets a single string identifying the underlying platform.

        :return: The platform as a string.
        """
        return platform.platform()

    @staticmethod
    def get_host_info():
        """
        Gets the detailed host information including OS details.

        :return: A dictionary containing the host information.
        """
        return {
            "hostname": HostInfo.get_hostname(),
            "ip_address": HostInfo.get_ip_address(),
            "fqdn": HostInfo.get_fqdn(),
            "os_name": HostInfo.get_os_name(),
            "os_version": HostInfo.get_os_version(),
            "os_release": HostInfo.get_os_release(),
            "machine": HostInfo.get_machine(),
            "processor": HostInfo.get_processor(),
            "platform": HostInfo.get_platform(),
        }


# Usage
host_info = HostInfo.get_host_info()
for key, value in host_info.items():
    print(f"{key}: {value}")
